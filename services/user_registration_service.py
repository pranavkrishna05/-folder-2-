import re
from repositories.user_repository import UserRepository

class UserRegistrationService:
    def __init__(self):
        self.user_repository = UserRepository()

    def register_user(self, username, password, email):
        if not self.is_valid_username(username):
            raise ValueError('Invalid username')
        if not self.is_valid_password(password):
            raise ValueError('Password does not meet criteria')
        if not self.is_valid_email(email):
            raise ValueError('Invalid email address')
        if self.user_repository.get_user_by_username(username):
            raise ValueError('Username already exists')
        self.user_repository.create_user(username, self.hash_password(password), email)

    @staticmethod
    def is_valid_username(username):
        return 3 <= len(username) <= 30

    @staticmethod
    def is_valid_password(password):
        return len(password) >= 8 and re.search(r'[A-Za-z]', password) and re.search(r'[0-9]', password)

    @staticmethod
    def is_valid_email(email):
        return re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email)

    @staticmethod
    def hash_password(password):
        # Implement your password hashing logic here
        return password