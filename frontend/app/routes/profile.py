from flask import Blueprint, render_template

profile_bp = Blueprint('profile', __name__)

@profile_bp.route('/<username>')
def index(username):
    return render_template('profile.html', title=username, username=username)