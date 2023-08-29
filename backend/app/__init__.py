from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.config import config_app

db = SQLAlchemy()
migrate = Migrate()

from app.models import *

def create_app():
    # instantiate flask app
    app = Flask(__name__)

    config_app(app)

    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        db.create_all()

    # register blueprints

    return app
