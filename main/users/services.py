from flask import current_app
from ..core import Service, guard
from .models import User

CONFIRMATION_SENDER = current_app.config.get('PRAETORIAN_CONFIRMATION_SENDER')   

class UsersService(Service):
  __model__ = User

  def get_authenticated_user_id(self):
    registration_token = guard.read_token_from_header()
    user = guard.get_user_from_registration_token(registration_token) 
    return user.id


  def get_authenticated_user(self):
    registration_token = guard.read_token_from_header()
    user = guard.get_user_from_registration_token(registration_token) 
    return user


  def signup(self, req):
    """
      Registers a new user by parsing a POST request containing new user info and
      dispatching an email with a registration token
    """  
    email = req.get('email', None)
    req['username'] = email

    if self.first(username=email):
      return {'message': 'There is an user related with this email'}, 400
    
    # Hasing password to save encrypted
    req['password'] = guard.hash_password(req['password'])

    new_user = self.create(**req)
    guard.send_registration_email(
      email, 
      user=new_user,   
      confirmation_sender = CONFIRMATION_SENDER
    )

    ret = {'message': 'Email has been sent to {}, please confirm your email to activate your account'.format(
        new_user.email
    )}, 201

    return ret
   

  def activate(self):
    """
      Finalizes a user registration with the token that they were issued in their
      registration email
    """        
    user = self.get_authenticated_user()     
    user.is_active = True

    self.update(user)

    ret = {'access_token': guard.encode_jwt_token(
      user,
      firstname=user.first_name,
      lastname=user.last_name,
    )}, 200

    return ret


  def update_password(self, user, password):
    """
      Update user password in the database
    """
    user.password = guard.hash_password(password)
    self.update(user)
    ret = {'message': 'Password updated successfully'}, 200

    return ret


users = UsersService()
