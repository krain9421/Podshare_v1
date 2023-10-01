from time import sleep
from flask import Blueprint, redirect, render_template, url_for, session, Response
from app.controllers.user import UserAuthentication, UserController

profile_frontend_bp = Blueprint("profile", __name__)


@profile_frontend_bp.route("/<username>", strict_slashes=False)
def index(username):
    if username == "me":
        if not UserAuthentication().is_logged_in():
            return redirect(url_for("auth_frontend.login"))
        username = session.get("user").get("username")
    user = UserController().find_user(username)
    return render_template("profile.html", title=username, user=user)


@profile_frontend_bp.route("/test")
def test():
    return render_template("test.html")


@profile_frontend_bp.route("/audio")
def audio():
    def generate():
        with open("audio/mine.mp3", "rb") as f:
            data = f.read(1024)
            while data:
                yield data
                data = f.read(1024)

    return Response(generate(), mimetype="audio/mp3")
