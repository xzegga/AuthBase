from flask import current_app
from ..core import Service, guard, bl
from ..templates import get_template
from ..users import users
from .models import Token



class AuthService(Service):
  __model__ = Token

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
    ret = {'access_token': new_token}

    return ret, 200

  def password_request(self, req):
    """
    
    """
    guard.send_reset_email(
      req['email'],
      reset_sender=current_app.config['MAIL_USERNAME'],
      template=get_template('emails/request_password')
    )
    return {"messasge": "A reset password e-mail has been sent to you. Please check your inbox"}, 200

  def verify_token(self, token):
    """

    """
    guard.validate_reset_token(token)

    return {"valid": "true"}, 200

  def password_match(self, req, token):  
    """

    """
    user = guard.validate_reset_token(token)
    if user:
      if req["new_password"] == req["password_confirm"]:
        users.update_password(user, req["new_password"])

    return {"Message": "Password change success"}, 200


  def invalid_token(self):
    token = guard.read_token_from_header()
    jti = guard.extract_jwt_token(token)["jti"]
    bl.blacklist_jti(jti)
    rv, code = {"success": True, "message": "token invalidated"}, 200
    return rv, code


auth = AuthService()
