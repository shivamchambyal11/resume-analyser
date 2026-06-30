from flask import request, jsonify

from services.auth_services import register_user, login_user
from utils.response import success_response, error_response
from utils.validators import validate_register

def register():
    data = request.get_json()

    name = data.get("name")
    email = data.get("email")
    password = data.get("password")

    result = register_user(name, email, password)

    data = request.get_json()

    validation_error = validate_register(data)

    if validation_error:
     return error_response(validation_error, 400)

# then continue...
    if "error" in result:
        return error_response(result["error"], 400)
    
    

    return success_response(result["message"], status_code=201)
    validation_error = validate_register(data)

    


def login():
    data = request.get_json()

    email = data.get("email")
    password = data.get("password")

    result = login_user(email, password)

    if "error" in result:
        return error_response(result["error"], 401)

    return success_response(
        "Login successful",
        {"token": result["token"]},
        200
    )