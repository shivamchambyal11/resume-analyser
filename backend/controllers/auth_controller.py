from flask import request, jsonify

from services.auth_services import register_user, login_user

def register():
    data = request.get_json()

    name = data.get("name")
    email = data.get("email")
    password = data.get("password")

    result = register_user(name, email, password)

    if "error" in result:
        return jsonify(result), 400

    return jsonify(result), 201

def login():
    data = request.get_json()

    email = data.get("email")
    password = data.get("password")

    result = login_user(email, password)

    if "error" in result:
        return jsonify(result), 401

    return jsonify(result), 200