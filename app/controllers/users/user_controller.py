"""
RESTful controller for user-related endpoints.
"""

from flask import Blueprint, request, jsonify
from sqlalchemy.orm import Session
from app.config.db_config import get_db_session
from app.repositories.user_repository import UserRepository
from app.services.user_service import UserService

user_bp = Blueprint("user", __name__)

@user_bp.route("/register", methods=["POST"])
def register_user():
    """
    Register a new user via a POST request.

    Returns:
        JSON response indicating success or errors.
    """
    data = request.json
    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"error": "Email and password are required"}), 400

    db_session: Session = get_db_session()
    user_repository = UserRepository(db_session)
    user_service = UserService(user_repository)

    response = user_service.register_user(email=email, password=password)
    db_session.close()
    
    status_code = 201 if "message" in response else 400
    return jsonify(response), status_code