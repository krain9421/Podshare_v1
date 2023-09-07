from flask import Blueprint, render_template

profile_frontend_bp = Blueprint('profile', __name__)

@profile_frontend_bp.route('/<username>')
def index(username):
    return render_template('profile.html', title=username, username=username)