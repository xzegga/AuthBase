# -*- coding: utf-8 -*-
"""
    main.services
    ~~~~~~~~~~~~~~~~~
    services module
"""
from .auth.services import AuthService
from .users.services import UsersService

users = UsersService()
auth = AuthService()

