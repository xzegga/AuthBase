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

@bp.route('/signup', methods=['POST'])
def signup():
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


@route(bp, '/')
def whoami():
    """Returns the user instance of the currently authenticated user."""    
    return users.all()