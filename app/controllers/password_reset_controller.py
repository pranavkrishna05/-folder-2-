from flask import Blueprint, request, jsonify
from app.services.password_reset_service import PasswordResetService
from app.repositories.user_repository import UserRepository
from app.repositories.password_reset_repository import PasswordResetRepository

password_reset_blueprint = Blueprint('password_reset', __name__)
password_reset_service = PasswordResetService(UserRepository(), PasswordResetRepository())

@password_reset_blueprint.route('/request_reset', methods=['POST'])
def request_reset():
    data = request.get_json()
    email = data.get('email')
    
    if not email:
        return jsonify({"message": "Email is required"}), 400
    
    try:
        token = password_reset_service.request_password_reset(email)
        return jsonify({"message": "Password reset token sent to email", "token": token}), 200
    except ValueError as e:
        return jsonify({"message": str(e)}), 400

@password_reset_blueprint.route('/reset_password', methods=['POST'])
def reset_password():
    data = request.get_json()
    token = data.get('token')
    new_password = data.get('new_password')
    
    if not token or not new_password:
        return jsonify({"message": "Token and new password are required"}), 400
    
    try:
        password_reset_service.reset_password(token, new_password)
        return jsonify({"message": "Password has been reset successfully"}), 200
    except ValueError as e:
        return jsonify({"message": str(e)}), 400