import time
from selenium import webdriver

# Инициализируем драйвер браузера. После этой команды вы должны
# увидеть новое открытое окно браузера
driver = webdriver.Chrome()

# Пауза в 5 секунд чтобы увидеть что происходит в браузере

# Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
driver.get("https://stepik.org/lesson/25969/step/12")
time.sleep(5)

# Находим нужный элемент на сайте через метод find_element_by_css_selector
# Ищем поле для ввода текста
textarea = driver.find_element_by_css_selector(".textarea")

# Напишем текста ответа в найденное поле
textarea.send_keys("get()")

# Найдем кнопку, которая отправляет введённое решение
submit_button = driver.find_element_by_css_selector(".submit-submission")

# Сообщаем драйверу, что нужно нажать на кнопку.
submit_button.click()
time.sleep()

# Не забываем закрыть окно браузера
driver.quit()