class Student:
    def student_info(self):
        print("Name: Siddhesh")


class Academic(Student):
    def academic(self):
        print("Academic: 85%")


class Sports(Student):
    def sports(self):
        print("Sports: Cricket")


class Result(Academic, Sports):
    def result(self):
        print("Final Result: Pass")


r = Result()

r.student_info()
r.academic()
r.sports()
r.result()