from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from BMC import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), unique = True, nullable = False)
    email = db.Column(db.String(120), unique = True, nullable = False)
    password = db.Column(db.String(60), nullable = False)

    def __repr__(self):
        return f"User('{self.id}, {self.username}', '{self.email}')"
    
class Venue(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    city = db.Column(db.String(100), nullable = False)
    state = db.Column(db.String(100), nullable = False)
    capacity = db.Column(db.Integer, nullable = False)

    def __repr__(self):
        return f"Venue('{self.id}, {self.name}', '{self.city}', '{self.state}')"
    
class Show(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    venue_id = db.Column(db.Integer, db.ForeignKey('venue.id'), primary_key = True)
    title = db.Column(db.String(100), nullable = False)
    time = db.Column(db.String(100), nullable = False) # time format HH:MM AM/PM
    price = db.Column(db.Integer, nullable = False)

    def __repr__(self):
        return f"Show('{self.id}, {self.title}', '{self.venue_id}', '{self.time}', '{self.price}')"
    
class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key = True)
    venue_id = db.Column(db.Integer, db.ForeignKey('venue.id'), primary_key = True)
    show_id = db.Column(db.Integer, db.ForeignKey('show.id'), primary_key = True)
    num_tickets = db.Column(db.Integer, nullable = False)
    total_price = db.Column(db.Integer, nullable = False)


    def __repr__(self):
        return f'Ticket("{self.id}, {self.user_id}", "{self.venue_id}", "{self.show_id}", "{self.num_tickets}", "{self.total_price}")'
