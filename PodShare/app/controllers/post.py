import uuid
from flask import session, request, abort
from app import db
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
        posts = db.session.query(Post).order_by(Post.created_at).all()[:10]
        posts = [post.to_json() for post in posts]
        return generate_response(data=posts, message="User feed")

    def upload(self):
        audio = request.files.get("audio")
        caption = request.form.get("caption")
        audio_path = f'audio/{str(uuid.uuid4())}.{audio.filename.split(".")[1]}'
        post = Post(
            audio=audio_path, caption=caption, user_id=session.get("user").get("id")
        )
        audio.save(audio_path)
        db.session.add(post)
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
        post = self.get_post(post_id)[0]
        comments = post
