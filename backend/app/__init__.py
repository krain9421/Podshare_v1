from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.config import config_app
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()

from app.models import *

def create_app():
    # instantiate flask app
    app = Flask(__name__)

    config_app(app)

    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)

    with app.app_context():
        db.create_all()

    # register blueprints
    from app.routes.auth import auth_bp

    app.register_blueprint(auth_bp)
    return app
