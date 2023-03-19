n = int(input("Write your number: "))
x = 1
i = 0

while x <= n:
    print("2 ^", i, "is", x)
    x *= 2 
    i += 1

print("that's all, you have", i, "numbers")