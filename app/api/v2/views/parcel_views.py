"""Docstring for version two's parcel_views.py."""
from flask import make_response, jsonify
from flask_restful import Resource, reqparse
from ..models.parcel_models import ParcelOrder
from ..models.user_models import UserModel
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
        payload = ParcelOrder().create_parcel_delivery_order(
            u=user_id, i=item_shipped, o=origin, d=destination, w=weight
        )

        return make_response(jsonify(payload), 201)


class UserOrderView(Resource, ParcelOrder):
    """docstring for UserOrderView."""

    @jwt_required
    def get(self, username):
        """Docstring for get method."""
        user_id = get_jwt_identity()
        user = UserModel().get_user_by_id(user_id)
        if user and username == user[3]:
            parcel_delivery_orders = ParcelOrder(
            ).get_specific_user_orders(user[0])
            payload = {
                "message": "success",
                "parcel orders": parcel_delivery_orders
            }
            return make_response(jsonify(payload), 200)
        else:
            return make_response(jsonify({
                "message": "You do not have access to these parcel orders"}),
                403)


class AllOrdersView(Resource, ParcelOrder):
    """docstring for AllOrdersView."""

    @jwt_required
    def get(self):
        """Docstring for get method."""
        user_id = get_jwt_identity()
        user = UserModel().get_user_by_id(user_id)
        if user[4] == "admin":
            all_parcels = ParcelOrder().get_all_orders()
            payload = {
                "message": "All parcel orders",
                "parcel orders": all_parcels
            }
            return make_response(jsonify(payload), 200)
        else:
            parcel = ParcelOrder().get_parcel_by_id(user_id)
            return {
                "message": "success",
                "parcel_order": parcel}, 200


class StatusView(Resource, ParcelOrder):
    """docstring for StatusView."""

    @jwt_required
    def put(self, parcel_id):
        """Docstring for put method."""
        user_id = get_jwt_identity()
        user = UserModel().get_user_by_id(user_id)
        parcel = ParcelOrder().get_parcel_by_id(parcel_id)
        if user and parcel:
            if user[4] == "admin":
                status = ParcelOrder().change_status(parcel_id)
                return make_response(jsonify(status), 200)

            else:
                return make_response(jsonify({
                    "message": "You have no access rights to change the status of parcel order"}), 403)

        else:
            return {"message": "user or parcel does not exist"}, 404


class DestinationView(Resource, ParcelOrder):
    """docstring for DestinationView."""

    @jwt_required
    def put(self, parcel_id):
        """Docstring for put method."""
        user_id = get_jwt_identity()
        user = UserModel().get_user_by_id(user_id)
        parcel = ParcelOrder().get_parcel_by_id(parcel_id)

        if user and parcel:
            if user_id == parcel[1]:
                if parcel[8] == "not_delivered":
                    new = ParcelOrder().change_destination(parcel_id)
                    return make_response(jsonify(new), 200)
                else:
                    return {
                        "message": "Destination cannot be changed since parcel is in transit"}, 400
            else:
                return {
                    "message": "You have no access rights to change parcel order"}, 403

        else:
            return {"message": "user or parcel does not exist"}, 404


class PresentLocView(Resource, ParcelOrder):
    """docstring for PresentLocView."""

    @jwt_required
    def put(self, parcel_id):
        """Docstring for put method."""
        user_id = get_jwt_identity()
        user = UserModel().get_user_by_id(user_id)
        parcel = ParcelOrder().get_parcel_by_id(parcel_id)
        if user and parcel:
            if user[4] == "admin":
                location = ParcelOrder().change_current_location(parcel_id)
                return make_response(jsonify(location), 200)

            else:
                return {
                    "message": "You have no access rights to change the location of parcel order"}, 403

        else:
            return {"message": "user or parcel does not exist"}, 404


class CancelOrderView(Resource, ParcelOrder):
    """docstring for DestinationView."""

    @jwt_required
    def put(self, parcel_id):
        """Docstring for put method."""
        user_id = get_jwt_identity()
        user = UserModel().get_user_by_id(user_id)
        parcel = ParcelOrder().get_parcel_by_id(parcel_id)

        if user and parcel:
            if user_id == parcel[1]:
                if parcel[8] == "not_delivered":
                    new = ParcelOrder().cancel_order(parcel_id)
                    return make_response(jsonify(new), 200)
                else:
                    return {
                        "message": "Order could not be cancelled since it is in transit"}, 400
            else:
                return {
                    "message": "You have no access rights to change parcel order"}, 403

        else:
            return {"message": "user or parcel does not exist"}, 404
