"""Docstring for users test."""
# import unittest
import json
from . import BaseCase


class TestLoginCase(BaseCase):
    """docstring for TestCase."""

    def test_create_user(self):
        """Docstring for test_create_user method."""
        res = self.client.post(
            '/api/v2/auth/signup',
            data=json.dumps(self.signup_to_create_parcel_order),
            content_type='application/json')

        self.assertEqual(res.status_code, 201)

    def test_user_not_created(self):
        """Docstring for test_user_not_found method."""
        self.client.post(
            '/api/v2/auth/signup', data=json.dumps(self.signup_data),
            content_type='application/json')
        res2 = self.client.post(
            '/api/v2/auth/signup', data=json.dumps(self.signup_data),
            content_type='application/json')
        result = json.loads(res2.data)
        self.assertEqual(result["message"], "user already exists")
        self.assertEqual(res2.status_code, 409)

    def test_valid_username_input(self):
        """Docstring for test_valid_username method."""
        self.data = {
            "email": "fionaityang@gmail.com",
            "first_name": "Fiona",
            "last_name": "Murie",
            "password": "quifi",
            "username": ""
        }
        res = self.client.post(
            '/api/v2/auth/signup', data=json.dumps(self.data),
            content_type='application/json')
        result = json.loads(res.data)
        self.assertEqual(result['message'], "Please enter a valid username")
        self.assertEqual(res.status_code, 400)
