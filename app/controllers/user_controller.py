"""
User Controller: Handles user-related HTTP requests.
"""

from flask import Blueprint, request, jsonify
from app.services.user_service import UserService

user_bp = Blueprint('user', __name__)
user_service = UserService()

@user_bp.route('/register', methods=['POST'])
def register_user():
    """Register a new user via API call."""
    try:
        data = request.json
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            return jsonify({'error': 'Email and password are required'}), 400

        # Delegate to UserService
        user = user_service.register_user(email=email, password=password)
        return jsonify({'id': user.id, 'email': user.email}), 201

    except ValueError as e:
        return jsonify({'error': str(e)}), 400

    except Exception as e:
        return jsonify({'error': 'An unexpected error occurred'}), 500