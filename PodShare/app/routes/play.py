from flask import Blueprint
from app.controllers.play import PlayController

play_bp = Blueprint('play', __name__, url_prefix='/api/play')

@play_bp.route('/<audio_id>')
def stream(audio_id):
    return PlayController().stream(audio_id)
