# -*- coding: utf-8 -*-
"""
    tlinks.users
    ~~~~~~~~~~~~~~~~~~
    User endpoints
"""
from flask_login import current_user
from ..services import users
from ..router import route
from flask import Blueprint

bp = Blueprint('users', __name__, url_prefix='/users')

@route(bp, '/')
def whoami():
    """Returns the user instance of the currently authenticated user."""
    return {'name': 'Raúl Escamilla'}
    # return current_user._get_current_object()


@route(bp, '/<user_id>')
def show(user_id):
    """Returns a user instance."""
    return users.get_or_404(user_id)