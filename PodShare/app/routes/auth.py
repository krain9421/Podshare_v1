from flask import Blueprint, render_template
from app.controllers.user import UserAuthentication, UserController

auth_bp = Blueprint('auth', __name__, url_prefix='/api/auth')
auth_frontend_bp = Blueprint('auth_frontend', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    return UserAuthentication().login()

@auth_bp.route('/register', methods=['POST'])
def register():
    return UserController().create_user()

# frontend routes

@auth_frontend_bp.route('/register')
def register():
    return render_template('register.html', title="Register")

@auth_frontend_bp.route('/login')
def login():
    return render_template('login.html', title="Login")
