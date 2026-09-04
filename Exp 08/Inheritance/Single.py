class Student:
    def display_student(self):
        print("Student Name: Siddhesh")
        print("Roll No: 67")


class Marks(Student):
    def display_marks(self):
        print("Maths: 85")
        print("Physics: 78")
        print("Computer: 90")


s = Marks()

s.display_student()
s.display_marks()