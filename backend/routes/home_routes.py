from flask import Blueprint
from controllers.home_controller import home, health

home_bp = Blueprint("home", __name__)

home_bp.route("/")(home)
home_bp.route("/health")(health)