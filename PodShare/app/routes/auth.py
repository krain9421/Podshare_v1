from flask import Blueprint, render_template, session, redirect, url_for
from app.controllers.user import UserAuthentication, UserController

auth_bp = Blueprint("auth", __name__)
auth_frontend_bp = Blueprint("auth_frontend", __name__)


@auth_bp.route("/login", methods=["POST"], strict_slashes=False)
def login():
    UserAuthentication().login()
    return redirect(url_for("home.index"))


@auth_bp.route("/register", methods=["POST"], strict_slashes=False)
def register():
    UserController().create_user()
    return redirect(url_for("auth_frontend.login"))


@auth_bp.route("/logout", strict_slashes=False)
def logout():
    return UserAuthentication().logout()


# frontend routes


@auth_frontend_bp.route("/register", strict_slashes=False)
def register():
    if session.get("user"):
        return redirect(url_for("home.index"))
    return render_template("register.html", title="Register")


@auth_frontend_bp.route("/login", strict_slashes=False)
def login():
    if session.get("user"):
        return redirect(url_for("home.index"))
    return render_template("login.html", title="Login")
