# -*- coding: utf-8 -*-
"""
    main.settings
    ~~~~~~~~~~~~~~~
    main settings module
"""
import os

class Config(object):
  DEBUG = False
  MAIL_DEFAULT_SENDER = 'raul.escamilla@asesoriait.com'
  SECRET_KEY = os.environ.get('SECRET_KEY')
  MAIL_SERVER = 'smtp.gmail.com'
  MAIL_PORT = 25
  MAIL_USE_TLS = True
  MAIL_USERNAME = 'raul.escamilla@asesoriait.com'
  MAIL_PASSWORD = ''

  SECURITY_POST_LOGIN_VIEW = '/'
  SECURITY_PASSWORD_HASH = 'plaintext'
  SECURITY_PASSWORD_SALT = 'password_salt'
  SECURITY_REMEMBER_SALT = 'remember_salt'
  SECURITY_RESET_SALT = 'reset_salt'
  SECURITY_RESET_WITHIN = '5 days'
  SECURITY_CONFIRM_WITHIN = '5 days'
  SECURITY_SEND_REGISTER_EMAIL = False


class ProductionConfig(Config):
  pass


class DevelopementConfig(Config):
  DEBUG = True    
  SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')

class TestingConfig(Config): 
  TESTING: True