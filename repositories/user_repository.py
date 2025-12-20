class UserRepository:
    def __init__(self):
        self.users = {}

    def create_user(self, username, hashed_password, email):
        self.users[username] = {
            'username': username,
            'password': hashed_password,
            'email': email
        }

    def get_user_by_username(self, username):
        return self.users.get(username)
