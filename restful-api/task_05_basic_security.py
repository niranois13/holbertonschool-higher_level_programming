#!/usr/bin/python3
"Module compiled with Python3"
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, JWTManager

app = Flask(__name__)
auth = HTTPBasicAuth()
app.config["JWT_SECRET_KEY"] = "5up3r-53c537"
jwt = JWTManager(app)

users = {
    "user1": {"username": "user1", "password": "<hashed_password>", "role": "user"},
    "admin1": {"username": "admin1", "password": "<hashed_password>", "role": "admin"}
}

@auth.verify_password
def verify_password(username, password):
    """
    Function that verify passwords with BasicAuth and werkzeug modules
    :param username: the name of the user
    :param password: the hashed password of the user
    """
    if username in users and \
    check_password_hash(users.get(username), password):
        return username

@app.route('/basic-protected', methods=['GET'])
@auth.login_required
def basic_protected():
    return jsonify({"msg": "Basic Auth: Access Granted"})


