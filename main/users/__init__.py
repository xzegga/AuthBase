# -*- coding: utf-8 -*-
"""
    main.users
    ~~~~~~~~~~~~~~
    main users package
"""
from ..services import users
from ..router import route
from flask import Blueprint, request

bp = Blueprint('users', __name__, url_prefix='/users')

@bp.route('/register', methods=['POST'])
def register():
  """
    Registers a new user by parsing a POST request containing new user info and
    dispatching an email with a registration token
  """
  data = request.get_json()
  return users.register(data)


@route(bp, '/')
def whoami():
    """Returns the user instance of the currently authenticated user."""    
    return users.all()


@route(bp, '/<user_id>')
def show(user_id):
    """Returns a user instance."""
    return users.get_or_404(user_id)

