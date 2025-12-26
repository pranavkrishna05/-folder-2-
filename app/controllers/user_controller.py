"""
Controller layer for user registration route.
"""

from flask import Blueprint, jsonify, request
from app.services.user_service import UserService
import re

user_blueprint = Blueprint("user", __name__, url_prefix="/user")

@user_blueprint.route("/register", methods=["POST"])
def register_user():
    """Endpoint for user account registration."""
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"error": "Email and password are required"}), 400

    # Enforce password requirements
    password_policy = r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
    if not re.match(password_policy, password):
        return jsonify({"error": "Password must be at least 8 characters long, contain at least one letter, one number, and one special character."}), 400

    try:
        user_data = UserService.register_user(email=email, password=password)
        return jsonify(user_data), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400