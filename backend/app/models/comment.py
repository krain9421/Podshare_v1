from app.models.basemodel import BaseModel
from app import db
import sqlalchemy as sa
from sqlalchemy.orm import relationship


class Comment(BaseModel, db.Model):
    audio = sa.Column(sa.String, nullable=True)
    caption = sa.Column(sa.Text)
    user_id = sa.Column(sa.String(60), sa.ForeignKey('user.id'), nullable=False)
    likes = relationship('Like', backref='comment')
    plays = relationship('Play', backref='comment')
