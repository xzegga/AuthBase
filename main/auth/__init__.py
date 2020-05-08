# -*- coding: utf-8 -*-
"""
    main.users
    ~~~~~~~~~~~~~~
    main users package
"""

from ..services import users
from ..router import route
from flask import Blueprint, jsonify, request
from ..core import guard

bp = Blueprint('auth', __name__)

@bp.route('/login')
def login():
    """Returns the user instance."""    
    json_data = request.get_json()
    username = json_data['username']
    password = json_data['password']
    user = guard.authenticate(username, password)
    
    return {'token': guard.encode_jwt_token(user)}


@route(bp, '/<user_id>')
def show(user_id):
    """Returns a user instance."""
    return users.get_or_404(user_id)

@bp.route('/forgot_pass', methods=['POST'])
def emailCatch():
  # get the post data
  payload = request.get_json()
  return users.request_password(payload)