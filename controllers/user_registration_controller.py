from flask import Blueprint, request, jsonify
from services.user_registration_service import UserRegistrationService

user_registration_controller = Blueprint('user_registration_controller', __name__)

@user_registration_controller.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')
    if not username or not password or not email:
        return jsonify({'error': 'Username, password, and email are required'}), 400
    user_registration_service = UserRegistrationService()
    try:
        user_registration_service.register_user(username, password, email)
        return jsonify({'message': 'User registered successfully'}), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400