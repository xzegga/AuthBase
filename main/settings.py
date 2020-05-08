# -*- coding: utf-8 -*-
"""
    main.settings
    ~~~~~~~~~~~~~~~
    main settings module
"""
from dotenv import load_dotenv
load_dotenv()

import os

class Config(object):
  DEBUG = False    
  MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER')
  SECRET_KEY = os.environ.get('SECRET_KEY')
  SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
  MAIL_SERVER = 'smtp.gmail.com'
  MAIL_PORT = 465
  MAIL_USE_TLS = False
  MAIL_USE_SSL = True
  MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
  MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
  FRONTED_URL = 'www.translationLinks.com'
  SECURITY_POST_LOGIN_VIEW = '/'
  SECURITY_PASSWORD_HASH = 'plaintext'
  SECURITY_PASSWORD_SALT = 'password_salt'
  SECURITY_REMEMBER_SALT = 'remember_salt'
  SECURITY_RESET_SALT = 'reset_salt'
  SECURITY_RESET_WITHIN = '5 days'
  SECURITY_CONFIRM_WITHIN = '5 days'
  SECURITY_SEND_REGISTER_EMAIL = False
  COMPANY_LOGO = 'http://translationlinks.com/img/logo.png'


class ProductionConfig(Config):
  pass


class DevelopementConfig(Config):
  DEBUG = True    

class TestingConfig(Config): 
  TESTING: True