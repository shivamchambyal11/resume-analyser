from flask import request
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def save_resume():

    if "resume" not in request.files:
        return {"message": "No file uploaded"}, 400

    file = request.files["resume"]

    if file.filename == "":
        return {"message": "No file selected"}, 400

    filename = secure_filename(file.filename)

    filepath = os.path.join(UPLOAD_FOLDER, filename)

    file.save(filepath)

    return {
        "message": "Resume uploaded successfully",
        "filename": filename
    }, 201