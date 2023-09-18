from flask import Blueprint
from app.controllers.post import PostController

post_bp = Blueprint('post', __name__, url_prefix='/api/post')

@post_bp.route('/', methods=['POST'], strict_slashes=False)
def upload():
    return PostController().upload()