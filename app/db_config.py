"""Docstring for db_config file."""
import psycopg2
import os
from instance.config import app_config
# from boto.s3.connection import S3Connection

# s3 = S3Connection(os.environ['S3_KEY'], os.environ['S3_SECRET'])


env = os.getenv("FLASK_ENV")
if not env:
    url = app_config["production"].DATABASE_URL
else:
    url = os.environ['DATABASE_URL']


def connection(url):
    """Docstring for connection method."""
    connection_to_db = psycopg2.connect(url, sslmode='require')
    return connection_to_db


def init_db():
    """Docstring for init_db method."""
    connection_to_db = psycopg2.connect(url)
    return connection_to_db


def tables():
    """Docstring for tables method."""
    users = """CREATE TABLE IF NOT EXISTS users(
    user_id  SERIAL PRIMARY KEY,
    first_name CHARACTER VARYING(200) NOT NULL,
    last_name CHARACTER VARYING(200) NOT NULL,
    username CHARACTER VARYING(200) NOT NULL,
    role CHARACTER VARYING(200) DEFAULT 'user',
    email CHARACTER VARYING(320) NOT NULL,
    password CHARACTER VARYING(200) NOT NULL);"""

    orders = """CREATE TABLE IF NOT EXISTS orders(
    parcel_id  SERIAL PRIMARY KEY,
    user_id SERIAL REFERENCES users(user_id),
    item_shipped CHARACTER VARYING(200) NOT NULL,
    origin CHARACTER VARYING(200) NOT NULL,
    destination CHARACTER VARYING(200) NOT NULL,
    weight INTEGER NOT NULL,
    current_location CHARACTER VARYING(200) NOT NULL,
    pickup_location CHARACTER VARYING(200) NOT NULL,
    status CHARACTER VARYING(200) NOT NULL);"""

    query = [users, orders]
    return query


def create_tables():
    """Docstring for create_tables method."""
    tables_to_create = tables()
    connection_to_db = connection(url)
    cursor = connection_to_db.cursor()
    for table in tables_to_create:
        cursor.execute(table)
    connection_to_db.commit()


def destroy_tables():
    """Docstring for destroy tables method."""
    connection_to_db = connection(url)
    cursor = connection_to_db.cursor()
    drop_orders = """DROP TABLE IF EXISTS orders CASCADE"""
    drop_users = """DROP TABLE IF EXISTS users CASCADE"""
    queries = [drop_users, drop_orders]
    for table_to_drop in queries:
        cursor.execute(table_to_drop)
    connection_to_db.commit()
