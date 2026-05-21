class CourseSection:
    def __init__(self, title, capacity, enrolled):
        if title == "":
            raise ValueError("Invalid input for course section")
        self.title = title
        self.capacity = capacity
        self.enrolled = enrolled

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value <= 0:
            raise ValueError("Capacity cannot be zero or negative")

        else:
            self.__capacity = value

    @property
    def enrolled(self):
        return self.__enrolled

    @enrolled.setter
    def enrolled(self, value):
        if value < 0:
            raise ValueError("Enrolled cannot be negative")
            if value > self.__capacity:
                raise ValueError("Enrolled cannot exceed capacity")
        else:
            self.__enrolled = value

    def register_students(self):
        if self.__enrolled < self.capacity:
            self.__enrolled += 1

    def drop_students(self):
        if self.__enrolled > 0:
            self.__enrolled -= 1
        else:
            raise ValueError("Cannot drop students, no students enrolled")

    def display_info(self):
        print(
            f"Course: {self.title}, Capacity: {self.capacity}, Enrolled: {self.enrolled}"
        )
