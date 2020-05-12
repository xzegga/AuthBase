# -*- coding: utf-8 -*-
"""
    main.auth
    ~~~~~~~~~~~~~~
    main auth package
"""

from .services import auth
from ..router import route
from ..core import guard
from flask import Blueprint, request


bp = Blueprint('auth', __name__)

@bp.route('/login', methods=['POST'])
def signin():
  """
  Logs a user in by parsing a POST request containing user credentials and
  issuing a JWT token.
  """  
  req = request.get_json(force=True)        
  return auth.signin(req)


@bp.route('/refresh', methods=['GET'])
def refresh():
  """
    Refreshes an existing JWT by creating a new one that is a copy of the old
    except that it has a refrehsed access expiration.
  """
  return auth.refresh_token()


@bp.route('/request-password', methods=['POST'])
def request_password_reset():
  """
    Sends a password reset email to a user, containing a time expiring
    token usable for validation. 
  """
  req = request.get_json()  
  return auth.password_request(req)


@bp.route('/validate_reset/<string:token>', methods=['POST'])
def request_token(token):
  """
    
  """ 
  return auth.verify_token(token)


@bp.route('/password_reset/<string:token>', methods=['POST'])
def password_reset(token):
  """
    
  """ 
  req = request.get_json()
  return auth.password_match(req, token)


@bp.route('/logout', methods=['DELETE'])
def logoutAccount():
  """
    
  """ 
  return auth.invalid_token()
