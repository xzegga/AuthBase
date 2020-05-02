from . import app
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from core import db

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_user('db', MigrateCommand)

if __name__ == "__main__":
    manager.run()