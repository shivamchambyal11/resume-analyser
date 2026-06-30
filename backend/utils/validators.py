import re


def validate_register(data):

    required_fields = ["name", "email", "password"]

    for field in required_fields:
        if field not in data or not data[field]:
            return f"{field} is required"

    email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    if not re.match(email_regex, data["email"]):
        return "Invalid email format"

    if len(data["password"]) < 6:
        return "Password must be at least 6 characters"

    return None