from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_session import Session
from flask_status import FlaskStatus
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
    FlaskStatus(app)
    Session(app)

    with app.app_context():
        db.create_all()

    # register blueprints
    from app.routes.auth import auth_bp
    from app.routes.post import post_bp
    from app.routes.play import play_bp
    from app.routes.like import like_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(post_bp)
    app.register_blueprint(play_bp)
    app.register_blueprint(like_bp)

    # register frontend blueprints
    from app.routes.index import index_frontend_bp
    from app.routes.auth import auth_frontend_bp
    from app.routes.home import home_frontend_bp
    from app.routes.list import list_frontend_bp
    from app.routes.profile import profile_frontend_bp
    from app.routes.post import post_frontend_bp

    app.register_blueprint(index_frontend_bp)
    app.register_blueprint(auth_frontend_bp)
    app.register_blueprint(home_frontend_bp)
    app.register_blueprint(list_frontend_bp)
    app.register_blueprint(profile_frontend_bp)
    app.register_blueprint(post_frontend_bp)
    return app
