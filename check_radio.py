from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time 

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "https://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.ID, "treasure")
    x_element = x_element.get_attribute("valuex")
    print(x_element)
    #x = x_element.text
    y = calc(x_element)
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    button = browser.find_element(By.ID, "robotCheckbox").click()
    button = browser.find_element(By.ID, "robotsRule").click()
    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    # people_radio = browser.find_element(By.ID, "peopleRule")
    # people_checked = people_radio.get_attribute("checked")
    # print("value of people radio: ", people_checked)
    # assert people_checked is not None, "People radio is not selected by default"

    # robots_radio = browser.find_element(By.ID, "robotsRule")
    # robots_checked = robots_radio.get_attribute("checked")
    # assert robots_checked is None
  #assert people_checked == "true", "People radio is not selected by default"
    
finally:
    time.sleep(10)
    browser.quit()