from flask import Blueprint, request, jsonify
from app.user_account.services.user_service import UserService
import logging
import re

user_bp = Blueprint('user', __name__, url_prefix='/api/v1/users')

logger = logging.getLogger(__name__)

EMAIL_REGEX = r'^\S+@\S+\.\S+$'
PASSWORD_MIN_LENGTH = 8
PASSWORD_REGEX = r'^(?=.*[a-zA-Z])(?=.*\d).{' + str(PASSWORD_MIN_LENGTH) + ',}$'

@user_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    if not email or not re.match(EMAIL_REGEX, email):
        return jsonify({'error': 'Invalid email address'}), 400

    if not password or not re.match(PASSWORD_REGEX, password):
        return jsonify({'error': f'Password must be at least {PASSWORD_MIN_LENGTH} characters long and contain both letters and numbers'}), 400

    try:
        UserService.register_user(email, password)
        return jsonify({'message': 'User registered successfully'}), 201
    except Exception as e:
        logger.error(f'Error registering user: {e}')
        return jsonify({'error': str(e)}), 500
