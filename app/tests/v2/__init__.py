"""Docstring for v2 __init__.py."""
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

    def tearDown(self):
        """Docstring for tearDown method."""
        destroy_tables()
