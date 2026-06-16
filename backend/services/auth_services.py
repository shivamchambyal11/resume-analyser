import bcrypt
from models.user_models import users_collection
from utils.jwt_utils import generate_token


def register_user(name, email, password):
    # Check if user already exists
    existing_user = users_collection.find_one({"email": email})

    if existing_user:
        return {"error": "User already exists"}

    # Hash password
    hashed_password = bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt()
    )

    # Create user document
    user = {
        "name": name,
        "email": email,
        "password": hashed_password
    }

    # Save user
    users_collection.insert_one(user)

    return {"message": "User registered successfully"}

def login_user(email, password):
    user = users_collection.find_one({"email": email})

    if not user:
        return {"error": "Invalid email or password"}

    if not bcrypt.checkpw(password.encode("utf-8"), user["password"]):
        return {"error": "Invalid email or password"}

    token = generate_token(user["_id"])

    return {
        "message": "Login successful",
        "token": token
    }