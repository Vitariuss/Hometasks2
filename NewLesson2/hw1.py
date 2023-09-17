def to_hex(num):
    hex_digits = "0123456789ABCDEF"
    if num == 0:
        return "0"
    hex_str = ""
    while num > 0:
        digit = num % 16
        hex_str = hex_digits[digit] + hex_str
        num //= 16
    return hex_str

number = int(input("Введите число: "))
print(to_hex(number))
print(hex(number)) # для проверки