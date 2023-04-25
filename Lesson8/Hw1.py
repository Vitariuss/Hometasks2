import os


def menu():
    print("1. Вывести данные")
    print("2. Добавить запись")
    print("3. Найти запись")
    print("4. Изменить запись")
    print("5. Удалить запись")
    print("6. Сохранить данные в файл")
    print("7. Загрузить данные из файла")
    print("8. Выход")


def output_data(data):
    for entry in data:
        print(', '.join(str(value) for value in entry))


def add_entry(data):
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    middle_name = input("Введите отчество: ")
    phone_number = input("Введите номер телефона: ")
    data.append((last_name, first_name, middle_name, phone_number))


def find_entry(data):
    search = input("Введите фамилию, либо имя, либо отчество, либо телефон: ")
    found = [entry for entry in data if search in entry]
    output_data(found)


def modify_entry(data):
    search = input("Введите фамилию, либо имя, либо отчество, либо телефон: ")
    found = [entry for entry in data if search in entry]
    if not found:
        print("Запись не найдена")
        return
    output_data(found)
    index = int(input("Введите номер записи для изменения: ")) - 1
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    middle_name = input("Введите отчество: ")
    phone_number = input("Введите номер телефона: ")
    data[data.index(found[index])] = (
        last_name, first_name, middle_name, phone_number)


def delete_entry(data):
    search = input("Введите фамилию, либо имя, либо отчество, либо телефон: ")
    found = [entry for entry in data if search in entry]
    if not found:
        print("Запись не найдена")
        return
    output_data(found)
    index = int(input("Введите номер записи для удаления: ")) - 1
    data.remove(found[index])


def save_data_to_file(data):
    file_name = input("Введите имя файла: ") + ".txt"
    with open(file_name, "w", encoding="utf-8") as f:
        for entry in data:
            f.write(', '.join(str(value) for value in entry) + "\n")


def load_data_from_file():
    file_name = input("Введите имя файла: ") + ".txt"
    if not os.path.isfile(file_name):
        print("Файл не найден")
        return []
    data = []
    with open(file_name, "r", encoding="utf-8") as f:
        for line in f:
            last_name, first_name, middle_name, phone_number = line.strip().split(', ')
            data.append((last_name, first_name, middle_name, phone_number))
    return data


def main():
    data = []
    while True:
        menu()
        choice = int(input("Выберите действие: "))
        if choice == 1:
            output_data(data)
        elif choice == 2:
            add_entry(data)
        elif choice == 3:
            find_entry(data)
        elif choice == 4:
            modify_entry(data)
        elif choice == 5:
            delete_entry(data)
        elif choice == 6:
            save_data_to_file(data)
        elif choice == 7:
            data = load_data_from_file()
        elif choice == 8:
            break
        else:
            print("Неверный ввод, пожалуйста, выберите действие из списка")


if __name__ == "__main__":
    main()
