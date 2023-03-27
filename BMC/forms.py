from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField 
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from BMC.models import User


class RegistrationForm(FlaskForm):
    username = StringField('Username', 
                           validators=[DataRequired(), Length(min=3, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                             validators=[DataRequired(), Length(min=8, max=24)])
    confirm_password = PasswordField('Confirm Password',
                                        validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username is already taken')
    
    def validate_email(self, email):
        email = User.query.filter_by(email=email.data).first()
        if email:
            raise ValidationError('Email is already associated with an account')

class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                             validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class UpdateAccountForm(FlaskForm):
    username = StringField('Username', 
                           validators=[DataRequired(), Length(min=3, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username: # type: ignore
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('Username is already taken')
    
    def validate_email(self, email):
        if email.data != current_user.email: # type: ignore
            email = User.query.filter_by(email=email.data).first()
            if email:
                raise ValidationError('Email is already associated with an account')

