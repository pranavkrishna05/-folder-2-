"""
Profile Controller handling user profile management.
"""

from flask import request, jsonify, Blueprint
from auth.services.profile_service import ProfileService

profile_controller = Blueprint("profile_controller", __name__)
profile_service = ProfileService()

@profile_controller.route("/profile", methods=["GET"])
def get_profile():
    """
    Endpoint to fetch user profile details.
    """
    user_id = request.args.get("user_id")
    
    if not user_id:
        return jsonify({"error": "User ID is required"}), 400
    
    profile = profile_service.get_profile(int(user_id))
    if profile:
        return jsonify(profile.dict()), 200

    return jsonify({"error": "Profile not found"}), 404

@profile_controller.route("/profile", methods=["PUT"])
def update_profile():
    """
    Endpoint to update user profile details.
    """
    data = request.json
    user_id = data.get("user_id")
    update_data = {key: value for key, value in data.items() if key != "user_id"}
    
    if not update_data or not user_id:
        return jsonify({"error": "User ID and at least one field to update are required"}), 400
    
    updated_profile = profile_service.update_profile(int(user_id), update_data)
    if updated_profile:
        return jsonify(updated_profile.dict()), 200

    return jsonify({"error": "Error updating profile"}), 400