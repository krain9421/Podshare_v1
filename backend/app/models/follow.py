from app.models.basemodel import BaseModel
from app import db
import sqlalchemy as sa


class Follow(BaseModel, db.Model):
    follower_id = sa.Column(sa.String(60), sa.ForeignKey('user.id'), nullable=False)
    followed_id = sa.Column(sa.String(60), sa.ForeignKey('user.id'), nullable=False)
