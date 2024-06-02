#!/usr/bin/python3
"""Module compiled with Python3"""
from flask import Flask, jsonify, request

app = Flask(__name__)
users = {}


@app.route('/')
def home():
    """Function that handles index"""
    return "Welcome to the Flask API!"


@app.route('/data')
def data():
    """
    Function that converts in JSON and returns the keys of the users dictionary
    """
    users_keys = list(users.keys())
    return jsonify(users_keys), 200


@app.route('/users/<username>')
def users_data(username):
    """Function that handles the users data"""
    user_data = users.get(username)
    if not user_data:
        return jsonify({"error": "User not found"}), 400
    else:
        return jsonify(user_data), 200


@app.route('/add_user', methods=['POST'])
def add_users():
    """Function that allows the addition of new users"""
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    new_user = request.get_json()
    username = new_user.get("username")

    if not username:
        return jsonify({"error": "Username is required"}), 400
    if username in users:
        return jsonify({"error": "User already exists"}), 400

    users[username] = {
        "username": new_user.get("username", ""),
        "name": new_user.get("name", ""),
        "age": new_user.get("age", ""),
        "city": new_user.get("city", "")
    }
    return jsonify({"message": "User added", "user": users[username]}), 200


@app.route('/status')
def status():
    """Returns the status of the server"""
    return "OK", 200


if __name__ == "__main__":
    app.run()
