from unicodedata import name
from flask import Flask
import pms.extensions
from config import Config
from pms.routes import bp as views_bp
from pms.extensions import db, migrate, login


app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate.init_app(app, db)
login.init_app(app)
app.register_blueprint(views_bp)
