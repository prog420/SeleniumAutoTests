import time
from selenium import webdriver
from selenium.webdriver.common.by import By


# link = "http://suninjuly.github.io/registration1.html"
link = "http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Fill "required" fields
    fields = {
        "first_name": "first",
        "last_name": "second",
        "email": "third"
    }
    browser.find_element(By.CSS_SELECTOR, f'form input.{fields["first_name"]}[required]').send_keys("Dmitry")
    browser.find_element(By.CSS_SELECTOR, f'form input.{fields["last_name"]}[required]').send_keys("Ivanov")
    browser.find_element(By.CSS_SELECTOR, f'form input.{fields["email"]}[required]').send_keys("d.ivanov@mail.ru")

    time.sleep(2)

    # Send filled form
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Wait for page loading
    time.sleep(2)

    # Find welcome text
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    # Check for successful registration
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(4)
    # Close browser after all manipulations
    browser.quit()