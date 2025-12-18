from app.database import db
from app.user_account.domain.entities.profile import Profile

class ProfileRepository:
    @staticmethod
    def update_profile(user_id: int, data: dict) -> None:
        profile = Profile.query.filter_by(user_id=user_id).first()
        if not profile:
            raise ValueError('Profile not found')
        for key, value in data.items():
            setattr(profile, key, value)
        db.session.commit()
