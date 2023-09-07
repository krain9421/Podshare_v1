from flask import Blueprint, render_template

home_frontend_bp = Blueprint('home', __name__)

@home_frontend_bp.route('/home')
def index():
    return render_template('home.html', title="Home")