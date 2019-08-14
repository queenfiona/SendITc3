"""Docstring for v2 __init__.py."""
import json
import unittest
from app import create_app
from app.db_config import destroy_tables


class BaseCase(unittest.TestCase):
    """docstring for TestCase."""

    def setUp(self):
        """Docstring for setUp method."""
        self.app = create_app('testing')
        self.client = self.app.test_client()
        self.signup_to_create_parcel_order = {
            "email": "tom@gmail.com",
            "first_name": "Tom",
            "last_name": "Tom",
            "password": "tom",
            "username": "tom"
        }

        self.signup_data = {
            "email": "fionaityang@gmail.com",
            "first_name": "Fiona",
            "last_name": "Murie",
            "password": "quifi",
            "username": "quifi"
        }
        self.signup_admin = {
            "email": "fionaityang@gmail.com",
            "first_name": "Mary",
            "last_name": "Doe",
            "password": "mary",
            "username": "mary",
            "role": "admin"
        }
        self.login_data = {
            "username": "quifi",
            "password": "quifi"
        }
        self.login_admin = {
            "username": "mary",
            "password": "mary"
        }
        self.parcel_data = {
            "item_shipped": "Books",
            "origin": "Nairobi",
            "destination": "Kisumu",
            "current_location": "Nairobi",
            "pickup_location": "Kisumu",
            "weight": 12
        }
        self.specific_data = {
            "item_shipped": "Books",
            "origin": "Nairobi",
            "destination": "Kisumu",
            "current_location": "Nairobi",
            "pickup_location": "Kisumu",
            "weight": 12
        }
        self.client.post(
            '/api/v2/auth/signup', data=json.dumps(self.signup_data),
            content_type='application/json')
        res = self.client.post(
            '/api/v2/auth/login', data=json.dumps(self.login_data),
            content_type='application/json')
        data = json.loads(res.get_data(as_text=True))
        self.token = data["access_token"]
        self.user_headers = {
            'AUTHORIZATION': 'Bearer ' + self.token
        }
        self.client.post(
            '/api/v2/auth/signup', data=json.dumps(self.signup_admin),
            content_type='application/json')
        res = self.client.post(
            '/api/v2/auth/login', data=json.dumps(self.login_admin),
            content_type='application/json')
        data = json.loads(res.get_data(as_text=True))
        self.token = data["access_token"]
        self.admin_headers = {
            'AUTHORIZATION': 'Bearer ' + self.token
        }

    def tearDown(self):
        """Docstring for tearDown method."""
        destroy_tables()
