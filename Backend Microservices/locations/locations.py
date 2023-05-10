from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

# Flask/SQLAlchemy instance
locations_api = Flask(__name__)
locations_api.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:nKaqQ1wlHFBq3cGCvB6u@database-proyecto.crt5dlbdpqks.us-east-1.rds.amazonaws.com:5432/postgres"
locations_api.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(locations_api)

# Location Model
class Location(db.Model):
    __tablename__ = 'locations'
    id = db.Column(db.Integer, primary_key = True, nullable = False)
    address = db.Column(db.String(120), nullable = False)
    district = db.Column(db.String(50), nullable = False)
    def __repr__(self):
        return f'<Location {self.id}>'

# 404 Error Handler 
@locations_api.errorhandler(404)
def not_found(error):
    return jsonify({'error' : 'Not found.'}), 404

# 500 Error Handler
@locations_api.errorhandler(500)
def internal_server_error(error):
    return jsonify({'error' : 'Internal server error.'}), 500

# CREATE
@locations_api.route('/locations', methods = ['POST'])
def create_location():
    data = request.get_json()
    location = Location(address = data['address'], district = data['district'])
    db.session.add(location)
    db.session.commit()
    return jsonify({'message' : 'Location created sucessfully'}), 201

# READ (all)
@locations_api.route('/locations', methods = ['GET'])
def get_locations():
    locations = Location.query.all()
    return jsonify([{'id' : location.id,
                      'address' : location.address,
                      'district' : location.district} for location in locations]), 200

# READ (each)
@locations_api.route('/locations/<int:id>', methods = ['GET'])
def get_location(id):
    location = Location.query.get(id)
    if location is None:
        return not_found(404)
    return jsonify({'id' : location.id,
                      'address' : location.address,
                      'district' : location.district}), 200

# UPDATE
@locations_api.route('/locations/<int:id>', methods = ['PATCH'])
def update_location(id):
    location = Location.query.get(id)

    if location is None:
        return not_found(404)

    data = request.get_json()
    if 'address' in data:
        location.address = data['address']
    if 'district' in data:
        location.district = data['district']
    db.session.commit()
    return jsonify({'message' : 'Location updated successfully'}), 200

# DELETE
@locations_api.route('/locations/<int:id>', methods = ['DELETE'])
def delete_location(id):
    location = Location.query.get(id)
    if location is None:
        return not_found(404)

    db.session.delete(location)
    db.session.commit()
    return jsonify({'message' : 'Location deleted successfully'}),204

# Run
if __name__ == '__main__':
    locations_api.run(port = 8013, debug = True)