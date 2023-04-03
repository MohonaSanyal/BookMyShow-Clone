from BMC import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    fullname = db.Column(db.String(100), nullable = False)
    username = db.Column(db.String(20), unique = True, nullable = False)
    email = db.Column(db.String(120), unique = True, nullable = False)
    password = db.Column(db.String(60), nullable = False)

    def __repr__(self):
        return f"User('{self.id}, {self.username}', '{self.email}')"
    
    def data(self):
        return {
            'id': self.id,
            'fullname': self.fullname,
            'username': self.username,
            'email': self.email,
            'password': self.password
        }

class Admin(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(120), unique = True, nullable = False)
    password = db.Column(db.String(60), nullable = False)

    def __repr__(self):
        return f"Admin('{self.id}, {self.email}')"
    
    def data(self):
        return {
            'id': self.id,
            'email': self.email,
            'password': self.password
        }

class Venue(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    place = db.Column(db.String(100), nullable = False)
    location = db.Column(db.String(100), nullable = False)
    capacity = db.Column(db.Integer, nullable = False)

    def __repr__(self):
        return f"Venue('{self.id}, {self.name}', '{self.place}', '{self.location}', '{self.capacity}')"
    
    def data(self):
        return {
            'id': self.id,
            'name': self.name,
            'place': self.place,
            'location': self.location,
            'capacity': self.capacity
        }
    
class Show(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    venue_id = db.Column(db.Integer, db.ForeignKey('venue.id'), primary_key = True)
    rating = db.Column(db.Float, nullable = False)
    title = db.Column(db.String(100), nullable = False)
    time = db.Column(db.String(100), nullable = False)
    tags = db.Column(db.String(100), nullable = False)
    price = db.Column(db.Integer, nullable = False)
    tickets = db.Column(db.Integer, nullable = False)

    def __repr__(self):
        return f"Show('{self.id}, {self.title}', '{self.venue_id}', '{self.time}', '{self.price}', '{self.tickets}')"
    
    def data(self):
        return {
            'id': self.id,
            'venue_id': self.venue_id,
            'rating': self.rating,
            'title': self.title,
            'time': self.time,
            'tags': self.tags,
            'price': self.price,
            'tickets': self.tickets
        }

class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key = True)
    venue_id = db.Column(db.Integer, db.ForeignKey('venue.id'), primary_key = True)
    show_id = db.Column(db.Integer, db.ForeignKey('show.id'), primary_key = True)
    num_tickets = db.Column(db.Integer, nullable = False)
    total_price = db.Column(db.Integer, nullable = False)


    def __repr__(self):
        return f'Ticket("{self.id}, {self.user_id}", "{self.venue_id}", "{self.show_id}", "{self.num_tickets}", "{self.total_price}")'

    def data(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'venue_id': self.venue_id,
            'show_id': self.show_id,
            'num_tickets': self.num_tickets,
            'total_price': self.total_price
        }