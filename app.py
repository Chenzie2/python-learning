# from pprint import pprint as pp

class MoringaStudent:
    def __init__(self, first_name, last_name, course, cohort, tm):
        self.first_name = first_name
        self.last_name = last_name
        self.course = course
        self.cohort = cohort
        self.tm = tm
        self.email = f"{first_name.lower()}.{last_name.lower()}@student.moringaschool.com"

# Create a student instance
student_1 = MoringaStudent("Grace", "Zawadi", "Software Engineering", "SDF-FT13/14", "Erick Mongare")
student_2 = MoringaStudent("Adrian", "Maduafokwa", "Electrical Engineering", "Year 1", "Temi Odulaju")
print(student_1.first_name)
print(student_1.course)
print(student_1.email)
print(student_2.first_name)
print(student_2.course)
print(student_2.email)

