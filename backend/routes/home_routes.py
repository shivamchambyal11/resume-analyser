from flask import Blueprint
from controllers.home_controller import home, health
from middleware.auth_middleware import token_required

home_bp = Blueprint("home", __name__)

home_bp.route("/")(home)
home_bp.route("/health")(health)

@home_bp.route("/profile")
@token_required
def profile():

    return {
        "message": "Welcome to protected route"
    }