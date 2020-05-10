# -*- coding: utf-8 -*-
"""
    main.users
    ~~~~~~~~~~~~~~
    main users package
"""

from ..services import users
from ..router import route
from flask import Blueprint, jsonify, request, current_app
from ..core import guard
from ..templates import get_template

bp = Blueprint('auth', __name__)

@bp.route('/login')
def login():
    """
    Logs a user in by parsing a POST request containing user credentials and
    issuing a JWT token.
    """  
    req = request.get_json(force=True)
    username = req.get('username', None)
    password = req.get('password', None)

    user = guard.authenticate(username, password)
    ret = {'access_token': guard.encode_jwt_token(
      user,
      firstname=user.first_name,
      lastname=user.last_name,
    )}
    
    return (ret, 200)


@bp.route('/refresh', methods=['GET'])
def refresh():
    """
    Refreshes an existing JWT by creating a new one that is a copy of the old
    except that it has a refrehsed access expiration.
    """

    old_token = guard.read_token_from_header()
    new_token = guard.refresh_jwt_token(old_token)
    ret = {'access_token': new_token}
    return ret, 200


@bp.route('/request-password', methods=['POST'])
def request_reset_password():
  """
    Sends a password reset email to a user, containing a time expiring
    token usable for validation. 
  """
  payload = request.get_json()

  guard.send_reset_email(
    payload['email'], 
    reset_sender = current_app.config['MAIL_USERNAME'],
    template = get_template('emails/request_password')
  )

  return ("success", 200)


@route(bp, '/<user_id>')
def show(user_id):
    """Returns a user instance."""
    return users.get_or_404(user_id)
