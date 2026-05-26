from course import Course
from status import CourseStatus
from course import DeliveryMode

try:
    bad_course = Course("Bad Course", 20, "open")
except ValueError as e:
    print("Error:", e)
course1 = Course("Advanced Programming", 30, CourseStatus.OPEN, DeliveryMode.ONLINE)
course2 = Course("Web Interface Programming 2", 25, CourseStatus.CLOSED, DeliveryMode.IN_PERSON)

course1.display_info()
course2.display_info()

course1.close_registration()
course1.display_info()

course2.reopen_course()
course2.display_info()


#Reflection answers:
#1. Constant values when defined cannot be changed.The enum is used to define a set of named constants where we can choose the value we want when doing the program.
#2. They are safer because they restrict inputs to a predefined set of valid options so we avoid typos.
#3. Because the value is already typed so we have only to choose what we want without thinking of any typos or something.
#4. We used a property for status because it is a private attribute so we needed that property to be able to access it.
#5. By restricting variable values to a predefined not changeable set of constants.