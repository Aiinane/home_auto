import os 
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "https://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
    input2.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, "[name='email']")
    input2.send_keys("Ivan@m.com")
    button = browser.find_element(By.CSS_SELECTOR,"[type='file']")
    file_path = os.path.join('C:\уеба\\new.txt')
    button.send_keys(file_path)
    submit = browser.find_element(By.CSS_SELECTOR,"[type='submit']").click()
finally:
    time.sleep(10)
    browser.quit()

# current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
# file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
#element.send_keys(file_path)