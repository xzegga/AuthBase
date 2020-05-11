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
  SECRET_KEY = os.environ.get('SECRET_KEY')
  JWT_ACCESS_LIFESPAN = {'hours': 24}
  JWT_REFRESH_LIFESPAN = {'minutes': 120}

  PRAETORIAN_RESET_SENDER = os.environ.get('MAIL_USERNAME')
  PRAETORIAN_CONFIRMATION_SENDER = os.environ.get('MAIL_USERNAME')
  PRAETORIAN_RESET_URI = 'https://www.translationLinks.com/reset-password'
  PRAETORIAN_RESET_SUBJECT = "Reset password request for InterpTlinks"

  SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
  
  MAIL_SERVER = 'smtp.gmail.com'
  MAIL_PORT = 587
  MAIL_USE_TLS = True
  MAIL_USE_SSL = False
  MAIL_DEFAULT_SENDER = (os.environ.get('MAIL_DEFAULT_NAME'), os.environ.get('MAIL_DEFAULT_SENDER'))
  MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
  MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
  
  SECURITY_POST_LOGIN_VIEW = '/'
  SECURITY_PASSWORD_HASH = 'plaintext'
  SECURITY_PASSWORD_SALT = 'password_salt'
  SECURITY_REMEMBER_SALT = 'remember_salt'
  SECURITY_RESET_SALT = 'reset_salt'
  SECURITY_RESET_WITHIN = '5 days'
  SECURITY_CONFIRM_WITHIN = '5 days'
  SECURITY_SEND_REGISTER_EMAIL = False
  
  FRONTED_URL = 'www.translationLinks.com'
  COMPANY_LOGO = 'http://translationlinks.com/img/logo.png'


class ProductionConfig(Config):
  pass


class DevelopementConfig(Config):
  PYTHONPROFILEIMPORTTIME = 1
  DEBUG = True    

class TestingConfig(Config): 
  TESTING: True


config = {
  'production': ProductionConfig,
	'development': DevelopementConfig,
	'default': DevelopementConfig
}