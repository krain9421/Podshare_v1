from os import getenv
from dotenv import load_dotenv
from flask import render_template
from app.utils.errors import CustomError
from app.utils.constants import (
    HTTP_401_UNAUTHORIZED,
    HTTP_409_CONFLICT,
    HTTP_500_INTERNAL_SERVER_ERROR,
    HTTP_404_NOT_FOUND,
)

load_dotenv()


def config_app(app):
    # config app
    app.config["SECRET_KEY"] = getenv("SECRET_KEY", "secret_key:D")
    app.config["SQLALCHEMY_DATABASE_URI"] = getenv("SQLALCHEMY_DATABASE_URI")
    app.config["SESSION_PERMANENT"] = False
    app.config["SESSION_TYPE"] = "filesystem"

    # add error handlers
    @app.errorhandler(CustomError)
    def handle_authentication_error(error):
        if error.status_code == HTTP_409_CONFLICT:
            return (
                render_template("register.html", message=error.message),
                HTTP_409_CONFLICT,
            )
        if error.status_code == HTTP_404_NOT_FOUND:
            return (
                render_template("404.html", message=error.message),
                HTTP_404_NOT_FOUND,
            )
        if error.status_code == HTTP_401_UNAUTHORIZED:
            return (
                render_template("login.html", message=error.message),
                HTTP_401_UNAUTHORIZED,
            )
        return render_template("50x.html", message=error.message), error.status_code

    @app.errorhandler(404)
    def handle_not_found_error(error):
        return render_template("404.html"), HTTP_404_NOT_FOUND

    @app.errorhandler(Exception)
    def handle_generic_error(error):
        print(error)
        return render_template("50x.html"), HTTP_500_INTERNAL_SERVER_ERROR
