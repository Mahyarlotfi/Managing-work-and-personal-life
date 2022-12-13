"""All Models Are Placed In This File."""
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import (
    db,
    login
)


class User(UserMixin, db.Model):
    """User Model For Database"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return f"<User {self.username}>"

    def set_password(self, password):
        """Generating Password Hash For Database"""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Check User Input Password Hash With Database"""
        return check_password_hash(self.password_hash, password)


@login.user_loader
def load_user(user_id):
    """This callback is used to reload the user object from the user ID stored in the session."""
    return User.query.get(int(user_id))
