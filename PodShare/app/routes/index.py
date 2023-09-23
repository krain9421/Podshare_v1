from flask import Blueprint, redirect, url_for

index_frontend_bp = Blueprint("index", __name__)


@index_frontend_bp.route("/", strict_slashes=False)
def index():
    return redirect(url_for("auth_frontend.login"))
