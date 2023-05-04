from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from clients import clients_api
from cars import cars_api
from locations import locations_api
from reservations import reservations_api

# Creando la instancias Flask y SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'URI DE LA DB'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Registrando los BPs
app.register_blueprint(clients_api)
app.register_blueprint(cars_api)
app.register_blueprint(locations_api)
app.register_blueprint(reservations_api)

# Handler para errores
@app.errorhandler(404)
def not_found(error):
    response = jsonify({'message' : 'The requested URL was not found on the server.'})
    response.status_code = 404
    return response

if __name__ == '__main__':
    app.run(debug = True)