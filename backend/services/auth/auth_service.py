from repositories.user_repository import UserRepository


class AuthService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    def login(self, username, password):
        user = self.user_repo.get_user(username)
        if user and user.check_password(password):
            return 'Logged in successfully'
        return 'Invalid credentials'

    def register(self, username, password):
        if not self.user_repo.get_user(username):
            self.user_repo.add_user(username, password)
            return 'Registered successfully'
        return 'User already exists'