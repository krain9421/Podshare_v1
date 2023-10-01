import uuid
from flask import session, request, abort
from sqlalchemy import desc
from app import db
from app.models.audio import Audio
from app.models.post import Post
from app.models.like import Like
from app.models.play import Play
from app.models.comment import Comment
from app.utils.response import generate_response
from app.utils.constants import HTTP_201_CREATED, HTTP_200_OK


class PostController:
    def all_posts(self):
        posts = db.session.query(Post).all()
        return generate_response(
            data=[post.to_json() for post in posts], message="Posts"
        )

    def feed(self):
        posts = db.session.query(Post).order_by(desc(Post.created_at)).limit(10)
        # prevent repeated feed data -- to be implemented later
        if not session.get("viewed_posts"):
            session["viewed_posts"] = []
        for post in posts:
            session.get("viewed_posts").append(post.id)
        return posts

    def upload(self):
        form_audio = request.files.get("audio")
        form_caption = request.form.get("caption")
        audio_path = f'audio/{str(uuid.uuid4())}.{form_audio.filename.split(".")[1]}'
        post = Post(caption=form_caption, user_id=session.get("user").get("id"))
        db.session.add(post)
        db.session.commit()

        # get mimetype
        mime = ""
        if audio_path.split(".")[-1] == "mp3":
            mime = "audio/mp3"
        audio = Audio(url=audio_path, mime=mime, post_id=post.id)
        form_audio.save(audio_path)
        db.session.add(audio)
        db.session.commit()
        return generate_response(
            data=post.to_json(), message="Post Uploaded", status_code=HTTP_201_CREATED
        )

    def get_post(self, post_id):
        post = db.session.query(Post).filter_by(id=post_id).first()
        if not post:
            abort(404)
        like_count = db.session.query(Like).filter_by(post_id=post.id).count()
        play_count = db.session.query(Play).filter_by(post_id=post.id).count()
        comment_count = db.session.query(Comment).filter_by(post_id=post.id).count()
        post = post.to_json()
        post.update(
            {
                "like_count": like_count,
                "play_count": play_count,
                "comment_count": comment_count,
            }
        )
        return generate_response(data=post, message="Post")

    def get_post_details(self, post_id):
        post = self.get_post(post_id)[0]["data"]
        comments = db.session.query(Comment).filter_by(post_id=post["id"]).all()
        comments = [comment.to_json() for comment in comments]
        post["comments"] = comments
        return generate_response(data=post, message="post details")
