import sqlalchemy as sa
from sqlalchemy.orm import relationship
from app import db
from app.models.basemodel import BaseModel


class List(BaseModel, db.Model):
    owner_id = sa.Column(sa.String(60), sa.ForeignKey("user.id"), nullable=False)
    user_id = sa.Column(sa.String(60), sa.ForeignKey("user.id"), nullable=False)

    list_owner = relationship(
        "User", foreign_keys=[owner_id], back_populates="fav_user_list"
    )
