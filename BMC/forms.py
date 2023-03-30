from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField 
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from BMC.models import User, Venue, Show, Ticket, Admin


class RegistrationForm(FlaskForm):
    fullname = StringField('Fullname', validators=[DataRequired()])
    username = StringField('Select Username', 
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
        elif username.data.lower() == "admin":
                raise ValidationError('This is a restricted username')
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
    fullname = StringField('Fullname', validators=[DataRequired()])
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
            elif username.data.lower() == "admin":
                raise ValidationError('This is a restricted username')
    
    def validate_email(self, email):
        if email.data != current_user.email: # type: ignore
            email = User.query.filter_by(email=email.data).first()
            if email:
                raise ValidationError('Email is already associated with an account')

class AdminRegistrationForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                             validators=[DataRequired(), Length(min=8, max=24)])
    confirm_password = PasswordField('Confirm Password',
                                        validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    
    def validate_email(self, email):
        email = User.query.filter_by(email=email.data).first()
        if email:
            raise ValidationError('Email is already associated with an account')

class AdminLoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                             validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class VenueForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    place = StringField('Place', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    capacity = StringField('Capacity', validators=[DataRequired()])
    submit = SubmitField('Add Venue')

class EditVenueForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    place = StringField('Place', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    capacity = StringField('Capacity', validators=[DataRequired()])
    submit = SubmitField('Save Changes')

class ShowForm(FlaskForm):
    venue_id = StringField('Venue ID', validators=[DataRequired()])
    title = StringField('Title', validators=[DataRequired()])
    rating = StringField('Rating', validators=[DataRequired()])
    time = StringField('Time', validators=[DataRequired()])
    tags = StringField('Tags', validators=[DataRequired()])
    price = StringField('Price', validators=[DataRequired()])
    tickets = StringField('Seats Left', validators=[DataRequired()])
    submit = SubmitField('Add Show')
    
    def check_venue_id(self, venue_id):
        if type(venue_id) != int:
            raise ValidationError('Venue ID must be an integer')
    def check_title(self, title):
        if type(title) != str:
            raise ValidationError('Title must be a string')
    def check_rating(self, rating):
        if type(rating) != float:
            raise ValidationError('Rating must be a float')
    def check_time(self, time):
        if type(time) != str:
            raise ValidationError('Time must be a string')
    def check_tags(self, tags):
        if type(tags) != str:
            raise ValidationError('Tags must be a string')
    def check_price(self, price):
        if type(price) != float:
            raise ValidationError('Price must be a float')
    def check_tickets(self, tickets):
        if type(tickets) != int:
            raise ValidationError('Number of Tickets must be an integer')
    def validate_ticket_number(self, tickets, venue_id):
        venue_capacity = Venue.query.filter_by(id=venue_id).first().capacity
        if tickets > venue_capacity:
            raise ValidationError('Number of Seats exceeds venue capacity')
        if tickets < 0:
            raise ValidationError('Number of Seats cannot be negative')

class EditShowForm(FlaskForm):
    venue_id = StringField('Venue ID', validators=[DataRequired()])
    title = StringField('Title', validators=[DataRequired()])
    rating = StringField('Rating', validators=[DataRequired()])
    time = StringField('Time', validators=[DataRequired()])
    tags = StringField('Tags', validators=[DataRequired()])
    price = StringField('Price', validators=[DataRequired()])
    tickets = StringField('Seats Left', validators=[DataRequired()])
    submit = SubmitField('Save Changes')

    def check_venue_id(self, venue_id):
        if type(venue_id) != int:
            raise ValidationError('Venue ID must be an integer')
    def check_title(self, title):
        if type(title) != str:
            raise ValidationError('Title must be a string')
    def check_rating(self, rating):
        if type(rating) != float:
            raise ValidationError('Rating must be a float')
    def check_time(self, time):
        if type(time) != str:
            raise ValidationError('Time must be a string')
    def check_tags(self, tags):
        if type(tags) != str:
            raise ValidationError('Tags must be a string')
    def check_price(self, price):
        if type(price) != float:
            raise ValidationError('Price must be a float')
    def check_tickets(self, tickets):
        if type(tickets) != int:
            raise ValidationError('Number of Tickets must be an integer')
        
    def validate_ticket_number(self, tickets, venue_id):
        venue_capacity = Venue.query.filter_by(id=venue_id).first().capacity
        if tickets > venue_capacity:
            raise ValidationError('Number of Seats exceeds venue capacity')
        if tickets < 0:
            raise ValidationError('Number of Seats cannot be negative')