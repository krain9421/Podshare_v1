from os import getenv
from dotenv import load_dotenv
from flask import jsonify
from app.utils.errors import CustomError
from flask_cors import CORS

load_dotenv()

def config_app(app):
    # config app
    app.config['SECRET_KEY'] = getenv('SECRET_KEY', 'secret_key:D')
    app.config['SQLALCHEMY_DATABASE_URI'] = getenv('SQLALCHEMY_DATABASE_URI')
    app.config["SESSION_PERMANENT"] = False
    app.config["SESSION_TYPE"] = "filesystem"

    # configure CORS
    cors = CORS(app, resources={r'/api/*': {'origins': getenv('FRONTEND_DOMAIN'), 'supports_credentials': True}})

    # add error handlers
    @app.errorhandler(CustomError)
    def handle_authentication_error(error):
        response = {
            'error': error.message
        }
        return jsonify(response), error.status_code

    @app.errorhandler(404)
    def handle_not_found_error(error):
        response = {
        'error': 'Resource not found',
        }
        return jsonify(response), 404
    
    @app.errorhandler(Exception)
    def handle_generic_error(error):
        response = {
            'error': 'An unexpected error occurred',
        }
        print(error)
        return jsonify(response), 500
