from flask import Blueprint
from app.controllers.user import UserAuthentication, UserController

auth_bp = Blueprint('auth', __name__, url_prefix='/api/auth')

@auth_bp.route('/login', methods=['POST'])
def login():
    return UserAuthentication().login()

@auth_bp.route('/register', methods=['POST'])
def register():
    return UserController().create_user()