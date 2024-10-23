from flask import Flask, jsonify, request
from services.auth_service import register_user, login_user
from services.food_service import list_food_items, add_food_item
from services.bike_service import get_bike_orders, create_bike_order, get_bike_riders
from services.home_service import get_technician_info
from services.db import init_db, seed_data

app = Flask(__name__)
init_db()  # Initialize the database
seed_data()  # Seed dummy data

@app.route('/api/register', methods=['POST'])
def register():
    data = request.json
    return jsonify(register_user(data))

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    return jsonify(login_user(data))

@app.route('/api/food', methods=['GET', 'POST'])
def food():
    if request.method == 'POST':
        data = request.json
        return jsonify(add_food_item(data))
    return jsonify(list_food_items())

@app.route('/api/bike-orders', methods=['GET', 'POST'])
def bike_orders():
    if request.method == 'POST':
        data = request.json
        return jsonify(create_bike_order(data))
    return jsonify(get_bike_orders())

@app.route('/api/riders', methods=['GET'])
def bike_riders():
    return jsonify(get_bike_riders())

@app.route('/api/technicians', methods=['GET'])
def technicians():
    return jsonify(get_technician_info())

if __name__ == '__main__':
    app.run(debug=True)
