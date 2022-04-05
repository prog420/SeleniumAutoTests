import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

num_1 = browser.find_element(By.ID, "num1")
num_2 = browser.find_element(By.ID, "num2")
result = str(int(num_1.text) + int(num_2.text))


# First approach.
# Use click to choose option
dropdown = browser.find_element(By.ID, "dropdown")
# browser.find_element(By.CSS_SELECTOR, 'select[id="dropdown"] > [value="50"]').click()

# Second approach.
# Use Select class to instantiate dropdown object
# Available options: 
# - select_by_value(x);
# - select_by_visible_text(x)
select = Select(dropdown)
select.select_by_value(result)

# Submit results
button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

time.sleep(5)
browser.quit()