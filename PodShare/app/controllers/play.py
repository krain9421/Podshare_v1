from flask import Response, session
from app import db
from app.models.post import Post
from app.models.play import Play


class PlayController:
    def stream(self, audio_id):
        post = db.session.query(Post).filter_by(audio_id=audio_id).first()
        play = Play(user_id=session.get("user").get("id"), post_id=post.id)
        db.session.add(play)
        db.session.commit()

        def generate():
            with open(f"audio/{audio_id}.mp3", "rb") as f:
                data = f.read(1024)
                while data:
                    yield data
                    data = f.read(1024)

        return Response(generate(), mimetype="audio/mp3")
