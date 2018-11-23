"""Docstring for version 2 parcel_models.py."""
from flask import Flask
from flask_restful import Api
from app.db_config import init_db

app = Flask(__name__)
api = Api(app)


class ParcelOrder(object):
    """Docstring for ParcelOrder."""

    def __init__(self):
        """Docstring for __init__."""
        self.database = init_db()

    def create_parcel_delivery_order(self, **kwargs):
        """Docstring for create_parcel_delivery_order."""
        payload = {
            "user_id": kwargs["u"],
            "item_shipped": kwargs['i'],
            "origin": kwargs['o'],
            "destination": kwargs['d'],
            "weight": int(kwargs['w']),
            "current_location": kwargs['cl'],
            "pickup_location": kwargs['pl'],
            "status": "not_delivered"
        }
        query = """
            INSERT INTO orders(user_id,item_shipped,origin,destination,weight
            ,current_location,pickup_location,status)
            VALUES(%(user_id)s,%(item_shipped)s,%(origin)s,%(destination)s,%(weight)s,
            %(current_location)s,%(pickup_location)s,%(status)s)
        """
        cur = self.database.cursor()
        cur.execute(query, payload)
        self.database.commit()
        return payload
