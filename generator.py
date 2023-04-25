import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'

chars = ''

n = int(input('Введите количество паролей для генерации: '))
length = int(input('Введите длину пароля: '))
add_digit = input('Включить цифры? (д = да, н = нет) ').strip()
add_lowercase = input('Включить прописные буквы? (д = да, н = нет) ').strip()
add_uppercase = input('Включить строчные буквы? (д = да, н = нет) ').strip()
add_punctuation = input('Включить символы, такие как !#$%&*+-=?@^_? (д = да, н = нет) ').strip()
remove_badsymbols = input('Исключить символы il1Lo0O? (д = да, н = нет)').strip()

if add_digit.lower() == 'д':
    chars += digits

if add_lowercase.lower() == 'д':
    chars += lowercase_letters

if add_uppercase.lower() == 'д':
    chars += uppercase_letters

if add_punctuation.lower() == 'д':
    chars += punctuation

if remove_badsymbols.lower() == 'д':
    chars = chars.replace('i', '').replace('l', '').replace('1', '').replace('L', '').replace('o', '').replace('0', '').replace('O', '')

if not chars:
    print('Вы должны выбрать хотя бы один тип символов для включения в пароль')
    exit()

def generate_password(length, chars):
    password = ''
    for j in range(length):
        password += random.choice(chars)
    return password

passwords = []
for _ in range(n):
    password = generate_password(length, chars)
    passwords.append(password)
    print(password)