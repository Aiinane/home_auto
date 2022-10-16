import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

#answer = math.log(int(time.time()))
answer = ""

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('links', ["https://stepik.org/lesson/236895/step/1",
                            "https://stepik.org/lesson/236896/step/1",
                            "https://stepik.org/lesson/236897/step/1",
                            "https://stepik.org/lesson/236898/step/1",
                            "https://stepik.org/lesson/236899/step/1",
                            "https://stepik.org/lesson/236903/step/1",
                            "https://stepik.org/lesson/236904/step/1",
                            "https://stepik.org/lesson/236905/step/1"])
def test_for_link(browser, links):
    link = f"{links}"
    browser.get(link)
    browser.implicity_wait(10)
    new_input = browser.find_element(By.CSS_SELECTOR, "textarea[id='ember89']")
    new_input.send_keys(math.log(int(time.time())))
    button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()