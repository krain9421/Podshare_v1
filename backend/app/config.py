from os import getenv
from dotenv import load_dotenv

load_dotenv()

def config_app(app):
    # config app
    app.config['SECRET_KEY'] = getenv('SECRET_KEY', 'secret_key:D')
    app.config['SQLALCHEMY_DATABASE_URI'] = getenv('SQLALCHEMY_DATABASE_URI')
