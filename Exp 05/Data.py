f = open("Data.py", "r")
print(f.read())
f.close()

f = open("data1.txt", "w")
f.write("Hello Siddhesh")
f.close()

f = open("data2.txt", "a")
f.write("My Name is Siddhesh")
f.close()

f = open("data2.txt", "r+")
print(f.read())
f.write("How Are You?")
f.close()

f = open("data4.txt", "a+")
f.write("DYPCET_TY_CSE_A_67")
f.seek(0)
print(f.read())
f.close()

f = open("data5.txt", "x")
f.write("HELLO WORLD")
f.close()

with open("data5.txt", "r") as f:
    data = f.read()
    print(data)