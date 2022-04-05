import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

# Fill required fields
browser.find_element(By.NAME, "firstname").send_keys("Dmitry")
browser.find_element(By.NAME, "lastname").send_keys("Ivanov")
browser.find_element(By.NAME, "email").send_keys("d.ivanov@mail.ru")

filename = "file.txt"
with open(filename, "w") as file:
    file.write("example")
root_dir = os.path.abspath(os.path.dirname(__file__))
path_to_file = os.path.join(root_dir, filename)
# Send path to file to field
file = browser.find_element(By.ID, "file")
file.send_keys(path_to_file)

# Find button
button = browser.find_element(By.CSS_SELECTOR, "button.btn")
# Scroll page to see the button
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
# Submit results
button.click()

time.sleep(5)
browser.quit()