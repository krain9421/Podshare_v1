import sqlalchemy as sa
from sqlalchemy.orm import relationship
from app import db
from app.models.basemodel import BaseModel


class Follow(BaseModel, db.Model):
    follower_id = sa.Column(sa.String(60), sa.ForeignKey('user.id'), nullable=False)
    followed_id = sa.Column(sa.String(60), sa.ForeignKey('user.id'), nullable=False)
    follower_user = relationship('User', foreign_keys=[follower_id], back_populates='followers')
    followed_user = relationship('User', foreign_keys=[followed_id], back_populates='following')
