from flask import current_app
from ..core import Service, guard
from .models import User



class UsersService(Service):
  __model__ = User


  def signup(self, req):
    """
      Registers a new user by parsing a POST request containing new user info
    """    
    if self.first(username=req['username']):
      return {'Error': 'User exist.'}, 400
    
    email = req.get('email', None)
    req['password'] = guard.hash_password(req['password'])

    new_user = self.create(**req)
    guard.send_registration_email(
      email, 
      user=new_user,   
      confirmation_sender = current_app.config.get('PRAETORIAN_CONFIRMATION_SENDER')      
    )

    ret = {'message': 'successfully sent registration email to user {}'.format(
        new_user.username
    )}

    return ret, 201


  def activate(self):
    """
      Activate registered user througth email confirmation token
    """        
    registration_token = guard.read_token_from_header()
    user = guard.get_user_from_registration_token(registration_token)       
    user.is_active = True

    self.update(user)

    ret = {'access_token': guard.encode_jwt_token(
      user,
      firstname=user.first_name,
      lastname=user.last_name,
    )}

    return ret, 200

  def update_password(self, user, password):
    user.password = guard.hash_password(password)
    self.update(user)

    ret = {'message': 'Success'}

    return ret, 200



users = UsersService()