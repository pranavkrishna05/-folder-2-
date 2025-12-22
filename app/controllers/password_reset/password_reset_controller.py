"""
Controller for managing password reset requests.
"""

from flask import Blueprint, request, jsonify
from app.config.db_config import get_db_session
from app.repositories.user_repository import UserRepository
from app.repositories.password_reset_repository import PasswordResetRepository
from app.services.password_reset_service import PasswordResetService

password_reset_bp = Blueprint("password_reset", __name__)

@password_reset_bp.route("/request-reset", methods=["POST"])
def request_password_reset():
    """
    Endpoint to request a password reset link.

    Returns:
        JSON: Success or error response.
    """
    data = request.json
    email = data.get("email")

    if not email:
        return jsonify({"error": "Email is required"}), 400

    db_session = get_db_session()
    user_repository = UserRepository(db_session)
    password_reset_repository = PasswordResetRepository(db_session)
    password_reset_service = PasswordResetService(user_repository, password_reset_repository)

    response = password_reset_service.create_password_reset_request(email=email)
    db_session.close()

    status_code = 200 if "message" in response else 404
    return jsonify(response), status_code

@password_reset_bp.route("/verify-reset-token", methods=["POST"])
def verify_reset_token():
    """
    Endpoint to verify a password reset token.

    Returns:
        JSON: Success or error response.
    """
    data = request.json
    token = data.get("token")

    if not token:
        return jsonify({"error": "Token is required"}), 400

    db_session = get_db_session()
    password_reset_repository = PasswordResetRepository(db_session)
    password_reset_service = PasswordResetService(None, password_reset_repository)

    response = password_reset_service.verify_password_reset_token(token=token)
    db_session.close()

    status_code = 200 if "message" in response else 400
    return jsonify(response), status_code