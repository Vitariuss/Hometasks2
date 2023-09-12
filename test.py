import time
from pywinauto.application import Application
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
import random

# Запускаем приложение (предполагается, что оно уже запущено)
app = Application().connect(title_re=".*DeadByDaylight.*")

# Получаем окно приложения
window = app.window(title_re=".*DeadByDaylight.*")

keyboard = KeyboardController()
mouse = MouseController()

while True:
    # Проверяем, что окно не свернуто
    if window.is_visible() and not window.is_minimized():
        # Устанавливаем фокус на окно
        window.set_focus()
        # Передаем рандомное нажатие клавиши W, S, A или D
        key = random.choice(['w', 's', 'a', 'd'])
        keyboard.press(key)
        time.sleep(1)  # Держим нажатой клавишу 1 секунду
        keyboard.release(key)
        # Имитируем взмах мыши
        mouse.move(random.randint(-50, 50), random.randint(-50, 50))
        # Имитируем нажатие левой кнопки мыши
        mouse.click(Button.left, 1)
        # Ждем 1 секунду перед следующим нажатием
        time.sleep(5)
    else:
        # Если окно свернуто, ждем немного и проверяем снова
        time.sleep(1)