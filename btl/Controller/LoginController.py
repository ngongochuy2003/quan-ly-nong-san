from Dao.LoginDao import LoginDao

class LoginController:
    def __init__(self):
        self.dao = LoginDao()

    def get_user(self, username):
        return self.dao.get_user(username)



