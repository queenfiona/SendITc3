"""user_models.py."""
import datetime
from flask import Flask
from flask_restful import Api
from app.db_config import init_db
from flask_jwt_extended import create_access_token


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

    def user_signin(self, **kwargs):
        """Docstring for user login method."""
        username = kwargs["username"]
        password = kwargs["pwd"]
        user = self.get_user_by_name(username)

        if user != 404 and user[3] == username and user[6] == password:
            access_token = self.create_user_token(user)
            return {
                "message": "successful login",
                "access_token": access_token
            }

    def get_user_by_name(self, username):
        """Docstring for get user by name."""
        self.cur.execute(
            """SELECT * FROM users WHERE username = %s;""", (username,))
        user = self.cur.fetchone()
        return user

    def get_user_by_id(self, user_id):
        """Docstring for get user by id."""
        self.cur.execute(
            """SELECT * FROM users WHERE user_id = %s;""", (user_id,))
        user = self.cur.fetchone()
        return user

    def create_user_token(self, user):
        """Docstring for create access token method."""
        expires = datetime.timedelta(days=1)
        access_token = create_access_token(
            identity=user[0], expires_delta=expires)
        return access_token
