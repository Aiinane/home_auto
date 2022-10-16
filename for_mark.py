import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1():

    @pytest.mark.smoke
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    @pytest.mark.regression
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")

# Чтобы запустить тест с нужной маркировкой, нужно передать в командной строке параметр -m и нужную метку:

# pytest -s -v -m smoke test_fixture8.py

# Как же регистрировать метки?
# Создайте файл pytest.ini в корневой директории вашего тестового проекта и добавьте в файл следующие строки:

# [pytest]
# markers =
#     smoke: marker for smoke tests
#     regression: marker for regression tests
# Текст после знака ":" является поясняющим — его можно не писать.

# Инверсия
# Чтобы запустить все тесты, не имеющие заданную маркировку, можно использовать инверсию. Для запуска всех тестов, не отмеченных как smoke, нужно выполнить команду:

# pytest -s -v -m "not smoke" test_fixture8.py


# Инверсия
# Чтобы запустить все тесты, не имеющие заданную маркировку, можно использовать инверсию. Для запуска всех тестов, не отмеченных как smoke, нужно выполнить команду:

# pytest -s -v -m "not smoke" test_fixture8.py
# Объединение тестов с разными маркировками
# Для запуска тестов с разными метками можно использовать логическое ИЛИ. Запустим smoke и regression-тесты:

# pytest -s -v -m "smoke or regression" test_fixture8.py
# Выбор тестов, имеющих несколько маркировок
# Предположим, у нас есть smoke-тесты, которые нужно запускать только для определенной операционной системы, например, для Windows 10. Зарегистрируем метку win10 в файле pytest.ini, а также добавим к одному из тестов эту метку.

# pytest.ini:

# [pytest]
# markers =
#     smoke: marker for smoke tests
#     regression: marker for regression tests
#     win10
# test_fixture81.py:

# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By

# link = "http://selenium1py.pythonanywhere.com/"


# @pytest.fixture(scope="function")
# def browser():
#     print("\nstart browser for test..")
#     browser = webdriver.Chrome()
#     yield browser
#     print("\nquit browser..")
#     browser.quit()


# class TestMainPage1:

#     @pytest.mark.smoke
#     def test_guest_should_see_login_link(self, browser):
#         browser.get(link)
#         browser.find_element(By.CSS_SELECTOR, "#login_link")

#     @pytest.mark.smoke
#     @pytest.mark.win10
#     def test_guest_should_see_basket_link_on_the_main_page(self, browser):
#         browser.get(link)
#         browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")

# Чтобы запустить только smoke-тесты для Windows 10, нужно использовать логическое И:

# pytest -s -v -m "smoke and win10" test_fixture81.py


# Итак, чтобы пропустить тест, его отмечают в коде как @pytest.mark.skip:

# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By

# link = "http://selenium1py.pythonanywhere.com/"

# @pytest.fixture(scope="function")
# def browser():
#     print("\nstart browser for test..")
#     browser = webdriver.Chrome()
#     yield browser
#     print("\nquit browser..")
#     browser.quit()


# class TestMainPage1():

#     @pytest.mark.skip
#     def test_guest_should_see_login_link(self, browser):
#         browser.get(link)
#         browser.find_element(By.CSS_SELECTOR, "#login_link")

#     def test_guest_should_see_basket_link_on_the_main_page(self, browser):
#         browser.get(link)
#         browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")


# Отметить тест как падающий

# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By

# link = "http://selenium1py.pythonanywhere.com/"


# @pytest.fixture(scope="function")
# def browser():
#     print("\nstart browser for test..")
#     browser = webdriver.Chrome()
#     yield browser
#     print("\nquit browser..")
#     browser.quit()


# class TestMainPage1():

#     def test_guest_should_see_login_link(self, browser):
#         browser.get(link)
#         browser.find_element(By.CSS_SELECTOR, "#login_link")

#     def test_guest_should_see_basket_link_on_the_main_page(self, browser):
#         browser.get(link)
#         browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")

#     @pytest.mark.xfail(reason="fixing this bug right now")
#     def test_guest_should_see_search_button_on_the_main_page(self, browser):
#         browser.get(link)
#         browser.find_element(By.CSS_SELECTOR, "input.btn.btn-default")

# Запустите тесты. Здесь мы добавили символ X в параметр -r, чтобы получить подробную информацию по XPASS-тестам:

# pytest -rX -v test_fixture10b.py

# Запустим наши тесты:

# pytest -rx -v test_fixture10a.py