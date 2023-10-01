from flask import Response, session
from app import db
from app.models.post import Post
from app.models.play import Play


class PlayController:
    def stream(self, post_id):
        post = db.session.query(Post).filter_by(id=post_id).first()
        user_id = session.get("user").get("id") if session.get("user") else None
        play = Play(user_id=user_id, post_id=post.id)
        db.session.add(play)
        db.session.commit()

        def generate():
            with open(post.audio[0].url, "rb") as f:
                data = f.read(1024)
                while data:
                    yield data
                    data = f.read(1024)

        return Response(generate(), mimetype=post.audio[0].mime)
