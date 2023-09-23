from functools import wraps
from flask import request, session, redirect, url_for
from app import bcrypt, db
from app.models.user import User
from app.utils.constants import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_401_UNAUTHORIZED,
    HTTP_409_CONFLICT,
)
from app.utils.errors import CustomError
from app.utils.response import generate_response


class UserAuthentication:
    def login(self):
        try:
            user = UserController().find_user_by_email()
            password = request.form.get("password")
            if not bcrypt.check_password_hash(user.password, password):
                raise Exception()
            session["user"] = user.to_json()
        except Exception:
            raise CustomError("email or password is incorrect", HTTP_401_UNAUTHORIZED)

    def logout(self):
        session["user"] = None
        return redirect(url_for("auth_frontend.login"))

    def login_required(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            user = session.get("user")
            if not user:
                raise CustomError("Not logged in", HTTP_401_UNAUTHORIZED)
            return func(*args, **kwargs)

        return wrapper

    def is_logged_in(self):
        return True if session.get("user") else False


class UserController:
    def create_user(self):
        user = None
        try:
            user = self.find_user()
        except CustomError:
            pass
        if user:
            raise CustomError("User already Exists", HTTP_409_CONFLICT)
        new_user = {
            "fullname": request.form.get("fullname"),
            "username": request.form.get("username"),
            "email": request.form.get("email"),
            "password": request.form.get("password"),
        }
        new_user["password"] = bcrypt.generate_password_hash(
            new_user["password"]
        ).decode()
        new_user = User(**new_user)
        db.session.add(new_user)
        db.session.commit()
        return True

    def find_user(self, username=None):
        username = username if username != None else request.form.get("username")
        user = db.session.query(User).filter_by(username=username).first()
        if not user:
            raise CustomError("User not found", 404)
        return user

    def find_user_by_email(self, email=None):
        email = email if email != None else request.form.get("email")
        user = db.session.query(User).filter_by(email=email).first()
        if not user:
            raise CustomError("User not found", 404)
        return user

    def user_info(self, username):
        if username == "me":
            username = session.get("user").get("username")
        user = self.find_user(username)
        response = user.to_json()
        response["posts"] = [post.to_json() for post in user.posts]
        response["following_count"] = len(user.following)
        response["follower_count"] = len(user.followers)
        return generate_response(response, "User Info")
