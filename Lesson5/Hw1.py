def power(a, b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    else:
        return a * power(a, b-1)

a = int(input("Write a: "))
b = int(input("Write b: "))

result = power(a, b)
print(f"{a} raised to the power of {b} is {result}")