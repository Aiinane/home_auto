# from selenium import webdriver
# browser = webdriver.Chrome()
# #browser.execute_script("alert('Robots at work');")
# #browser.execute_script("document.title='Script executing';")
# browser.execute_script("document.title='Script executing';alert('Robots at work');")#Можно с помощью этого метода выполнить сразу несколько инструкций, перечислив их через точку с запятой. Изменим сначала заголовок страницы, а затем вызовем alert:

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

browser = webdriver.Chrome()
link = "https://suninjuly.github.io/alert_accept.html"
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser.get(link)
    submit = browser.find_element(By.CSS_SELECTOR,"[type='submit']").click()
    confirm = browser.switch_to.alert
    confirm.accept()
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)
    input = browser.find_element(By.TAG_NAME, "input")
    input.send_keys(y)
    submit = browser.find_element(By.CSS_SELECTOR,"[type='submit']").click()

# button = browser.find_element(By.TAG_NAME, "button")
# browser.execute_script("return arguments[0].scrollIntoView(true);", button)
# button.click()
finally:
    time.sleep(10)
    browser.quit()

# driver = webdriver.Chrome()
# driver.get("https://SunInJuly.github.io/execute_script.html")

# try:
#     button = driver.find_element_by_tag_name("button")
#     _ = button.location_once_scrolled_into_view

#    button.click()
#     assert True
# finally:
#     driver.quit() #можно справится без кода на Javascript. Для этого нужно использовать ActionChains:


# alert = browser.switch_to.alert
# alert.accept()
# Чтобы получить текст из alert, используйте свойство text объекта alert:

# alert = browser.switch_to.alert
# alert_text = alert.text
# Другой вариант модального окна, который предлагает пользователю выбор согласиться с сообщением или отказаться от него, называется confirm. Для переключения на окно confirm используется та же команда, что и в случае с alert:

# confirm = browser.switch_to.alert
# confirm.accept()
# Для confirm-окон можно использовать следующий метод для отказа:

# confirm.dismiss()
# То же самое, что и при нажатии пользователем кнопки "Отмена". 

# Третий вариант модального окна — prompt — имеет дополнительное поле для ввода текста. Чтобы ввести текст, используйте метод send_keys():

# prompt = browser.switch_to.alert
# prompt.send_keys("My answer")
# prompt.accept()