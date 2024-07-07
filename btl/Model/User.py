class User:
    def __init__(self, username, password, role, name, age, address, phone_number):
        self.username = username
        self.password = password
        self.role = role  # 'admin' or 'manager'
        self.name = name
        self.age = age
        self.address = address
        self.phone_number = phone_number

