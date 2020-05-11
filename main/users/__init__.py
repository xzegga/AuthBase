# -*- coding: utf-8 -*-
"""
    main.users
    ~~~~~~~~~~~~~~
    main users package
"""

from .services import users
from ..router import route
from flask import Blueprint, request

bp = Blueprint('users', __name__, url_prefix='/users')

@bp.route('/singup', methods=['POST'])
def singup():
  """
  Registers a new user by parsing a POST request containing new user info and
  dispatching an email with a registration token
  """
  req = request.get_json()
  return users.signup(req)


@bp.route('/confirm', methods=['POST'])
def confirm():
  """
  Finalizes a user registration with the token that they were issued in their
  registration email
  """   
  return users.activate()
