import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)

# Change page
button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

browser.switch_to.alert.accept()

# Calculate y from x obtained from "valuex" attribute of the image
input_value = browser.find_element(By.ID, "input_value")
x = input_value.text
output = calc(x)

# Send calculated y to textarea
textarea = browser.find_element(By.ID, "answer")
textarea.send_keys(output)

# Submit answer
button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

time.sleep(5)
browser.quit()