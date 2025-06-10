from collections import defaultdict

class School:

    def __init__(self, name):
        self.school_name = name
        self.classes = []
        self.teachers = defaultdict(list)
        self.students = []

    def add_class(self, class_name: str):
        print(f"Adding class, {class_name}")
        return self.classes.append(class_name)
            

    def add_teacher(self, teacher, subject):
        print(f"Adding teacher and subject")
        return self.teachers[subject].append(teacher) 
    
class Student(School):
    def __init__(self, name, school):
        super().__init__(school)
        self.student_name = name

primary_school = School("Mayfield")
primary_school.add_class("Maths")
for class_room in primary_school.classes:
    print(class_room)

primary_school.add_teacher("Jessel", "Python")
for subject, teachers in primary_school.teachers.items():
    for teacher in teachers:
        print(f"{teacher} teaches {subject}")

tilly = Student("Tilly", "Mayfield")
print(f"{tilly.school_name} goes to {tilly.school_name}")

# Why is this a bad example of inheritance? Hint - what does it imply about the class Student?