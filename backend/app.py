from flask import Flask
from config.config import Config
from routes.home_routes import home_bp
from database.mongodb import db
from routes.auth_routes import auth_bp
from routes.resume_routes import resume_bp
import os

from routes.auth_routes import auth_bp

app = Flask(__name__)
os.makedirs("uploads", exist_ok=True)
app.config.from_object(Config)


app.register_blueprint(home_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(resume_bp)
@app.route("/db-test")
def db_test():
    db.test.insert_one({"message": "MongoDB Connected"})
    return {"status": "MongoDB Connected Successfully"}

if __name__ == "__main__":
    app.run(debug=True)

@app.route("/")
def test():
    return "Backend Running 🚀"