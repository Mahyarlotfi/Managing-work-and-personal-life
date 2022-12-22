"""All Forms Are Placed In This File."""
from flask_wtf import FlaskForm

from wtforms import (
    StringField,
    PasswordField,
    BooleanField,
    SubmitField
    )

from wtforms.validators import (
    DataRequired,
    ValidationError,
    Email,
    EqualTo
    )

from pms.models import (
    User
    )


class LoginForm(FlaskForm):
    """Login Form"""
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Login')


class RegistrationForm(FlaskForm):
    """Registration Form"""
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        """Checking That The Username Is Allowed

        Args:
            username (String): Username taken through the form

        Raises:
            ValidationError: Raised when a validator fails to validate its input.
        """
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        """Checking That The Email Is Allowed

        Args:
            email (String): Email taken through the form

        Raises:
            ValidationError: Raised when a validator fails to validate its input.
        """
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')
