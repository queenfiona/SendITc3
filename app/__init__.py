"""Docstring app's __init__.py."""
from flask import Flask
from .db_config import create_tables
from .api.v2 import version_2
from instance.config import app_config


def create_app(config):
    """Docstring for create_app method."""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config])
    app.register_blueprint(version_2)
    create_tables()
    return app
