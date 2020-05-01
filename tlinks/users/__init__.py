# -*- coding: utf-8 -*-
"""
    tlinks.users
    ~~~~~~~~~~~~~~
    tlinks users package
"""

from ..core import Service
from .models import User


class UsersService(Service):
    __model__ = User