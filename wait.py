from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

# browser = webdriver.Chrome()
# # говорим WebDriver искать каждый элемент в течение 5 секунд
# browser.implicitly_wait(5)
# browser.get("https://suninjuly.github.io/cats.html")
# browser.find_element(By.ID, "button") 

#time.sleep(1)
# button = browser.find_element(By.ID, "verify").click()
# message = browser.find_element(By.ID, "verify_message")

# assert "successful" in message.text


# browser = webdriver.Chrome()


# browser.get("http://suninjuly.github.io/wait2.html")

# # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
# button = WebDriverWait(browser, 5).until(
#         EC.element_to_be_clickable((By.ID, "verify"))
#     )
# button.click()

# message = browser.find_element(By.ID, "verify_message")

# assert "successful" in message.text

# title_is
# title_contains
# presence_of_element_located
# visibility_of_element_located
# visibility_of
# presence_of_all_elements_located
# text_to_be_present_in_element
# text_to_be_present_in_element_value
# frame_to_be_available_and_switch_to_it
# invisibility_of_element_located
# element_to_be_clickable
# staleness_of
# element_to_be_selected
# element_located_to_be_selected
# element_selection_state_to_be
# element_located_selection_state_to_be
# alert_is_present
#https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.support.expected_conditions

# Если мы захотим проверять, что кнопка становится неактивной после отправки данных, то можно задать негативное правило с помощью метода until_not:

# # говорим Selenium проверять в течение 5 секунд пока кнопка станет неактивной
# button = WebDriverWait(browser, 5).until_not(
#         EC.element_to_be_clickable((By.ID, "verify"))
#     )

browser = webdriver.Chrome()
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser.get("http://suninjuly.github.io/explicit_wait2.html")

try:
    button = WebDriverWait(browser, 10).until(
            EC.text_to_be_present_in_element((By.ID, "price"),"100")
        )
    submit = browser.find_element(By.ID,"book").click()
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)
    input = browser.find_element(By.TAG_NAME, "input")
    input.send_keys(y)
    submit = browser.find_element(By.CSS_SELECTOR,"[type='submit']").click()

finally:
    time.sleep(10)
    browser.quit()

