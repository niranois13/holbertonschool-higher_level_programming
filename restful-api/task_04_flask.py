#!/usr/bin/python3
"""Module compiled with Python3"""
from flask import Flask, jsonify, request
from markupsafe import escape

app = Flask(__name__)
users = {
        "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
        "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
    }


@app.route('/')
def home():
    return "Welcome to the Flask API!"


@app.route('/data')
def data():
    users_keys = list(users.keys())
    return jsonify(users_keys)


@app.route('/users/<username>')
def users_data(username):
    username = escape(username)
    user_data = users.get(username)
    if not user_data:
        return {"error": "User not found"}
    else:
        return jsonify(user_data)


@app.post('/add_users')
def add_users():
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"})

    new_user = request.get_json()
    username = new_user.get("username")

    if not username:
        return jsonify({"error": "Username is required"})
    if username in users:
        return jsonify({"error": "User already exists"})

    users[username] = {
        "name": new_user.get("name", ""),
        "age": new_user.get("age", ""),
        "city": new_user.get("city", "")
    }
    return jsonify({"message": "User added", "user": users[username]})


@app.route('/status')
def status():
    return "OK"


if __name__ == "__main__":
    app.run()
