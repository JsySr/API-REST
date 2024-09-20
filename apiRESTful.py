from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# URL base del Mock API
BASE_URL = 'https://66eb848d55ad32cda47cc96b.mockapi.io/IoTCarStatus'

# Ruta para obtener todos los datos (GET)
@app.route('/cars', methods=['GET'])
def get_all_cars():
    response = requests.get(BASE_URL)
    return jsonify(response.json()), response.status_code

# Ruta para obtener un coche específico por ID (GET)
@app.route('/cars/<int:id>', methods=['GET'])
def get_car_by_id(id):
    response = requests.get(f'{BASE_URL}/{id}')
    return jsonify(response.json()), response.status_code

# Ruta para crear un nuevo coche (POST)
@app.route('/cars', methods=['POST'])
def create_car():
    data = request.json
    response = requests.post(BASE_URL, json=data)
    return jsonify(response.json()), response.status_code

# Ruta para actualizar un coche existente (PUT)
@app.route('/cars/<int:id>', methods=['PUT'])
def update_car(id):
    data = request.json
    response = requests.put(f'{BASE_URL}/{id}', json=data)
    return jsonify(response.json()), response.status_code

# Ruta para eliminar un coche (DELETE)
@app.route('/cars/<int:id>', methods=['DELETE'])
def delete_car(id):
    response = requests.delete(f'{BASE_URL}/{id}')
    return jsonify({"message": "Car deleted successfully"}), response.status_code

# Iniciar la aplicación Flask
if __name__ == '__main__':
    app.run(debug=True)
