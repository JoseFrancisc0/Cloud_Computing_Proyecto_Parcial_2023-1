from flask import Blueprint, jsonify, request
from app import db
from models import Car

# BP de la API
cars_api = Blueprint('cars', __name__)

# CREATE
@cars_api.route('/cars', methods = ['POST'])
def create_car():
    data = request.get_json()
    car = Car(brand = data['brand'], model = data['model'], type = data['type'], year = data['year'], cost = data['cost'])
    db.session.add(car)
    db.session.commit()
    return jsonify(car.serialize()), 201

# READ (all)
@cars_api.route('/cars', methods = ['GET'])
def get_cars():
    cars = Car.query.all()
    return jsonify([car.serialize() for car in cars]), 200

# READ (each)
@cars_api.route('/cars/<int:id>', methods = ['GET'])
def get_car(id):
    car = Car.query.get(id)
    if car is None:
        return jsonify({'error': 'Car not found'}), 404
    return jsonify(car.serialize()), 200

# UPDATE
@cars_api.route('/cars/<int:id>', methods = ['PATCH'])
def update_car(id):
    car = Car.query.get(id)

    if car is None:
        return jsonify({'error' : 'Car not found'}), 404

    data = request.get_json()
    if 'brand' in data:
        car.brand = data['brand']
    if 'model' in data:
        car.model = data['model']
    if 'type' in data:
        car.type = data['type']
    if 'year' in data:
        car.year = data['year']
    if 'cost' in data:
        car.cost = data['cost']

    db.session.commit()
    return jsonify(car.serialize()), 200

# DELETE
@cars_api.route('/cars/<int:id>', methods = ['DELETE'])
def delete_car(id):
    car = Car.query.get(id)
    if car is None:
        return jsonify({'error' : 'Car not found'}), 404

    db.session.delete(car)
    db.session.commit()
    return '',204