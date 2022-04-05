import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

# Calculate y from x obtained from "valuex" attribute of the image
input_value = browser.find_element(By.ID, "treasure")
x = input_value.get_attribute("valuex")
output = calc(x)

# Send calculated y to textarea
textarea = browser.find_element(By.ID, "answer")
textarea.send_keys(output)

# Choose checkbox option
robot_check = browser.find_element(By.ID, "robotCheckbox")
robot_check.click()

# Choose one of the radiobuttons
robot_radio = browser.find_element(By.ID, "robotsRule")
robot_radio.click()

# Submit results
button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

time.sleep(5)
browser.quit()