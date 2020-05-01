from flask import Flask
from flask_security import SQLAlchemyUserDatastore

from .core import db, mail, security
from .helpers import register_blueprints
from .middleware import HTTPMethodOverrideMiddleware
from .models import User, Role


def create_app(package_name, package_path, settings_override=None,
               register_security_blueprint=True):
    """Returns a :class:`Flask` application instance configured with common
    functionality for the tlinks platform.
    :param package_name: application package name
    :param package_path: application package path
    :param settings_override: a dictionary of settings to override
    :param register_security_blueprint: flag to specify if the Flask-Security
                                        Blueprint should be registered. Defaults
                                        to `True`.
    """
    app = Flask(package_name, instance_relative_config=True)

    if app.config['ENV'] == 'production':      
        app.config.from_object('tlinks.settings.ProductionConfig')

    elif app.config['ENV'] == 'testing':        
        app.config.from_object('tlinks.settings.TestingConfig')

    else:        
        app.config.from_object('tlinks.settings.DevelopementConfig')

    # app.config.from_pyfile('settings.cfg', silent=True)
    
    app.config.from_object(settings_override)

    db.init_app(app)
    mail.init_app(app)
    security.init_app(app, SQLAlchemyUserDatastore(db, User, Role),
                      register_blueprint=register_security_blueprint)

    register_blueprints(app, package_name, package_path)

    app.wsgi_app = HTTPMethodOverrideMiddleware(app.wsgi_app)

    return app
