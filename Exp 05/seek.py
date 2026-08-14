with open("data5.txt", "r") as f:
    print(f.tell())
    print(f.read(5))
    print(f.tell())

with open("data5.txt", "r") as f:
    print(f.read(5))

    f.seek(0)

    print(f.read(5))
    