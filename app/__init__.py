"""Docstring app's __init__.py."""
from flask import Flask
from .db_config import create_tables, destroy_tables


def create_app():
    """Docstring for create_app method."""
    app = Flask(__name__)
    destroy_tables()
    create_tables()
    return app
