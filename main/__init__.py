# -*- coding: utf-8 -*-
"""
    main
    ~~~~~~~~
    main1.0 application package
"""
from flask import jsonify

from .core import AppError, AppFormError
from .helpers import JSONEncoder
from . import factory

def create_app(settings_override=None, register_security_blueprint=False):
    """Returns the main API application instance"""

    api = factory.create_app(__name__, __path__, settings_override,
                             register_security_blueprint=register_security_blueprint)

    # Set the default JSON encoder
    api.json_encoder = JSONEncoder

    # Register custom error handlers
    api.errorhandler(AppError)(on_app_error)
    api.errorhandler(AppFormError)(on_app_form_error)
    api.errorhandler(404)(on_404)

    return api


def on_app_error(e):
    return jsonify(dict(error=e.msg)), 400


def on_app_form_error(e):
    return jsonify(dict(errors=e.errors)), 400


def on_404(e):
    return jsonify(dict(error='Not found')), 404
