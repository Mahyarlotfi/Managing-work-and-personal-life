import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or '63f6fe797026d794e0dc3e2bd279aee19dd2f8db67488172a644bb68792a570c'
    SQLa
# ... add more variables here as needed
