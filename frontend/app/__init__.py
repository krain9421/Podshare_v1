from flask import Flask

def create_app():
    # instantiate flask app
    app = Flask(__name__)

    # register blueprints
    from app.routes.index import index_bp
    from app.routes.auth import auth_bp
    from app.routes.home import home_bp
    from app.routes.list import list_bp
    from app.routes.profile import profile_bp

    app.register_blueprint(index_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(home_bp)
    app.register_blueprint(list_bp)
    app.register_blueprint(profile_bp)
    return app
