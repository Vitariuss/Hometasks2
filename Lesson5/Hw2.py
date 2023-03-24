def sum(a, b):
    if b == 0:
        return a
    else:
        return sum(a + 1, b - 1)

a = int(input("Write a: "))
b = int(input("Write b: "))

result = sum(a, b)

print(a, '+', b, '=', result) 