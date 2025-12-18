from models.user import User


class UserRepository:
    def __init__(self):
        self.users = {}

    def add_user(self, username, password):
        user = User(username, password)
        self.users[username] = user

    def get_user(self, username):
        return self.users.get(username)