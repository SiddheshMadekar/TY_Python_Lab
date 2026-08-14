with open("data1.txt", "r") as f:
    data = f.read()
    print(data)


with open("data2.txt", "r") as f:
    print(f.readline())
    print(f.readline())


with open("data4.txt", "r") as f:
    lines = f.readlines()
    print(lines)