from flask import Flask
from unicodedata import name


app = Flask(__name__)

from app import routes

