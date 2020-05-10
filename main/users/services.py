from ..core import Service, guard
from flask_mail import Message
from .models import User
from flask import current_app, render_template
import os

class UsersService(Service):
  __model__ = User

  def hash_password(self, password):
      return guard.hash_password(password)

  def exist(self, email):
    return self.first(username=email)


  def signup(self, data):
    if not self.exist(data['username']):
      data['password'] = self.hash_password(data['password'])
      return self.create(**data)
    else:
      return {'Error': 'User exist.'}, 400


