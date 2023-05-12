from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# Flask/SQLAlchemy instance
reservations_api = Flask(__name__)
reservations_api.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:nKaqQ1wlHFBq3cGCvB6u@database-proyecto.crt5dlbdpqks.us-east-1.rds.amazonaws.com:5432/postgres"
reservations_api.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(reservations_api)
CORS(reservations_api)

# Client Model
class Client(db.Model):
    __tablename__ = 'clients'
    id = db.Column(db.Integer, primary_key = True, nullable = False)
    firstname = db.Column(db.String(30), nullable = False)
    lastname = db.Column(db.String(30), nullable = False)

    def __repr__(self):
        return f'<Client {self.id}>'

# Car Model
class Car(db.Model):
    __tablename__ = 'cars'
    id = db.Column(db.Integer, primary_key = True, nullable = False)
    brand = db.Column(db.String(30), nullable = False)
    model = db.Column(db.String(60), nullable = False)
    type_of_car = db.Column(db.String(30), nullable = False)
    year_car = db.Column(db.Integer, nullable = False)
    cost_per_day = db.Column(db.Integer, nullable = False)
    image = db.Column(db.String(150), nullable = False)
    def __repr__(self):
        return f'<Car {self.id}>'
    
# Location Model
class Location(db.Model):
    __tablename__ = 'locations'
    id = db.Column(db.Integer, primary_key = True, nullable = False)
    address = db.Column(db.String(120), nullable = False)
    district = db.Column(db.String(50), nullable = False)
    def __repr__(self):
        return f'<Location {self.id}>'

# Resevation Model
class Reservation(db.Model):
    __tablename__ = 'reservations'
    id = db.Column(db.Integer, primary_key = True, nullable = False)
    client_id = db.Column(db.Integer, db.ForeignKey('clients.id'), nullable = False)
    car_id = db.Column(db.Integer, db.ForeignKey('cars.id'), nullable = False)
    location_id = db.Column(db.Integer, db.ForeignKey('locations.id'), nullable = False)
    date = db.Column(db.DateTime, nullable = False)
    start_of_rental = db.Column(db.DateTime, nullable = False)
    end_of_rental = db.Column(db.DateTime, nullable = False)
    total_cost = db.Column(db.Float, nullable = False)

# API ENDPOINTS
# CREATE
@reservations_api.route('/reservations', methods = ['POST'])
def create_reservation():
    data = request.get_json()
    
    client = Client.query.get(data['client_id'])
    if client is None:
        return jsonify({'error': 'Client not found'}), 404

    car = Car.query.get(data['car_id'])
    if car is None:
        return jsonify({'error': 'Car not found'}), 404

    location = Location.query.get(data['location_id'])
    if location is None:
        return jsonify({'error': 'Location not found'}), 404

    reservation = Reservation(client_id = data['client_id'], car_id = data['car_id'], location_id = data['location_id'], date = data['date'], start_of_rental = data['start_of_rental'], end_of_rental = data['end_of_rental'], total_cost = data['total_cost'])
    db.session.add(reservation)
    db.session.commit()
    return jsonify(reservation.serialize()), 201

# READ (all)
@reservations_api.route('/reservations', methods = ['GET'])
def get_reservations():
    reservations = Reservation.query.all()
    return jsonify([{'id': reservation.id,
                     'client_id': reservation.client_id,
                     'car_id': reservation.car_id,
                     'location_id': reservation.location_id,
                     'date': reservation.date,
                     'start_of_rental': reservation.start_of_rental,
                     'end_of_rental' : reservation.end_of_rental,
                     'total_cost' : reservation.total_cost} for reservation in reservations]), 200

# READ (each)
@reservations_api.route('/reservations/<int:id>', methods = ['GET'])
def get_reservation(id):
    reservation = Reservation.query.get(id)
    if reservation is None:
        return jsonify({'error' : 'Reservation not found'}), 404
    
    return jsonify(reservation.serialize()), 200

# UPDATE
@reservations_api.route('/reservations/<int:id>', methods = ['PATCH'])
def update_reservation(id):
    reservation = Reservation.query.get(id)
    if reservation is None:
        return jsonify({'error' : 'Reservation not found'}), 404

    data = request.get_json()

    if 'client_id' in data:
        client = Client.query.get(data['client_id'])
        if client is None:
            return jsonify({'error' : 'Client not found'}), 404
        else:
            reservation.client_id = data['client_id']

    if 'car_id' in data:
        car = Car.query.get(data['car_id'])
        if car is None:
            return jsonify({'error' : 'Car not found'}), 404
        else:
            reservation.car_id = data['car_id']
    
    if 'location_id' in data:
        location = Location.query.get(data['location_id'])
        if location is None:
            return jsonify({'error' : 'Location not found'}), 404
        else:
            reservation.car_id = data['location_id']
    
    if 'date' in data:
        reservation.date = data['date']
    if 'start_of_rental' in data:
        reservation.start_of_rental = data['start_of_rental']
    if 'end_of_rental' in data:
        reservation.end_of_rental = data['end_of_rental']
    if 'total_cost' in data:
        reservation.total_cost = data['total_cost']
    
    db.session.commit()
    return jsonify(reservation.serialize()), 200


# DELETE
@reservations_api.route('/reservations/<int:id>', methods = ['DELETE'])
def delete_reservation(id):
    reservation = Reservation.query.get(id)
    if reservation is None:
        return jsonify({'error' : 'Reservation not found'}), 404
    
    db.session.delete(reservation)
    db.session.commit()
    return '', 204

# Run
if __name__ == '__main__':
    reservations_api.run(host = '0.0.0.0', port = 8014, debug = True)