"""Docstring for v2's  __init__.py."""
from flask import Blueprint
from flask_restful import Api
from .views.user_views import UserRegistration, UserLogin
from .views.parcel_views import (
    ParcelOrderView, UserOrderView, AllOrdersView, StatusView, DestinationView)

version_2 = Blueprint('apiv2', __name__)

api = Api(version_2, prefix="/api/v2")
api.add_resource(UserRegistration, "/auth/signup")
api.add_resource(UserLogin, "/auth/login")
api.add_resource(ParcelOrderView, "/parcels")
api.add_resource(UserOrderView, "/parcels/<string:username>")
api.add_resource(AllOrdersView, "/parcels")
api.add_resource(StatusView, "/parcels/<int:parcel_id>/status")
api.add_resource(DestinationView, "/parcels/<int:parcel_id>/destination")
