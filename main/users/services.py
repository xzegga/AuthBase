from ..core import Service, guard
from .models import User

class UsersService(Service):
  __model__ = User

  def hash_password(self, password):
      return guard.hash_password(password)

  def exist(self, email):
    return self.first(username=email)

  def register(self, data):
    if not self.exist(data['username']):
      data['password'] = self.hash_password(data['password'])
      return self.create(**data)
    else:
      return {'Error': 'User exist.'}, 400
    




    



