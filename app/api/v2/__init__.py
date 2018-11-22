"""Docstring for v2's  __init__.py."""
from flask import Blueprint
from flask_restful import Api
from .views.parcel_views import (
    ParcelOrderView, UserOrderView, AllOrdersView, DestinationView, StatusView,
    PresentLocView)
from .views.user_views import UserRegistration


version_2 = Blueprint('apiv2', __name__)

api = Api(version_2, prefix="/api/v2")
api.add_resource(ParcelOrderView, "/parcels", strict_slashes=False)
api.add_resource(UserOrderView, "/parcels/<string:username>",
                 strict_slashes=False)
api.add_resource(AllOrdersView, "/parcels")
api.add_resource(DestinationView, "/parcels/<int:parcel_id>/destination")
api.add_resource(StatusView, "/parcels/<int:parcel_id>/status")
api.add_resource(PresentLocView,
                 "/parcels/<int:parcel_id>/presentLocation")
api.add_resource(UserRegistration, "/auth/signup")
