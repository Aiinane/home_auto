from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    
    link_one = "https://suninjuly.github.io/registration1.html"
    link_two = "https://suninjuly.github.io/registration2.html"

    
    browser = webdriver.Chrome()
    browser.get(link_two)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, "div.form-group.second_class:nth-child(2) > input.form-control.second:nth-child(2)")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CSS_SELECTOR, " div.form-group.third_class:nth-child(3) > input.form-control.third:nth-child(2)")
    input3.send_keys("t@m.com")    

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "[class = 'submit-submission']").click()
    
    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(3)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")

    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()