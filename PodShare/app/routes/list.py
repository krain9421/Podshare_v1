from flask import Blueprint, render_template, session
from app.controllers.user import UserAuthentication

list_frontend_bp = Blueprint("list", __name__)


@list_frontend_bp.route("/list", strict_slashes=False)
@UserAuthentication().login_required
def index():
    return render_template("list.html", user=session.get("user"))
