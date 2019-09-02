from flask import Flask, request, render_template, send_from_directory, abort, Response
from flask.cli import FlaskGroup
from flask_cors import CORS
from pony.flask import Pony
from pony.orm import db_session, select
from backend.models import db, User, initialize_db

def create_app():
	"""
	Create the basic Flask application.

	Following the factory patter, this function creates a Flask application an runs it.
	Theoretically, multiple instances could be run, however for this example only
	a single one will.

	Returns:
	app: a flask app object
	"""

	app = Flask(
		__name__,
		template_folder='templates',
		static_folder='../frontend/public',
		static_url_path='/frontend/public'
		)
	CORS(app)

	# initialize ORM
	initialize_db()
	Pony(app)

	# error pages
	@app.errorhandler(404)
	def handle_404(error):
		"""
		Signal Not Found errors to the client.
		"""
		return render_template('404.html'), 404

	@app.errorhandler(500)
	def handle_500(error):
		"""
		Signal internal server errors to the client.
		"""
		return render_template('500.html'), 500

	@app.route('/admin')
	def serve_admin():
		"""
		The route which serves the Svelte SPA with the User administration
		widget. The SPA files need to be in a compiled form already and are
		served statically.
		"""
		return send_from_directory(app.static_folder, 'index.html')

	@app.route('/user', methods=['GET', 'POST'])
	def user():
		"""
		The basic User route for a simple JSON-CRUD-API. At the moment only supports
		READ all users and CREATE a single user but could be extended easily.

		Returns:
		{data: [User]}: a JSON object containing a list of all users on GET
		or
		{data: User}: a JSON object containing the single user that was just created on POST
		"""
		if request.method == 'GET':
			try:
				with db_session:
					users = select(u for u in User)[:]
					return dict(data=[u.dictify() for u in users])
			except Exception as e:
				abort(Response('Error: could not get user list from database.'))
		if request.method == 'POST':
			try:
				body = request.json
				with db_session:
					u = User(
						first_name = body['first_name'],
						last_name=body['last_name'],
						user_name=body['user_name'],
						street = body['street'],
						city = body['city'],
						zip = body['zip']
						)
					db.commit()
					return dict(data=u.dictify())
			except Exception as err:
				app.logger.error('Error creating user object:', err)
				abort(Response('Error: Could not create user object in database.'))

	return app

cli = FlaskGroup(create_app=create_app)

if __name__ == '__main__':
	cli()