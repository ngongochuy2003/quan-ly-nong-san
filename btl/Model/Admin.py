from User import User
from Context.DBConnect import Database
class Admin(User):
    def __init__(self, username, password, name, age, address, phone_number):
        super().__init__(username, password, '1', name, age, address, phone_number)

    # Add any admin-specific methods here