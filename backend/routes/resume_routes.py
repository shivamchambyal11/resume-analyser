from flask import Blueprint
from controllers.resume_controller import upload_resume
from middleware.auth_middleware import token_required

resume_bp = Blueprint(
    "resume",
    __name__,
    url_prefix="/api/v1/resume"
)

@resume_bp.route("/upload", methods=["POST"])
@token_required
def upload():
    return upload_resume()