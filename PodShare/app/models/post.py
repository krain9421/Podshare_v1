import sqlalchemy as sa
from sqlalchemy.orm import relationship
from app import db
from app.models.basemodel import BaseModel
from app.models.comment import Comment
from app.models.like import Like
from app.models.play import Play


class Post(BaseModel, db.Model):
    audio = sa.Column(sa.String(60), nullable=False) #VARCHAR requires a length on dialect mysql
    caption = sa.Column(sa.Text, nullable=False)
    user_id = sa.Column(sa.String(60), sa.ForeignKey('user.id'), nullable=False)
    likes = relationship('Like', backref='post')
    plays = relationship('Play', backref='post')
    comments = relationship('Comment', backref='post')
