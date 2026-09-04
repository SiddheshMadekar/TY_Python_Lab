class Student:
    def student_info(self):
        print("Name: Siddhesh")
        print("Roll No: 67")


class Marks(Student):
    def marks(self):
        print("Maths: 85")
        print("Physics: 80")
        print("Computer: 90")


class Result(Marks):
    def percentage(self):
        total = 85 + 80 + 90
        percentage = total / 3
        print("Percentage:", percentage)


r = Result()

r.student_info()
r.marks()
r.percentage()