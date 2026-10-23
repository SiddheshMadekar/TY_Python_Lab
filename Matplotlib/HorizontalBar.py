import matplotlib.pyplot as plt

students = ["Rahul", "Amit", "Priya", "Sneha"]
marks = [75, 88, 92, 81]

plt.barh(students, marks)

plt.xlabel("Marks")
plt.ylabel("Students")
plt.title("Student Performance")

plt.show()
#Siddhesh_67