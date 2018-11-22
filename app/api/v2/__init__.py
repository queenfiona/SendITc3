"""Docstring for v2's  __init__.py."""
from flask import Blueprint
from flask_restful import Api
from .views.user_views import UserRegistration


version_2 = Blueprint('apiv2', __name__)

api = Api(version_2, prefix="/api/v2")
api.add_resource(UserRegistration, "/auth/signup")
