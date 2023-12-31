from flask import Blueprint, render_template, session
from app.controllers.post import PostController

home_frontend_bp = Blueprint("home", __name__)


@home_frontend_bp.route("/home", strict_slashes=False)
def index():
    return render_template(
        "home.html",
        title="Home",
        user=session.get("user"),
        feed=PostController().feed(),
    )
