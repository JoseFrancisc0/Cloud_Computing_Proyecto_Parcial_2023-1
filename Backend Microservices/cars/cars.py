from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# Flask/SQLAlchemy instance
cars_api = Flask(__name__)
cars_api.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:nKaqQ1wlHFBq3cGCvB6u@database-proyecto.crt5dlbdpqks.us-east-1.rds.amazonaws.com:5432/postgres"
cars_api.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(cars_api)
CORS(cars_api)

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

# 404 Error Handler 
@cars_api.errorhandler(404)
def not_found(error):
    return jsonify({'error' : 'Not found.'}), 404

# 500 Error Handler
@cars_api.errorhandler(500)
def internal_server_error(error):
    return jsonify({'error' : 'Internal server error.'}), 500

# CREATE API Endpoint
@cars_api.route('/cars', methods = ['POST'])
def create_car():
    data = request.get_json()
    car = Car(brand = data['brand'], model = data['model'], type_of_car = data['type_of_car'], year_car = data['year_car'], cost_per_day = data['cost_per_day'], image = data['image'])
    db.session.add(car)
    db.session.commit()
    return jsonify({'message' : 'Car created successfully'}), 201

# READ (all) API Endpoint
@cars_api.route('/cars', methods = ['GET'])
def get_cars():
    cars = Car.query.all()
    return jsonify([{'id' : car.id,
                        'brand' : car.brand,
                        'model': car.model,
                        'type_of_car' : car.type_of_car,
                        'year_car' : car.year_car,
                        'cost_per_day' : car.cost_per_day,
                        'image': car.image} for car in cars]), 200

# READ (each)
@cars_api.route('/cars/<int:id>', methods = ['GET'])
def get_car(id):
    car = Car.query.get(id)
    if car is None:
        return not_found(404)
    return jsonify({'id' : car.id,
                        'brand' : car.brand,
                        'model': car.model,
                        'type_of_car' : car.type_of_car,
                        'year_car' : car.year_car,
                        'cost_per_day' : car.cost_per_day,
                        'image': car.image}), 200

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
    if 'type_of_car' in data:
        car.type_of_car = data['type_of_car']
    if 'year_car' in data:
        car.year_car = data['year_car']
    if 'cost_per_day' in data:
        car.cost_per_day = data['cost_per_day']
    if 'image' in data:
        car.image = data['image']

    db.session.commit()
    return jsonify({'message' : 'Car updated successfully'}), 200

# DELETE
@cars_api.route('/cars/<int:id>', methods = ['DELETE'])
def delete_car(id):
    car = Car.query.get(id)
    if car is None:
        return not_found(404)

    db.session.delete(car)
    db.session.commit()
    return jsonify({'message' : 'Car deleted successfully'}),204

# Run
if __name__ == '__main__':
    cars_api.run(port = 8012, debug = True)
