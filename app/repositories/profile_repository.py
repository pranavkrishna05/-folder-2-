"""
Repository layer for profile data interactions.
"""

from app.models.profile import Profile, db


class ProfileRepository:
    """Provides Profile model-related database functionality."""

    @staticmethod
    def get_profile_by_user_id(user_id: int) -> Profile | None:
        """Retrieve a profile by user ID."""
        return Profile.query.filter_by(user_id=user_id).first()

    @staticmethod
    def create_profile(user_id: int, first_name: str = None, last_name: str = None, preferences: str = None) -> Profile:
        """Create and store a new profile."""
        profile = Profile(user_id=user_id, first_name=first_name, last_name=last_name, preferences=preferences)
        db.session.add(profile)
        db.session.commit()
        return profile

    @staticmethod
    def update_profile(profile_id: int, first_name: str = None, last_name: str = None, preferences: str = None) -> None:
        """Update an existing profile."""
        profile = Profile.query.get(profile_id)
        if profile:
            profile.update_profile(first_name=first_name, last_name=last_name, preferences=preferences)
            db.session.commit()