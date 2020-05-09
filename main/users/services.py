from ..core import Service, guard, mail
from ..mails.emails import ForgotPasswordTemplate
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


  def request_password(self, payload):
    user = self.exist(payload['username'])
    if not user:
      return {"Error": "The email you entered does not exist in our records"}, 400

    #try:    
    
    token = guard.encode_jwt_token(user)
    
    email_template = ForgotPasswordTemplate(token)

    mail.username = os.environ.get('MAIL_USERNAME')
    mail.password = os.environ.get('MAIL_PASSWORD')

    print(mail.username, mail.password)

    object_email = Message("Cambio de contraseña", recipients=["albertolinares001@gmail.com"])
    object_email.body = email_template['text']
    object_email.html = email_template['html']

    mail.send(object_email)

    return 'Sent'

    # except Exception as identifier:
    #   pass
      # print(identifier.__dict__)
      # return {
      #       'message': 'Hubo un error al enviar el correo, favor intentarlo más tarde.' 
      #   }, 400


    



