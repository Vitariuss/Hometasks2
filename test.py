def power(a, b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    else:
        return a * power(a, b-1)

a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
c = int(input("Введите число c: "))
d = int(input("Введите число d: "))

result = power(c, d)
final_result = power(b, result)
final_result2 = power(a, final_result)
print(f"{a} в степени {b} в степени {c} в степени {d} равно {final_result2}")