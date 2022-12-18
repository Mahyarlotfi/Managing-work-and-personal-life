""" All variables are placed in this file """
import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """ add more variables here """
    SECRET_KEY = os.environ.get(
        'SECRET_KEY') or '63f6fe797026d794e0dc3e2bd279aee19dd2f8db67488172a644bb68792a570c'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    debug = True
    FLASK_ADMIN_SWATCH = "cerulean"
