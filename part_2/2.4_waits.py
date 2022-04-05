import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)


price = WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "$100")
)

browser.find_element(By.ID, "book").click()

# Calculate y from x obtained from "valuex" attribute of the image
input_value = browser.find_element(By.ID, "input_value")
x = input_value.text
output = calc(x)

# Send calculated y to textarea
textarea = browser.find_element(By.ID, "answer")
textarea.send_keys(output)

# Submit answer
button = browser.find_element(By.ID, "solve")
button.click()

time.sleep(5)
browser.quit()