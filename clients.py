from flask import Blueprint, jsonify, request
from app import db
from models import Client

# BP de la API
clients_api = Blueprint('clients', __name__)

# CREATE
@clients_api.route('/clients', methods = ['POST'])
def create_client():
    data = request.get_json()
    client = Client(firstname = data['firstname'], lastname = data['lastname'])
    db.session.add(client)
    db.session.commit()
    return jsonify(client.serialize()), 201

# READ (all)
@clients_api.route('/clients', methods = ['GET'])
def get_clients():
    clients = Client.query.all()
    return jsonify([client.serialize() for client in clients]), 200

# READ (each)
@clients_api.route('/clients/<int:id>', methods = ['GET'])
def get_client(id):
    client = Client.query.get(id)
    if client is None:
        return jsonify({'error': 'Client not found'}), 404
    return jsonify(client.serialize()), 200

# UPDATE
@clients_api.route('/clients/<int:id>', methods = ['PATCH'])
def update_client(id):
    client = Client.query.get(id)

    if client is None:
        return jsonify({'error' : 'Client not found'}), 404

    data = request.get_json()
    if 'firstname' in data:
        client.firstname = data['firstname']
    if 'lastname' in data:
        client.lastname = data['lastname']
    db.session.commit()
    return jsonify(client.serialize()), 200

# DELETE
@clients_api.route('/clients/<int:id>', methods = ['DELETE'])
def delete_client(id):
    client = Client.query.get(id)
    if client is None:
        return jsonify({'error' : 'Client not found'}), 404

    db.session.delete(client)
    db.session.commit()
    return '',204