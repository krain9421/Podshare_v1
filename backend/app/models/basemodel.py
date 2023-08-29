import datetime
import uuid
import sqlalchemy as sa


class BaseModel:
    id = sa.Column(sa.String(60), primary_key=True, default=lambda: str(uuid.uuid4()), unique=True, nullable=False)
    created_at = sa.Column(sa.DateTime, default=datetime.datetime.now)
