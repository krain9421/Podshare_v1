from flask import Blueprint, render_template

list_bp = Blueprint('list', __name__)

@list_bp.route('/list')
def index():
    return render_template('list.html')