class Student:
    def student_info(self):
        print("Name: Siddhesh")
        print("Roll No: 67")


class Sports:
    def sports_info(self):
        print("Sport: Cricket")


class Result(Student, Sports):
    def result(self):
        print("Result: Pass")


r = Result()

r.student_info()
r.sports_info()
r.result()