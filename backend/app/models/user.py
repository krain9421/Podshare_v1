import sqlalchemy as sa
from sqlalchemy.orm import relationship
from app import db
from app.models.basemodel import BaseModel
from app.models.follow import Follow
from app.models.list import List
from app.models.post import Post


class User(BaseModel, db.Model):
    username = sa.Column(sa.String(25), nullable=False, unique=True)
    password = sa.Column(sa.String(60), nullable=False)
    email = sa.Column(sa.String(255), unique=True, nullable=False)
    bio = sa.Column(sa.Text)
    profile_picture = sa.Column(sa.String)
    posts = relationship('Post', backref='user')
    followers = relationship('Follow', foreign_keys=[Follow.followed_id], back_populates='followed_user')
    following = relationship('Follow', foreign_keys=[Follow.follower_id], back_populates='follower_user')
    fav_user_list = relationship('List', foreign_keys=[List.owner_id], back_populates='list_owner')
