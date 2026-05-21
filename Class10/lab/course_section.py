class CourseSection:
    def __init__(self, title, capacity, enrolled):
        if title == "":
            print("Invalid input for course section")
        self.title = title
        self.capacity = capacity
        self.enrolled = enrolled

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value > 0:
            self.__capacity = value
        else:
            print("Capacity cannot be zero or negative")

    @property
    def enrolled(self):
        return self.__enrolled

    @enrolled.setter
    def enrolled(self, value):
        if value >= 0 and value <= self.__capacity:
            self.__enrolled = value
        else:
            print("Invalid enrollment number")

    def register_students(self):
        if self.__enrolled < self.__capacity:
            self.__enrolled += 1

    def drop_students(self):
        if self.__enrolled > 0:
            self.__enrolled -= 1
        else:
            print("Cannot drop students, no students enrolled")

    def display_info(self):
        print(
            f"Course: {self.title}, Capacity: {self.capacity}, Enrolled: {self.enrolled}"
        )
