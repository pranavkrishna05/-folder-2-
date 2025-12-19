
from repositories.user import UserRepository

class AuthenticationService:
    @staticmethod
    def authenticate(username, password):
        user = UserRepository.get_user_by_id(1)
        return user is not None and user.username == username and password == 'password'
