from flask import Blueprint, jsonify, request
from app import db
from models import Location

# BP de la API
locations_api = Blueprint('locations', __name__)

# CREATE
@locations_api.route('/locations', methods = ['POST'])
def create_location():
    data = request.get_json()
    location = Location(address = data['address'], district = data['district'])
    db.session.add(location)
    db.session.commit()
    return jsonify(location.serialize()), 201

# READ (all)
@locations_api.route('/locations', methods = ['GET'])
def get_locations():
    locations = Location.query.all()
    return jsonify([location.serialize() for location in locations]), 200

# READ (each)
@locations_api.route('/locations/<int:id>', methods = ['GET'])
def get_location(id):
    location = Location.query.get(id)
    if location is None:
        return jsonify({'error': 'Location not found'}), 404
    return jsonify(location.serialize()), 200

# UPDATE
@locations_api.route('/locations/<int:id>', methods = ['PATCH'])
def update_location(id):
    location = Location.query.get(id)

    if location is None:
        return jsonify({'error' : 'Location not found'}), 404

    data = request.get_json()
    if 'address' in data:
        location.address = data['address']
    if 'district' in data:
        location.district = data['district']
    db.session.commit()
    return jsonify(location.serialize()), 200

# DELETE
@locations_api.route('/locations/<int:id>', methods = ['DELETE'])
def delete_location(id):
    location = Location.query.get(id)
    if location is None:
        return jsonify({'error' : 'Location not found'}), 404

    db.session.delete(location)
    db.session.commit()
    return '',204