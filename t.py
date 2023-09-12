import time
from pywinauto.application import Application

import random

# Запускаем приложение (предполагается, что оно уже запущено)
app = Application().connect(title_re=".*DeadByDaylight.*")

# Получаем окно приложения
window = app.window(title_re=".*DeadByDaylight.*")

while True:
    # Проверяем, что окно не свернуто
    if window.is_visible() and not window.is_minimized():
        # Устанавливаем фокус на окно
        window.set_focus()
        # Передаем рандомное нажатие клавиши W, S, A или D
 
        # Ждем 1 секунду перед следующим нажатием
        time.sleep(5)
    else:
        # Если окно свернуто, ждем немного и проверяем снова
        time.sleep(1)