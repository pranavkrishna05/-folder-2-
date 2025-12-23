"""
Controller layer for user session routes.
"""

from flask import Blueprint, jsonify, request
from app.services.session_service import SessionService

session_blueprint = Blueprint("session", __name__, url_prefix="/session")


@session_blueprint.route("/login", methods=["POST"])
def login_user():
    """Endpoint for user login."""
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"error": "Email and password are required"}), 400

    try:
        session_data = SessionService.login_user(email=email, password=password)
        return jsonify(session_data), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 401


@session_blueprint.route("/validate", methods=["POST"])
def validate_session():
    """Endpoint to validate a session."""
    data = request.get_json()
    session_token = data.get("session_token")

    if not session_token:
        return jsonify({"error": "Session token is required"}), 400

    is_valid = SessionService.validate_session(session_token=session_token)
    if is_valid:
        return jsonify({"message": "Session is valid"}), 200
    return jsonify({"error": "Invalid or expired session"}), 403