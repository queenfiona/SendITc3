"""For user_models.py."""
from flask import make_response, jsonify
from flask_restful import Resource, reqparse
from ..models.user_models import UserModel
from utils.validate_input import CheckUserInput


class UserRegistration(Resource, UserModel):
    """User registration class."""

    def post(self):
        """Registration post method."""
        parser = reqparse.RequestParser()
        parser.add_argument('first_name', type=str,
                            help="First name is missing", required=True)
        parser.add_argument('last_name', type=str,
                            help="Last name is missing", required=True)
        parser.add_argument('username', type=str,
                            help="Username is missing", required=True)
        parser.add_argument("email", type=str,
                            help="Email is missing", required=True)
        parser.add_argument("password", type=str,
                            help="Password is missing", required=True)
        user_data = parser.parse_args()
        first_name = user_data['first_name']
        if not CheckUserInput().check_if_input_is_string(first_name):
            return {"message": "Please enter a valid first name"}, 400
        last_name = user_data['last_name']
        if not CheckUserInput().check_if_input_is_string(last_name):
            return {"message": "Please enter a valid first name"}, 400
        username = user_data['username']
        if not CheckUserInput().check_if_input_is_string(username):
            return {"message": "Please enter a valid username"}, 400
        email = user_data['email']
        if not CheckUserInput().check_if_input_is_string(username):
            return {"message": "Please enter a valid email"}, 400

        password = user_data['password']
        if not CheckUserInput().check_if_input_is_string(password):
            return {"message": "Please enter a valid password"}

        payload = UserModel().user_signup(fn=first_name, ln=last_name,
                                          un=username, e=email, pwd=password)
        if payload == 409:
            return make_response(jsonify({
                "message": "user already exists"}), 409)

        return make_response(jsonify(payload), 201)


class UserLogin(Resource, UserModel):
    """User login class."""

    def post(self):
        """Login post method."""
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str,
                            help="Username is missing", required=True)
        parser.add_argument("password", type=str,
                            help="Password is missing", required=True)
        user_data = parser.parse_args()
        username = user_data['username']
        if not CheckUserInput().check_if_input_is_string(username):
            return {"message": "Please enter a valid username"}, 400
        password = user_data['password']
        if not CheckUserInput().check_if_input_is_string(password):
            return {"message": "Please enter a valid password"}, 400
        payload = UserModel().user_signin(username=username, pwd=password)
        return make_response(jsonify(payload), 200)
