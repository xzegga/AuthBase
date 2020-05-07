from ..core import Service, guard, mail
from flask_mail import Message
from .models import User
import os

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
    
  def sendForgotPass(self, payload):
    # if not self.exist(payload['username']):
    #   return {"Error": "The email you entered does not exist in our records"}, 400

    # try:
    #   token = guard.encode_jwt_token(payload)
   
    mail.username = os.environ.get('MAIL_USERNAME')
    print(mail.username, mail.password)
    object_email = Message("HEllo world",
                            recipients=["albertolinares001@gmail.com"])
    mail.send(object_email)

    # except Exception as identifier:
    #   pass


    



