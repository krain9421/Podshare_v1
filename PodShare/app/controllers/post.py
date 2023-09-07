from app.models.post import Post
from app import db

class PostController:
    def feed(self):
        db.session.query(Post).order_by(Post.created_at).all()[:10]
