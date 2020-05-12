import click
from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask.cli import with_appcontext

from main.core import db, guard
from main.models import User
from main.users.services import users

from main import create_app
from flask_script import Manager, Command


class create_users(Command):
  """Create a user"""
  
  def run(self):
    company_user = User(username='xzegga', email='raul.escamilla@asesoriait.com', password=guard.hash_password('super.super'),   
    first_name='Raul', last_name='Escamilla', roles='company')
    interpreter_user = User(username='inversiones', email='inversiones@asesoriait.com', password=guard.hash_password('super.super'), first_name='Alberto', last_name='Salinas', roles='interpreter')
    users.save(company_user)
    users.save(interpreter_user)


app = create_app()
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)
manager.add_command('create_users', create_users())

if __name__ == '__main__':
    manager.run()



