"""
Controller layer for profile management routes.
"""

from flask import Blueprint, jsonify, request
from app.services.profile_service import ProfileService

profile_blueprint = Blueprint("profile", __name__, url_prefix="/profile")

@profile_blueprint.route("/view/<int:user_id>", methods=["GET"])
def view_profile(user_id: int):
    """Endpoint to view user profile."""
    try:
        profile_data = ProfileService.get_user_profile(user_id=user_id)
        if profile_data:
            return jsonify(profile_data), 200
        return jsonify({"error": "Profile not found"}), 404
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@profile_blueprint.route("/create", methods=["POST"])
def create_profile():
    """Endpoint to create a new user profile."""
    data = request.get_json()
    user_id = data.get("user_id")
    first_name = data.get("first_name")
    last_name = data.get("last_name")
    preferences = data.get("preferences")
    description = data.get("description")
    bio = data.get("bio")

    if not user_id:
        return jsonify({"error": "User ID is required"}), 400

    try:
        profile_data = ProfileService.create_user_profile(
            user_id=user_id,
            first_name=first_name,
            last_name=last_name,
            preferences=preferences,
            description=description,
            bio=bio,
        )
        return jsonify(profile_data), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@profile_blueprint.route("/update", methods=["PUT"])
def update_profile():
    """Endpoint to update an existing user profile."""
    data = request.get_json()
    user_id = data.get("user_id")
    first_name = data.get("first_name")
    last_name = data.get("last_name")
    preferences = data.get("preferences")
    description = data.get("description")
    bio = data.get("bio")

    if not user_id:
        return jsonify({"error": "User ID is required"}), 400

    try:
        updated_profile = ProfileService.update_user_profile(
            user_id=user_id,
            first_name=first_name,
            last_name=last_name,
            preferences=preferences,
            description=description,
            bio=bio,
        )
        return jsonify(updated_profile), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
