from flask import Blueprint, request, jsonify, g
from app.user_account.services.profile_service import ProfileService

profile_bp = Blueprint('profile', __name__, url_prefix='/api/v1/profile')

@profile_bp.route('/update', methods=['POST'])
def update_profile():
    user_id = g.user.id if g.user else None
    if not user_id:
        return jsonify({'error': 'User must be logged in to update profile'}), 403

    data = request.json
    try:
        ProfileService.update_profile(user_id, data)
        return jsonify({'message': 'Profile updated successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
