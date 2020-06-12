# -*- coding: utf-8 -*-
"""
    main.users
    ~~~~~~~~~~~~~~
    main users package
"""

from .services import users
from ..router import route
from flask import Blueprint, request

bp = Blueprint('users', __name__, url_prefix='/')

@bp.route('/signup', methods=['POST'])
def signup():
  req = request.get_json()
  return users.signup(req)


@bp.route('/confirm', methods=['POST'])
def confirm():
  return users.activate()


@route(bp, '/users')
def whoami():
    return users.all()
