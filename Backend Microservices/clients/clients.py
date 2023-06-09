from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# Flask/SQLAlchemy instance
clients_api = Flask(__name__)
clients_api.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:nKaqQ1wlHFBq3cGCvB6u@database-proyecto.crt5dlbdpqks.us-east-1.rds.amazonaws.com:5432/postgres"
clients_api.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(clients_api)
CORS(clients_api)

# Client Model
class Client(db.Model):
    __tablename__ = 'clients'
    id = db.Column(db.String(8), primary_key = True, nullable = False)
    firstname = db.Column(db.String(30), nullable = False)
    lastname = db.Column(db.String(30), nullable = False)

    def __repr__(self):
        return f'<Client {self.id}>'

# 404 Error Handler 
@clients_api.errorhandler(404)
def not_found(error):
    return jsonify({'error' : 'Not found.'}), 404

# 500 Error Handler
@clients_api.errorhandler(500)
def internal_server_error(error):
    return jsonify({'error' : 'Internal server error.'}), 500

# CREATE API Endopoint
@clients_api.route('/clients', methods = ['POST'])
def create_client():
    data = request.get_json()
    client = Client(id = data['id'], firstname = data['firstname'], lastname = data['lastname'])
    db.session.add(client)
    db.session.commit()
    return jsonify({'message' : 'Client created successfully'}), 201

# READ (all) API Endpoint
@clients_api.route('/clients', methods = ['GET'])
def get_clients():
    clients = Client.query.all()
    return jsonify([{'id': client.id,
                     'firstname': client.firstname,
                     'lastname': client.lastname} for client in clients]), 200

# READ (each) API Endpoint
@clients_api.route('/clients/<string:id>', methods = ['GET'])
def get_client(id):
    client = Client.query.get(id)
    if client is None:
        return not_found(404)
    return jsonify({'id': client.id,
                     'firstname': client.firstname,
                     'lastname': client.lastname}), 200

# UPDATE API Endpoint
@clients_api.route('/clients/<string:id>', methods = ['PATCH'])
def update_client(id):
    client = Client.query.get(id)

    if client is None:
        return not_found(404)

    data = request.get_json()
    if 'firstname' in data:
        client.firstname = data['firstname']
    if 'lastname' in data:
        client.lastname = data['lastname']
    db.session.commit()
    return jsonify({'message' : 'Client updated successfully'}), 200

# DELETE API Endpoint
@clients_api.route('/clients/<string:id>', methods = ['DELETE'])
def delete_client(id):
    client = Client.query.get(id)
    if client is None:
        return not_found(404)

    db.session.delete(client)
    db.session.commit()
    return jsonify({'message' : 'Client deleted successfully'}), 204

# Run
if __name__ == '__main__':
    clients_api.run(host = '0.0.0.0', port = 8011, debug = True)