"""Docstring for version two's parcel_views.py."""
from flask import make_response, jsonify
from flask_restful import Resource, reqparse
from ..models.parcel_models import ParcelOrder
from flask_jwt_extended import get_jwt_identity, jwt_required
from utils.validate_input import CheckUserInput


class ParcelOrderView(Resource, ParcelOrder):
    """docstring for ParcelOrderView."""

    @jwt_required
    def post(self):
        """Docstring for post method."""
        user_id = get_jwt_identity()
        parser = reqparse.RequestParser()
        parser.add_argument("item_shipped", type=str,
                            help="Item to ship is required", required=True)
        parser.add_argument("origin", type=str,
                            help="Origin is required", required=True)
        parser.add_argument("destination", type=str,
                            help="Destination is required", required=True)
        parser.add_argument("weight", type=int,
                            help="Weight is required", required=True)

        data = parser.parse_args()
        item_shipped = data["item_shipped"]
        if not CheckUserInput().check_if_input_is_string(item_shipped):
            return {"message": "Please enter a valid item to be shipped"}, 400
        origin = data["origin"]
        if not CheckUserInput().check_if_input_is_string(origin):
            return {"message": "Please enter a valid origin"}, 400
        destination = data["destination"]
        if not CheckUserInput().check_if_input_is_string(destination):
            return {"message": "Please enter a valid destination"}, 400
        weight = data["weight"]
        if not CheckUserInput().check_if_input_is_integer(weight):
            return {"message": "Please enter a valid weight"}, 400
        current_location = origin
        pickup_location = destination + " Branch Office"
        payload = ParcelOrder().create_parcel_delivery_order(
            u=user_id, i=item_shipped, o=origin, d=destination, w=weight,
            cl=current_location, pl=pickup_location)

        return make_response(jsonify(payload), 201)
