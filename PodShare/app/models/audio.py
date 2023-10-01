import sqlalchemy as sa
from app import db
from app.models.basemodel import BaseModel


class Audio(BaseModel, db.Model):
    url = sa.Column(sa.String(60), nullable=False)
    mime = sa.Column(sa.String(20), nullable=False)
    post_id = sa.Column(sa.String(60), sa.ForeignKey("post.id"), nullable=False)
