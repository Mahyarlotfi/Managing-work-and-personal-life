from unicodedata import name
from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from config import Config
from .models import User
from .routes import bp as views_bp
from .extensions import db, migrate, login



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
    admin = Admin(my_app, name='microblog', template_mode='bootstrap4')
    # Add administrative views here
    admin.add_view(ModelView(User, db.session))
    return my_app

app = create_app()
