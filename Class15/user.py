class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    def display_info(self):
        print(f"Name: {self.name}, Email: {self.email}")

class Customer(User):
    def __init__(self, name, email, customer_id):
        super().__init__(name, email)
        self.__customer_id = customer_id
    def display_info(self):
        super().display_info()
        print(f"Customer ID: {self.__customer_id}")

class Admin(User):
    def __init__(self, name, email, employee_id):
        super().__init__(name, email)
        self.__employee_id = employee_id
    def display_info(self):
        super().display_info()
        print(f"Employee ID: {self.__employee_id}")