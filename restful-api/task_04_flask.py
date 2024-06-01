#!/usr/bin/python3
"""Module compiled with Python3"""
from flask import Flask, jsonify, request
from markupsafe import escape

app = Flask(__name__)
users = {
        "jane": {"name": "Jane", "age": 28, "city": "Los Angeles"},
        "noah": {"name": "Noah", "age": 7, "city": "Thonon-les-Bains"}
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
        return jsonify({username: user_data})


@app.post('/users')
def add_users():
    new_user = request.get_json()
    username = new_user.get("username")
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
