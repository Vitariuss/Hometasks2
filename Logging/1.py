import datetime
import logging

MONTH = {"января": 1, "февраля": 2, "марта": 3, "апреля": 4, "мая": 5, "июня": 6, "июля": 7, "августа": 8,
         "сентября": 9, "октября": 10, "ноября": 11, "декабря": 12, }
WEEKDAY = {"понедельник": 0, "вторник": 1, "среда": 2, "четверг": 3, "пятница": 4, "суббота": 5, "воскресенье": 6, }
logging.basicConfig(filename='logs.log', filemode='w', encoding='utf-8', level=logging.ERROR)


def print_date(str_day):
    try:
        num, weekday, month = str_day.split()
        num = int(num[:-2])
        weekday = WEEKDAY.get(weekday)
        month = MONTH.get(month)
        count = 0
        if weekday is None:
            raise ValueError(f'Неверное значение дня недели: {weekday}')
        if month is None:
            raise ValueError(f'Неверное значение месяца: {month}')
        for i in range(1, 32):
            temp_date = datetime.datetime(datetime.datetime.now().year, month, i)
            if temp_date.weekday() == weekday:
                count += 1
                if count == num:
                    return temp_date

        raise ValueError('Неверное значение даты')

    except ValueError as e:
        logging.error(f'Ошибка: {str(e)}')


print(print_date("1-й четверг марта"))