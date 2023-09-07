from flask import Blueprint, redirect, render_template, url_for
from app.controllers.user import UserAuthentication

profile_frontend_bp = Blueprint('profile', __name__)

@profile_frontend_bp.route('/<username>')
def index(username):
    if username == 'me':
        if not UserAuthentication().is_logged_in():
            return redirect(url_for('auth_frontend.login'))
    return render_template('profile.html', title=username, username=username)