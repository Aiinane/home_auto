from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)
    # x_element = browser.find_element(By.ID, "input_value")
    # x = x_element.text
    # y = calc(x_element)
    input = browser.find_element(By.TAG_NAME, "input")
    browser.execute_script("return arguments[0].scrollIntoView(true);", input)
    #button.click()
    input.send_keys(y)
    button = browser.find_element(By.ID, "robotCheckbox").click()
    button = browser.find_element(By.ID, "robotsRule").click()
    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
finally:
    time.sleep(10)
    browser.quit()