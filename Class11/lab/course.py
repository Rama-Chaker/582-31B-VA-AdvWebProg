from enum import Enum

from status import CourseStatus

class Course:
    MAX_CAPACITY = 60
    def __init__(self, title, capacity, status, delivery_mode):
        if not isinstance(status, CourseStatus):
            raise ValueError("status must be a CourseStatus value")
        if not isinstance(delivery_mode, DeliveryMode):
            raise ValueError("delivery_mode must be a DeliveryMode value")
        self.title = title
        self.capacity = min(capacity, self.MAX_CAPACITY)
        self.status = status
        self.delivery_mode = delivery_mode

    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self, new_status):
        if not isinstance(new_status, CourseStatus):
            raise ValueError("status must be a CourseStatus value")
        self.__status = new_status
    @property
    def delivery_mode(self):
        return self.__delivery_mode
    @delivery_mode.setter
    def delivery_mode(self, new_mode):
        if not isinstance(new_mode, DeliveryMode):
            raise ValueError("delivery_mode must be a DeliveryMode value")
        self.__delivery_mode = new_mode
    def display_info(self):
        print(f"{self.title} | Capacity: {self.capacity} | Status: {self.__status.value} | Delivery Mode: {self.delivery_mode.value}")

    def close_registration(self):
        self.status = CourseStatus.CLOSED
    def cancel_course(self):
        self.status = CourseStatus.CANCELLED
    def reopen_course(self):
        self.status = CourseStatus.OPEN

class DeliveryMode(Enum):
    ONLINE = "online"
    IN_PERSON = "in_person"
    HYBRID = "hybrid"