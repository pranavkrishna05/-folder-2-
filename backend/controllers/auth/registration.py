# registration.py
from flask import request, jsonify
from flask.views import MethodView
from backend.models.user import User
from backend.repositories.user_repository import UserRepository
from backend.services.auth_service import AuthService

class RegisterAPI(MethodView):
    def post(self):
        data = request.get_json()
        user_repository = UserRepository()
        auth_service = AuthService(user_repository)
        user = auth_service.register_user(data)
        return jsonify(user.to_dict()), 201
