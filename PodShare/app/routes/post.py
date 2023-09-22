from flask import Blueprint
from app.controllers.post import PostController

post_bp = Blueprint('post', __name__, url_prefix='/api/posts')

@post_bp.route('/', methods=['POST'], strict_slashes=False)
def upload():
    return PostController().upload()

@post_bp.route('/<post_id>')
def get_post(post_id):
    return PostController().get_post(post_id)

@post_bp.route('/')
def all_posts():
    return PostController().all_posts()