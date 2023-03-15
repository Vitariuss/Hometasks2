n = int(input())

if n % 3 != 0:
    print("wrong number")
else:
    a = b = n / 6

    a = int(a)
    b = int(b)

    c = a * 4

    print("first two children have", a, "each and the girl has", c)
