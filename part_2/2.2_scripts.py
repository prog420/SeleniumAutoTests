import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

# Calculate y from x obtained from "valuex" attribute of the image
input_value = browser.find_element(By.ID, "input_value")
x = input_value.text
output = calc(x)

# Send calculated y to textarea
textarea = browser.find_element(By.ID, "answer")
textarea.send_keys(output)

# Choose checkbox option
robot_check = browser.find_element(By.ID, "robotCheckbox")
browser.execute_script("return arguments[0].scrollIntoView(true);", robot_check)
robot_check.click()

# Choose one of the radiobuttons
robot_radio = browser.find_element(By.ID, "robotsRule")
browser.execute_script("return arguments[0].scrollIntoView(true);", robot_radio)
robot_radio.click()

# Find button
button = browser.find_element(By.CSS_SELECTOR, "button.btn")
# Scroll page to see the button
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
# Submit results
button.click()

time.sleep(5)
browser.quit()