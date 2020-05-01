# -*- coding: utf-8 -*-
"""
    tlinks.services
    ~~~~~~~~~~~~~~~~~
    services module
"""

from .users import UsersService


#: An instance of the :class:`UsersService` class
users = UsersService()