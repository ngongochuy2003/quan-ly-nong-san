from Context.DBConnect import Database

class LoginDao:
    def __init__(self):
        self.db = Database()
        self.cursor = self.db.get_connection().cursor()

    def get_user(self, username):
        self.cursor.execute("SELECT username, pass, role FROM taikhoan "
                            "WHERE username=%s",
                            (username,))
        user = self.cursor.fetchone()
        if user is None:
            return None
        else:
            return user