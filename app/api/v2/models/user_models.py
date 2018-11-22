"""user_models.py."""
from flask import Flask
from flask_restful import Api
from app.db_config import init_db


app = Flask(__name__)
api = Api(app)


class UserModel:
    """Usermodel class."""

    def __init__(self):
        """Init method."""
        self.connection = init_db()
        self.cur = self.connection.cursor()

    def user_signup(self, **kwargs):
        """User registration method."""
        payload = {
            "first_name": kwargs["fn"],
            "last_name": kwargs["ln"],
            "username": kwargs["un"],
            "email": kwargs["e"],
            "password": kwargs["pwd"]
        }
        query = """INSERT INTO users (first_name, last_name, username, email, password)
         VALUES (%(first_name)s,%(last_name)s,%(username)s,%(email)s,
         %(password)s);"""

        username = payload["username"]
        email = payload["email"]
        user = self.get_user_by_name(username)
        if user:
            if user[3] == username:
                return 409
            elif user[5] == email:
                return 409

            else:
                self.cur.execute(query, payload)
                self.connection.commit()
                return payload
        else:
            self.cur.execute(query, payload)
            self.connection.commit()
            return payload

    def get_user_by_name(self, username):
        """Get user by name."""
        self.cur.execute(
            """SELECT * FROM users WHERE username = %s;""", (username,))
        user = self.cur.fetchone()
        return user

    def get_user_by_id(self, user_id):
        """Get user by id."""
        self.cur.execute(
            """SELECT * FROM users WHERE user_id = %s;""", (user_id,))
        user = self.cur.fetchone()
        return user
