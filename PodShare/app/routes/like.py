from flask import Blueprint, request
from app.controllers.like import LikeController

like_bp = Blueprint("like", __name__, url_prefix="/api/like")


@like_bp.route("/<post_id>", methods=["POST"])
def like(post_id):
    post = True if request.json.get("post") else False
    return LikeController.like(post_id, post=post)
