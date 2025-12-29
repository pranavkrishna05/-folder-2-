"""
Authentication Controller handling user login and session management.
"""

from flask import request, jsonify, Blueprint
from auth.services.user_service import UserService
from auth.services.session_service import SessionService

auth_controller = Blueprint("auth_controller", __name__)
user_service = UserService()
session_service = SessionService()

@auth_controller.route("/login", methods=["POST"])
def login():
    """
    Endpoint to authenticate user credentials and initiate a session.
    """
    data = request.json
    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"error": "Email and password are required"}), 400

    user = user_service.authenticate_user(email, password)
    if user:
        session_token = session_service.create_session(user.id)
        return jsonify({"message": "Login successful", "session_token": session_token}), 200

    return jsonify({"error": "Invalid credentials"}), 401

@auth_controller.route("/logout", methods=["POST"])
def logout():
    """
    Endpoint to terminate user sessions.
    """
    data = request.json
    session_token = data.get("session_token")

    if not session_token:
        return jsonify({"error": "Session token is required"}), 400

    if session_service.invalidate_session(session_token):
        return jsonify({"message": "Logout successful"}), 200

    return jsonify({"error": "Invalid session token"}), 401