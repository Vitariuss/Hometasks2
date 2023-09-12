number = 0
while number < 2 or number > 100000:
    number = int(input("Введите число от 2 до 100 000: "))
    if number < 2:
        print("Неверное число. Введите число от 2 до 100 000.")
    elif number > 100000:
        print("Неверное число. Введите число от 2 до 100 000.")

is_prime = True

for i in range(2, number):
    if number % i == 0:
        is_prime = False
        break

if is_prime:
    print("Число", number, "является простым") 
else:
    print("Число", number ,"является составным")