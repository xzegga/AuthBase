from flask import current_app
from ..core import guard
from ..templates import get_template

class AuthService():
  
  def signin(self, req):
    
    username = req.get('username', None)
    password = req.get('password', None)

    user = guard.authenticate(username, password)
    ret = {'access_token': guard.encode_jwt_token(
      user,
      firstname=user.first_name,
      lastname=user.last_name,
    )}

    return ret, 200


  def refresh_token(self):
    
    old_token = guard.read_token_from_header()
    new_token = guard.refresh_jwt_token(old_token)
    ret = {'access_token': new_token }

    return ret, 200


  def request_password(self, req):
   
    guard.send_reset_email(
      req['email'], 
      reset_sender = current_app.config['MAIL_USERNAME'],
      template = get_template('emails/request_password')
    )

    return {"messasge": "A reset password e-mail has been sent to you. Please check your inbox"}, 200
