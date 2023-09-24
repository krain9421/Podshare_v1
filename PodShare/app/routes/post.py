from flask import Blueprint, render_template
from app.controllers.post import PostController
from app.controllers.user import UserAuthentication

post_bp = Blueprint("post", __name__, url_prefix="/api/posts")
post_frontend_bp = Blueprint("post_frontend", __name__)


@post_bp.route("/", methods=["POST"], strict_slashes=False)
@UserAuthentication().login_required
def upload():
    return PostController().upload()


@post_bp.route("/<post_id>", strict_slashes=False)
def get_post(post_id):
    return PostController().get_post(post_id)


@post_bp.route("/", strict_slashes=False)
def all_posts():
    return PostController().all_posts()


@post_frontend_bp.route("/posts/<post_id>", strict_slashes=False)
def post_page(post_id):
    post = PostController.get_post_details(post_id)
    return render_template("post.html", post=post)
