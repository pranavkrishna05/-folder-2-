from flask import Blueprint, request, jsonify
from app.services.profile_service import ProfileService
from app.repositories.user_repository import UserRepository

profile_blueprint = Blueprint('profile', __name__)
profile_service = ProfileService(UserRepository())

@profile_blueprint.route('/update', methods=['POST'])
def update_profile():
    data = request.get_json()
    user_id = data.get('user_id')
    email = data.get('email')
    password = data.get('password')
    
    if not user_id:
        return jsonify({"message": "User ID is required"}), 400
    
    try:
        user = profile_service.update_profile(user_id, email, password)
        return jsonify({"email": user.email, "date_updated": user.date_created}), 200
    except ValueError as e:
        return jsonify({"message": str(e)}), 400