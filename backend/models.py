from pony.orm import Database, Required, PrimaryKey, db_session, TransactionIntegrityError, perm
from backend.config import config, db_path
import os

db = Database()

def initialize_db():
	"""
	Create database bindings (SQLite) and prepopulate some example data if empty.
	"""
	try:
		if not os.path.exists(db_path):
			print(' * Creating database in: {}'.format(db_path))
			os.makedirs(db_path)
		db.bind(**config['PONY'])
		db.generate_mapping(create_tables=True)
		with db.set_perms_for(User):
			perm('view edit delete create', group='anybody')
		with db_session:
			if User.select().first() is None:
				populate_db()
	except Exception as err:
		print('Error creating or binding to database:', err)

def populate_db():
	"""
	Simple sxample data to prepopulate in the database if it is empty.
	"""
	with db_session:
		try:
			u1 = User(first_name='John', last_name='Doe', user_name='j.doe', street='Example Street 1', city="Exampletown", zip="12345"),
			u2 = User(first_name='Roberta', last_name='Foo', user_name='r.foo',  street='Another Street 12', city="Differentino", zip="54321"),
			db.commit()
		except TransactionIntegrityError as err:
			print('Error creating example users:', err)


class User(db.Entity):
	id = PrimaryKey(int, auto=True)
	first_name = Required(str, max_len=100)
	last_name = Required(str, max_len=100)
	user_name = Required(str, max_len=250, unique=True)
	street = Required(str,max_len=250)
	city = Required(str, max_len=100)
	zip = Required(str, max_len=12)

	def dictify(self):
		"""
		Returns a simple dict-representation of the entity that can easily be JSON-
		serialized by Flask on return.
		"""
		return dict(
			id = self.id,
			first_name = self.first_name,
			last_name = self.last_name,
			user_name = self.user_name,
			street = self.street,
			city = self.city,
			zip = self.zip
		)
