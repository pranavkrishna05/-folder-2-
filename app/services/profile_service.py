"""
Profile service: application layer for business logic.
"""

from app.repositories.profile_repository import ProfileRepository
from app.repositories.user_repository import UserRepository
from app.models.profile import Profile


class ProfileService:
    """Service layer to handle profile-related logic."""

    @staticmethod
    def get_user_profile(user_id: int) -> dict | None:
        """Retrieve the user's profile."""
        profile = ProfileRepository.get_profile_by_user_id(user_id)
        if profile:
            return {
                "profile_id": profile.id,
                "user_id": profile.user_id,
                "first_name": profile.first_name,
                "last_name": profile.last_name,
                "preferences": profile.preferences,
            }
        return None

    @staticmethod
    def create_user_profile(user_id: int, first_name: str = None, last_name: str = None, preferences: str = None) -> dict:
        """Create a new profile for the user."""
        user = UserRepository.get_user_by_id(user_id)
        if not user:
            raise ValueError("User not found")

        profile = ProfileRepository.create_profile(user_id=user.id, first_name=first_name, last_name=last_name, preferences=preferences)
        return {
            "profile_id": profile.id,
            "user_id": profile.user_id,
            "first_name": profile.first_name,
            "last_name": profile.last_name,
            "preferences": profile.preferences,
        }

    @staticmethod
    def update_user_profile(user_id: int, first_name: str = None, last_name: str = None, preferences: str = None) -> dict:
        """Update the user's profile."""
        profile = ProfileRepository.get_profile_by_user_id(user_id)
        if not profile:
            raise ValueError("Profile not found")

        ProfileRepository.update_profile(profile_id=profile.id, first_name=first_name, last_name=last_name, preferences=preferences)
        return {
            "profile_id": profile.id,
            "user_id": profile.user_id,
            "first_name": profile.first_name,
            "last_name": profile.last_name,
            "preferences": profile.preferences,
        }