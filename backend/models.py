from pony.orm import Database, Required, PrimaryKey, db_session, TransactionIntegrityError, perm
from backend.config import config

db = Database()

def initialize_db():
	db.bind(**config['PONY'])
	db.generate_mapping(create_tables=True)
	with db.set_perms_for(User):
		perm('view edit delete create', group='anybody')
	with db_session:
		if User.select().first() is None:
			populate_db()

def populate_db():
	with db_session:
		try:
			u1 = User(first_name='John', last_name='Doe', user_name='j.doe', street='Example Street 1', city="Exampletown", zip="12345"),
			u2 = User(first_name='Roberta', last_name='Foo', user_name='r.foo',  street='Another Street 12', city="Differentino", zip="54321"),
			db.commit()
		except TransactionIntegrityError as err:
			print('DB ERROR', err)


class User(db.Entity):
	id = PrimaryKey(int, auto=True)
	first_name = Required(str, max_len=100)
	last_name = Required(str, max_len=100)
	user_name = Required(str, max_len=250, unique=True)
	street = Required(str,max_len=250)
	city = Required(str, max_len=100)
	zip = Required(str, max_len=12)

	def dictify(self):
		return dict(
			id = self.id,
			first_name = self.first_name,
			last_name = self.last_name,
			user_name = self.user_name,
			street = self.street,
			city = self.city,
			zip = self.zip
		)
