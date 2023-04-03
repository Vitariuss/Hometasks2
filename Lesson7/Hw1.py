poem = input("Введите стихотворение: ")
words = poem.split()
syl = []

for word in words:
    count = 0
    for letter in word:
        if letter in "аеиоуыэюя":
            count += 1
    syl.append(count)

if syl.count(syl[0]) == len(syl):
    print("Парам пам-пам")
else:
    print("Пам парам")
