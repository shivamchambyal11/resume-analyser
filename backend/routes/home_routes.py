from flask import Blueprint
from controllers.home_controller import home, health
from middleware.auth_middleware import token_required

home_bp = Blueprint("home", __name__, url_prefix="/api/v1")

@home_bp.route("/")
def home_route():
    return home()

@home_bp.route("/health")
def health_route():
    return health()

@home_bp.route("/profile")
@token_required
def profile():
    return {
        "message": "Welcome to protected route"
    }

@home_bp.route("/")
def home():
    return {
        "message": "Resume Analyzer Backend is Running 🚀"
    }