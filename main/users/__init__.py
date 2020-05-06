# -*- coding: utf-8 -*-
"""
    main.users
    ~~~~~~~~~~~~~~
    main users package
"""
from ..services import users
from ..router import route
from flask import Blueprint, request
from ..core import guard

bp = Blueprint('users', __name__, url_prefix='/users')

@route(bp, '/')
def whoami():
    """Returns the user instance of the currently authenticated user."""    
    return users.all()


@route(bp, '/<user_id>')
def show(user_id):
    """Returns a user instance."""
    return users.get_or_404(user_id)

@bp.route('/register', methods=['POST'])
def register(data):
  data = request.get_json(data)
  data['password'] = guard.encrypt_password(data['password'])
  return users.create(data)
