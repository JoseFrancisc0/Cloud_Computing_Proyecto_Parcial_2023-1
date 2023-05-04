from flask import Blueprint, jsonify, request
from app import db
from models import Reservation, Client, Car, Location

# BP de la API
reservations_api = Blueprint('reservations', __name__)

# CREATE
@reservations_api.route('/reservations', method = ['POST'])
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
@reservations_api.route('/reservations', method = ['GET'])
def get_reservations():
    reservations = Reservation.query.all()
    return jsonify([reservation.serialize() for reservation in reservations]), 200

# READ (each)
@reservations_api.route('/reservations/<int:id>', method = ['GET'])
def get_reservation(id):
    reservation = Reservation.query.get(id)
    if reservation is None:
        return jsonify({'error' : 'Reservation not found'}), 404
    
    return jsonify(reservation.serialize()), 200

# UPDATE
@reservations_api.route('/reservations/<int:id>', method = ['PATCH'])
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
@reservations_api.route('/reservations/<int:id>', method = ['DELETE'])
def delete_reservation(id):
    reservation = Reservation.query.get(id)
    if reservation is None:
        return jsonify({'error' : 'Reservation not found'}), 404
    
    db.session.delete(reservation)
    db.session.commit()
    return '', 204