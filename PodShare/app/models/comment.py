import sqlalchemy as sa
from sqlalchemy.orm import relationship
from app import db
from app.models.basemodel import BaseModel
from app.models.like import Like
from app.models.play import Play


class Comment(BaseModel, db.Model):
    audio = sa.Column(sa.String, nullable=True)
    caption = sa.Column(sa.Text, nullable=False)
    user_id = sa.Column(sa.String(60), sa.ForeignKey('user.id'), nullable=False)
    post_id = sa.Column(sa.String(60), sa.ForeignKey('post.id'), nullable=False)
    likes = relationship('Like', backref='comment')
    plays = relationship('Play', backref='comment')
