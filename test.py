import random

def play_game(right):
    num = random.randint(1, right)
    print('Добро пожаловать в числовую угадайку')
    tries = 0
    while True:
        n = input("Введите число от 1 до {}: ".format(right))
        if n.isdigit() and 1 <= int(n) <= right:
            n = int(n)
            tries += 1
            if n > num:
                print('Ваше число больше загаданного, попробуйте еще разок')        
            elif n < num:
                print('Ваше число меньше загаданного, попробуйте еще разок')
            else:
                print('Вы угадали, поздравляем!')
                print('Количество попыток:', tries)
                break
        else:
            print('А может быть все-таки введем целое число от 1 до {}?'.format(right))

    return tries

def play_again():
    while True:
        choice = input("Хотите сыграть еще раз? (да/нет): ")
        if choice.lower() == 'да':
            return True
        elif choice.lower() == 'нет':
            return False
        else:
            print("Пожалуйста, ответьте 'да' или 'нет'.")

right = int(input("Введите правую границу для случайного выбора числа: "))
play_game(right)
while play_again():
    play_game(right)
    
print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
