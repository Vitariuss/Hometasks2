S = int(input("Write the sum of numbers: "))
P = int(input("Write the product of numbers: "))

x = y = 0

for i in range(1, S):
    if P % i == 0:
        j = P // i
        if i + j == S:
            x, y = i, j
            break

if x == 0 and y == 0:
    print("Fail")
else:
    print("First number is: ", x)
    print("Second number is: ", y)