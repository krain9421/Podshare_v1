from flask import Blueprint
from app.controllers.user import UserController
from app.utils.response import generate_response


user_bp = Blueprint('user', __name__, url_prefix='/api/users')

@user_bp.route('/<username>')
def get_user(username):
    return UserController().user_info(username)
