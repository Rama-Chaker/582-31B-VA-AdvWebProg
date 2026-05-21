class StudentRecord:
    def __init__(self, name, gpa, credits):
        if name == "":
            print("Invalid input for student record")
        else:
            self.name = name
        self.gpa = gpa
        self.credits = credits

    @property
    def gpa(self):
        return self.__gpa

    @gpa.setter
    def gpa(self, value):
        if 0.0 <= value <= 4.0:
            self.__gpa = value
        else:
            print("Invalid GPA value")

    @property
    def credits(self):
        return self.__credits

    @credits.setter
    def credits(self, value):
        if value >= 0:
            self.__credits = value
        else:
            print("Credits cannot be negative")

    def add_credits(self, amount):
        if amount > 0:
            self.__credits += amount
        else:
            print("Credits to add must be positive")

    def update_gpa(self, new_gpa):
        self.gpa = new_gpa

    def display_info(self):
        print(f"Name: {self.name}, GPA: {self.gpa}, Credits: {self.credits}")
