from unicodedata import name
from flask import Flask
import pms.extensions
from config import Config
from pms.routes import bp as views_bp
from pms.extensions import db, migrate, login


def create_app():
    """Create App Function"""
    my_app = Flask(__name__)
    # Add Config Here
    my_app.config.from_object(Config)
    # Initialize Flask extensions here
    db.init_app(my_app)
    migrate.init_app(my_app, db)
    login.init_app(my_app)
    # Register blueprints here
    my_app.register_blueprint(views_bp)
    return my_app

app = create_app()
