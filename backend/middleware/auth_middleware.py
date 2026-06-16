from functools import wraps
from flask import request, jsonify

from utils.jwt_utils import verify_token


def token_required(f):

    @wraps(f)
    def decorated(*args, **kwargs):

        token = request.headers.get("Authorization")

        if not token:
            return jsonify({"message": "Token Missing"}), 401

        token = token.replace("Bearer ", "")

        payload = verify_token(token)

        if not payload:
            return jsonify({"message": "Invalid Token"}), 401

        return f(*args, **kwargs)

    return decorated