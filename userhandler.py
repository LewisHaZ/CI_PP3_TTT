from user_module import User


class UserHandler():
    def __init__(self, database):
        self.database = database

    def does_user_exist(self, email):
        return self.database.does_user_exist(email)

    def get_user(self, email):
        if self.does_user_exist(email):
            return self.database.get_user(email)
        return None

    def try_add_user(self, name, email):
        if self.does_user_exist(email):
            return False
        user = User(name, email)
        self.database.add_user(user)
        return True

    def try_update_user(self, user):
        if not self.does_user_exist(user.email):
            return False
        self.database.update_user(user)
        return True
    

