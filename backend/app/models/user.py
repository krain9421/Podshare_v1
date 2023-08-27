import sqlalchemy as sa
from app import db
from app.models.basemodel import BaseModel

class User(BaseModel, db.Model):
    username = sa.Column(sa.String(25), nullable=False, unique=True)
    password = sa.Column(sa.String(60), nullable=False)
    email = sa.Column(sa.string(255), unique=True)
    bio = sa.Column(sa.Text)
    profile_picture = sa.Column(sa.String)
    followers = sa.Column(sa.Double, default=0)
    following = sa.Column(sa.Double, default=0)
