import sqlalchemy as sa
from sqlalchemy.orm import relationship
from app import db
from app.models.basemodel import BaseModel
from app.models.follow import Follow
from app.models.list import List
from app.models.post import Post


class User(BaseModel, db.Model):
    username = sa.Column(sa.String(25), nullable=False, unique=True)
    fullname = sa.Column(sa.String(25), nullable=False)
    password = sa.Column(sa.String(60), nullable=False)
    email = sa.Column(sa.String(255), unique=True, nullable=False)
    bio = sa.Column(sa.Text)
    profile_picture = sa.Column(
        sa.String(255)
    )  # VARCHAR requires a length on dialect mysql
    posts = relationship("Post", backref="user")
    followers = relationship(
        "Follow", foreign_keys=[Follow.followed_id], back_populates="followed_user"
    )
    following = relationship(
        "Follow", foreign_keys=[Follow.follower_id], back_populates="follower_user"
    )
    fav_user_list = relationship(
        "List", foreign_keys=[List.owner_id], back_populates="list_owner"
    )

    def to_json(self):
        obj = super().to_json()
        if "password" in obj:
            del obj["password"]
        if "email" in obj:
            del obj["email"]
        return obj
