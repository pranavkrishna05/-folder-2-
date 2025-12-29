"""
Password reset Controller handling password recovery process.
"""

from flask import request, jsonify, Blueprint
from auth.services.password_reset_service import PasswordResetService
from auth.services.email_service import EmailService

password_reset_controller = Blueprint("password_reset_controller", __name__)
password_reset_service = PasswordResetService()
email_service = EmailService()

@password_reset_controller.route("/password-reset/request", methods=["POST"])
def request_password_reset():
    """
    Endpoint to initiate a password reset request.
    """
    data = request.json
    email = data.get("email")

    if not email:
        return jsonify({"error": "Email is required"}), 400

    token = password_reset_service.create_reset_token(email)
    if token:
        email_service.send_password_reset_email(email, token)
        return jsonify({"message": "Password reset email sent"}), 200

    return jsonify({"error": "User not found"}), 404

@password_reset_controller.route("/password-reset/confirm", methods=["POST"])
def confirm_password_reset():
    """
    Endpoint to reset the password using the reset token.
    """
    data = request.json
    token = data.get("token")
    new_password = data.get("new_password")

    if not token or not new_password:
        return jsonify({"error": "Token and new password are required"}), 400

    if password_reset_service.reset_password(token, new_password):
        return jsonify({"message": "Password reset successful"}), 200

    return jsonify({"error": "Invalid or expired token"}), 400