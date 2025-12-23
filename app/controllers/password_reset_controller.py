"""
Controller layer for password reset routes.
"""

from flask import Blueprint, jsonify, request
from app.services.password_reset_service import PasswordResetService

password_reset_blueprint = Blueprint("password_reset", __name__, url_prefix="/password_reset")


@password_reset_blueprint.route("/initiate", methods=["POST"])
def initiate_password_reset():
    """Endpoint to initiate password reset process."""
    data = request.get_json()
    email = data.get("email")

    if not email:
        return jsonify({"error": "Email is required"}), 400

    try:
        reset_data = PasswordResetService.initiate_password_reset(email=email)
        return jsonify(reset_data), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@password_reset_blueprint.route("/verify", methods=["POST"])
def verify_reset_token():
    """Endpoint to verify reset token."""
    data = request.get_json()
    reset_token = data.get("reset_token")

    if not reset_token:
        return jsonify({"error": "Reset token is required"}), 400

    is_valid = PasswordResetService.verify_reset_token(reset_token=reset_token)
    if is_valid:
        return jsonify({"message": "Reset token is valid"}), 200
    return jsonify({"error": "Invalid or expired reset token"}), 403


@password_reset_blueprint.route("/reset", methods=["POST"])
def reset_password():
    """Endpoint to reset the user's password."""
    data = request.get_json()
    reset_token = data.get("reset_token")
    new_password = data.get("new_password")

    if not reset_token or not new_password:
        return jsonify({"error": "Reset token and new password are required"}), 400

    try:
        PasswordResetService.reset_password(reset_token=reset_token, new_password=new_password)
        return jsonify({"message": "Password reset successfully"}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400