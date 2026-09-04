class Student:
    def student_info(self):
        print("Name: Siddhesh")
        print("Roll No: 67")


class Academic(Student):
    def academic(self):
        print("Academic Result: Excellent")


class Sports(Student):
    def sports(self):
        print("Sports: Cricket")


a = Academic()
a.student_info()
a.academic()

print()

s = Sports()
s.student_info()
s.sports()