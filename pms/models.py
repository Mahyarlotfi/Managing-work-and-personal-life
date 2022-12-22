"""All Models Are Placed In This File."""
from jdatetime import datetime

from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

from flask_login import UserMixin

from pms.extensions import (
    db,
    login
)


class User(UserMixin, db.Model):
    """User Model For Database"""
    __tablename__ = 'user'
    id = db.Column(
        db.Integer,
        primary_key=True
        )
    username = db.Column(
        db.String(64),
        index=True,
        unique=True
        )
    email = db.Column(
        db.String(120),
        index=True,
        unique=True
        )
    password_hash = db.Column(
        db.String(128)
        )
    account_name = db.relationship(
        'Bankaccount',
        backref='user',
        lazy=True
        )

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


class Bankname(db.Model):
    """Bank Name Model For Database"""
    __tablename__ = 'bankname'
    id = db.Column(
        db.Integer,
        primary_key=True
        )
    bank_name = db.Column(
        db.String(64),
        unique=True
        )
    account_name = db.relationship(
        'Bankaccount',
        backref='bankname',
        lazy=True
        )

    def __repr__(self):
        return f"<Bankname {self.bank_name}>"


class Bankaccount(db.Model):
    """Bank Account Model For Database"""
    __tablename__ = 'bankaccount'
    id = db.Column(
        db.Integer,
        primary_key=True
        )
    account_name = db.Column(
        db.String(64),
        unique=True
        )
    account_number = db.Column(
        db.Integer,
        unique=True,
        nullable=True
        )
    card_number = db.Column(
        db.Integer,
        unique=True,
        nullable=True
        )
    iban_number = db.Column(
        db.Integer,
        unique=True,
        nullable=True
        )
    user_id = db.Column(
        db.Integer,
        db.ForeignKey('user.id'),
        nullable=False
        )
    bank_id = db.Column(
        db.Integer,
        db.ForeignKey('bankname.id'),
        nullable=False
        )
    transition = db.relationship(
        'Transition',
        backref='bankaccount',
        lazy=True
        )

    def __repr__(self):
        return f"<Bankaccount {self.account_name}>"


class Transitiontype(db.Model):
    """Transition Type Model For Database"""
    __tablename__ = 'transitiontype'
    id = db.Column(
        db.Integer,
        primary_key=True
        )
    transition_type = db.Column(
        db.String(60),
        unique=True
        )
    transition = db.relationship(
        'Transition',
        backref='transitiontype',
        lazy=True
        )

    def __repr__(self):
        return f"<Transitiontype {self.transition_type}>"


class Transitionsubject(db.Model):
    """Transition Subject Model For Database"""
    __tablename__ = 'transitionsubject'
    id = db.Column(
        db.Integer,
        primary_key=True
        )
    transition_subject = db.Column(
        db.String(60)
        )
    transition_sub_subject = db.Column(
        db.String(60)
        )
    transition = db.relationship(
        'Transition',
        backref='transitionsubject',
        lazy=True
        )

    def __repr__(self):
        return f"<Transitionsubject {self.transition_subject} - {self.transition_sub_subject}>"


class Transition(db.Model):
    """Transition Model For Database"""
    __tablename__ = 'transition'
    id = db.Column(
        db.Integer,
        primary_key=True
        )
    bankaccount_id = db.Column(
        db.Integer,
        db.ForeignKey('bankaccount.id'),
        nullable=False
        )
    transitiontype_id = db.Column(
        db.Integer,
        db.ForeignKey('transitiontype.id'),
        nullable=False
        )
    transitionsubject_id = db.Column(
        db.Integer,
        db.ForeignKey('transitionsubject.id'),
        nullable=False
        )
    date = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow()
        )
    amount = db.Column(
        db.Float,
        nullable=False
        )
    describtion = db.Column(
        db.Text
        )

    def __repr__(self):
        return f"<Transition {self.transition}>"
