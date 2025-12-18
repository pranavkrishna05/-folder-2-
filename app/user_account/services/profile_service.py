from app.user_account.infrastructure.repositories.profile_repository import ProfileRepository

class ProfileService:
    @staticmethod
    def update_profile(user_id: int, data: dict) -> None:
        ProfileRepository.update_profile(user_id, data)
