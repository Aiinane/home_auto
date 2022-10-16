from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time 

link = "https://suninjuly.github.io/selects1.html"

browser = webdriver.Chrome()
browser.get(link)

try:
    x = browser.find_element(By.ID, "num1")
    y = browser.find_element(By.ID, "num2")
    x = x.text
    y = y.text
    my_sum = str(str(int(x)+int(y)))
    
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_visible_text(my_sum) 
    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    #Можно использовать еще два метода: select.select_by_visible_text("text") и select.select_by_index(index). Первый способ ищет элемент по видимому тексту, например, select.select_by_visible_text("Python") найдёт "Python" для нашего примера.


    # browser.find_element(By.TAG_NAME, "select").click()
    # browser.find_element(By.CSS_SELECTOR, "option:nth-child(2)").click()
    # #browser.find_element(By.CSS_SELECTOR, "[value='1']").click()
finally:
    time.sleep(10)
    browser.quit()