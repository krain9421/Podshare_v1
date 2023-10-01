from flask import Blueprint
from app.controllers.play import PlayController

play_bp = Blueprint("play", __name__, url_prefix="/api/play")


@play_bp.route("/audio/<post_id>", strict_slashes=False)
def stream(post_id):
    return PlayController().stream(post_id)
