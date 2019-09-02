from pathlib import Path
from os import path

db_path = path.join(Path.home(), '.mini_admin/')

config = dict(
  DEBUG = False,
  PONY = {
    'provider': 'sqlite',
    'filename': path.join(db_path, 'admin.db'),
    'create_db': True
  }
)