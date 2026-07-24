#Print sum of Odd No up to n
n = int(input("Enter a number: "))

sum = 0
i = 1

while i <= n:
    sum = sum + i
    i += 2

print("Sum of odd numbers =", sum)