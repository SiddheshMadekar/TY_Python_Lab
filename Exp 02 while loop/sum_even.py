#Print sum of Even No up to n
n = int(input("Enter a number: "))

sum = 0
i = 2

while i <= n:
    sum = sum + i
    i += 2

print("Sum of even numbers =", sum)