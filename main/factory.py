from flask import Flask
from .core import db, mail, guard, cors, bl
from .helpers import register_blueprints
from .middleware import HTTPMethodOverrideMiddleware
from .models import User, Token
from flask_blacklist import is_blacklisted
import os
from .settings import DevelopementConfig, ProductionConfig, TestingConfig


def create_app(package_name, package_path, settings_override=None,
               register_security_blueprint=True):
    """
    Returns a :class:`Flask` application instance configured with common
    functionality for the main platform.
    :param package_name: application package name
    :param package_path: application package path
    :param settings_override: a dictionary of settings to override
    :param register_security_blueprint: flag to specify if the Flask-Security
                                        Blueprint should be registered. Defaults
                                        to `True`.
    """
    app = Flask(package_name, instance_relative_config=True)
   
    # Set app variables based in the environment
    app.config.from_object('main.settings.DevelopementConfig')

    # Override setting with settings_override values
    # app.config.from_object(settings_override)
    
    with app.app_context():
      # Initialize a local database for the example
      db.init_app(app)

      # Initializes CORS so that the api_tool can talk to the example app
      cors.init_app(app)

      # Initializes Mail instance
      mail.init_app(app)

      bl.init_app(app, Token)

      # Initialize the flask-praetorian instance for the app
      guard.init_app(app, User, is_blacklisted = is_blacklisted)

      # Registre all blueprints in the package_name
      register_blueprints(app, package_name, package_path)


      # Apply middleware to support every HTTP method in old browsers
      app.wsgi_app = HTTPMethodOverrideMiddleware(app.wsgi_app)
      
      return app  
