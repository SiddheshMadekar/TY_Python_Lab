class Student:

    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        print("Constructor called")
        print("Student Name:", self.name)
        print("Roll No:", self.roll_no)

    def __del__(self):
        print("Destructor called")
        print("Student object destroyed")


s1 = Student("Siddhesh", 67)

del s1