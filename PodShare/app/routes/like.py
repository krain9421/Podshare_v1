from flask import Blueprint, request
from app.controllers.like import LikeController
from app.controllers.user import UserAuthentication

like_bp = Blueprint("like", __name__, url_prefix="/api/like")


@like_bp.route("/posts/<post_id>", methods=["POST"])
@UserAuthentication().login_required
def like(post_id):
    """
    requests to this endpoint should have a JSON body attached
    field:
        - post: to specify whether it is a post or a comment
    """
    print(request.json)
    post = True if request.json.get("post") else False
    print(post_id, "liked")
    return LikeController.like(post_id, post=post)
