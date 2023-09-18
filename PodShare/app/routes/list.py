from flask import Blueprint, render_template

list_frontend_bp = Blueprint('list', __name__)

@list_frontend_bp.route('/list', strict_slashes=False)
def index():
    return render_template('list.html')
