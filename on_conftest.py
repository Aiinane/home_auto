import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

#     Теперь, сколько бы файлов с тестами мы ни создали, у тестов будет доступ к фикстуре browser. Фикстура передается в тестовый метод в качестве аргумента. Таким образом можно удобно переиспользовать одни и те же вспомогательные функции в разных частях проекта.


# test_conftest.py:

# from selenium.webdriver.common.by import By

# link = "http://selenium1py.pythonanywhere.com/"

# def test_guest_should_see_login_link(browser):
#     browser.get(link)
#     browser.find_element(By.CSS_SELECTOR, "#login_link")