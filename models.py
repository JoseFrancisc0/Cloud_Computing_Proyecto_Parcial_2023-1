from app import db
from datetime import datetime

# Modelo de cliente
class Client(db.Model):
    __tablename__ = 'clients'
    id = db.Column(db.Integer, primary_key = True)
    firstname = db.Column(db.String(30))
    lastname = db.Column(db.String(30))

# Modelo de vehiculo
class Car(db.Model):
    __tablename__ = 'cars'
    id = db.Column(db.Integer, primary_key = True)
    brand = db.Column(db.String(30))
    model = db.Column(db.String(60))
    type = db.Column(db.String(30))
    year = db.Column(db.Integer)
    cost = db.Column(db.Integer)

# Modelo de local
class Location(db.Model):
    __tablename__ = 'locations'
    id = db.Column(db.Integer, primary_key = True)
    address = db.Column(db.String(120))
    district = db.Column(db.String(50))

# Modelo de reserva
class Reservation(db.Model):
    __tablename__ = 'reservations'
    id = db.Column(db.Integer, primary_key = True)
    client_id = db.Column(db.Integer, db.ForeignKey('clients.id'))
    car_id = db.Column(db.Integer, db.ForeignKey('cars.id'))
    location_id = db.Column(db.Integer, db.ForeignKey('locations.id'))
    date = db.Column(db.DateTime, default=datetime.utcnow)
    start_of_rental = db.Column(db.DateTime)
    end_of_rental = db.Column(db.DateTime)
    total_cost = db.Column(db.Float)

    client = db.relationship("Client", backref = "reservations")
    car = db.relationship("Car", backref = "reservations")
    location = db.relationship("Location", backref = "reservations")
