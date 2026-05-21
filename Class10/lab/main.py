from student_record import StudentRecord
from course_section import CourseSection


# VALID TESTS

print("=== Valid StudentRecord ===")

student1 = StudentRecord("Rama", 3.7, 30)

student1.display_info()

student1.add_credits(3)
student1.update_gpa(3.9)

student1.display_info()


print("\n=== Valid CourseSection ===")

course1 = CourseSection("Python Programming", 2, 1)

course1.display_info()

course1.register_students()

course1.display_info()

course1.drop_students()

course1.display_info()


# INVALID TESTS

print("\n=== Invalid Tests ===")

# Invalid GPA
try:
    student2 = StudentRecord("Ali", 5.0, 20)
except ValueError as e:
    print("Error:", e)

# Negative credits
try:
    student3 = StudentRecord("Sara", 3.2, -5)
except ValueError as e:
    print("Error:", e)

# Empty title
try:
    course2 = CourseSection("", 30, 10)
except ValueError as e:
    print("Error:", e)

# Capacity = 0
try:
    course3 = CourseSection("Math", 0, 0)
except ValueError as e:
    print("Error:", e)

# Enrolled > capacity
try:
    course4 = CourseSection("Science", 2, 5)
except ValueError as e:
    print("Error:", e)

# Register beyond capacity
try:
    full_course = CourseSection("History", 1, 1)
    full_course.register_students()
except ValueError as e:
    print("Error:", e)

# Drop below 0
try:
    empty_course = CourseSection("Physics", 5, 0)
    empty_course.drop_students()
except ValueError as e:
    print("Error:", e)