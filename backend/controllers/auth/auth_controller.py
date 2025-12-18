from flask import Blueprint, request, jsonify
from services.auth.auth_service import AuthService
from repositories.user_repository import UserRepository


auth_bp = Blueprint('auth', __name__)
service = AuthService(UserRepository())


@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    response = service.login(data['username'], data['password'])
    return jsonify({'message': response}), 200


@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    response = service.register(data['username'], data['password'])
    return jsonify({'message': response}), 201