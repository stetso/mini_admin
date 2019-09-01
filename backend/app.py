from flask import Flask, request, render_template, send_from_directory
from flask.cli import FlaskGroup
from flask_cors import CORS
from pony.flask import Pony
from pony.orm import db_session, select
from backend.models import db, User, initialize_db

def create_app():
	app = Flask(
		__name__,
		static_folder='../frontend/public',
		static_url_path='/frontend/public'
		)
	CORS(app)

	# initialize ORM
	initialize_db()
	Pony(app)

	@app.route('/admin')
	def serve_admin():
		return send_from_directory(app.static_folder, 'index.html')


	@app.route('/user', methods=['GET', 'POST'])
	def user():
		if request.method == 'GET':
			with db_session:
				users = select(u for u in User)[:]
				return dict(data=[u.dictify() for u in users])
		if request.method == 'POST':
			try:
				body = request.json
				# TODO: check body catch errors (let the ORM handle the validation)
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

	return app

cli = FlaskGroup(create_app=create_app)

if __name__ == '__main__':
	cli()