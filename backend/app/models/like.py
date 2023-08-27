from app.models.basemodel import BaseModel
from app import db
import sqlalchemy as sa


class Like(BaseModel, db.Model):
    user_id = sa.Column(sa.String(60), sa.ForeignKey('user.id'), nullable=False)
    post_id = sa.Column(sa.String(60), sa.ForeignKey('post.id'))
    comment_id = sa.Column(sa.String(60), sa.ForeignKey('comment.id'))
