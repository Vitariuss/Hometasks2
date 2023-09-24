transactions = []  
balance = 0  
transaction_count = 0  

def deposit(amount):
    global balance, transaction_count
    if balance >= 5000000:  
        amount -= amount * 0.1
    balance += amount
    transactions.append(("Пополнение", amount))
    transaction_count += 1
    if transaction_count % 3 == 0:  
        balance += balance * 0.03
    print("Текущий баланс:", balance)

def withdraw(amount):
    global balance, transaction_count
    if balance >= 5000000: 
        amount -= amount * 0.1
    if amount > balance:
        print("Ошибка: Недостаточно средств на счете.")
        return

    fee = amount * 0.015  
    if fee < 30:
        fee = 30
    elif fee > 600:
        fee = 600
    balance -= amount + fee
    transactions.append(("Снятие", amount))
    transaction_count += 1
    if transaction_count % 3 == 0:  
        balance += balance * 0.03
    print("Текущий баланс:", balance)

def print_transactions():
    print("История операций:")
    for transaction in transactions:
        print(transaction[0], "-", transaction[1])

def atm():
    global balance
    while True:
        print("\nДоступные действия:")
        print("1. Пополнить счет")
        print("2. Снять со счета")
        print("3. Вывести историю операций")
        print("4. Выйти")

        choice = input("Выберите действие (1-4): ")

        if choice == "1":
            amount = int(input("Введите сумму для пополнения (кратную 50): "))
            if amount % 50 != 0:
                print("Ошибка: Сумма должна быть кратной 50.")
                continue
            deposit(amount)
        elif choice == "2":
            amount = int(input("Введите сумму для снятия (кратную 50): "))
            if amount % 50 != 0:
                print("Ошибка: Сумма должна быть кратной 50.")
                continue
            withdraw(amount)
        elif choice == "3":
            print_transactions()
        elif choice == "4":
            break
        else:
            print("Ошибка: Неверный выбор. Попробуйте снова.")

atm()