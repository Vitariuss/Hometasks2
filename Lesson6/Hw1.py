a1 = int(input("Write the first number "))
d = int(input("Write the difference "))
n = int(input("Write the number of elements "))

progr = [a1 + (i-1) * d for i in range(1, n+1)]

print("Here is your progression")
print(progr)
