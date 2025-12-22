"""
Controller for managing authentication requests.
"""

from flask import Blueprint, request, jsonify
from app.config.db_config import get_db_session
from app.repositories.user_repository import UserRepository
from app.repositories.session_repository import SessionRepository
from app.services.authentication_service import AuthenticationService

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["POST"])
def login_user():
    """
    Endpoint to handle user login requests.

    Returns:
        JSON: Login success or error response.
    """
    data = request.json
    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"error": "Email and password are required"}), 400

    db_session = get_db_session()
    user_repository = UserRepository(db_session)
    session_repository = SessionRepository(db_session)
    auth_service = AuthenticationService(user_repository, session_repository)

    response = auth_service.authenticate_user(email=email, password=password)
    db_session.close()

    status_code = 200 if "message" in response else 401
    return jsonify(response), status_code