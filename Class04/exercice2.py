class User:
    def __init__(self, username, password):
        self.username = username
        if len(password) < 4:
            print("Warning: Password is too short.")
        else:
            self.password = password

    def set_password(self, new_password):
        self.password = new_password
        if len(new_password) < 4:
            print("Warning: Password is too short.")
        else:
            print("Password updated successfully.")

user1 = User("john_doe", "1234")
user1.set_password("abc")
user1.set_password("new_secure_password")