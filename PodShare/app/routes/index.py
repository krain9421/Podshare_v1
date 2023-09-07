from flask import Blueprint, render_template

index_frontend_bp = Blueprint('index', __name__)

@index_frontend_bp.route('/')
def index():
    return render_template('index.html')
