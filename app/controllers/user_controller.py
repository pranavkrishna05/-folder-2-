from flask import Blueprint, request, jsonify
from app.services.user_service import UserService
from app.repositories.user_repository import UserRepository

user_blueprint = Blueprint('user', __name__)
user_service = UserService(UserRepository())

@user_blueprint.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({"message": "Email and password are required"}), 400
    
    try:
        user = user_service.register_user(email, password)
        return jsonify({"email": user.email, "date_created": user.date_created}), 201
    except ValueError as e:
        return jsonify({"message": str(e)}), 400