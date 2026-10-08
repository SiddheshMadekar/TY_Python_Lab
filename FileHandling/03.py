file = open("student.txt", "a")

name = input("Enter student's name: ")
roll_no = input("Enter roll number: ")
branch = input("Enter branch: ")
semester = input("Enter semester: ")

file.write("\nName: " + name)
file.write("\nRoll Number: " + roll_no)
file.write("\nBranch: " + branch)
file.write("\nSemester: " + semester)

file.close()

print("Information appended successfully.")