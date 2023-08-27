from app.models.basemodel import BaseModel
from app import db
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class Post(BaseModel, db.Model):
    audio = sa.Column(sa.String)
    caption = sa.Column(sa.Text)
    user_id = sa.Column(sa.String(60), sa.ForeignKey('user.id'), nullable=False)
    likes = relationship('Like', backref='post')
    plays = relationship('Play', backref='post')
