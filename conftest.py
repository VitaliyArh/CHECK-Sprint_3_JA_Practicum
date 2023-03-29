import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support.wait import WebDriverWait
# import time
#
# @pytest.fixture(scope='function')
# def login(driver):
#     driver.find_element(By.CLASS_NAME, "button_button__33qZ0").click()
#     driver.find_element(By.XPATH, "//fieldset[2]/div/div/input").send_keys('Zanna_Shuvalova_8777@yandex.ru')
#     driver.find_element(By.XPATH, "//input[@type='password']").send_keys('123456')
#     return driver

# ========================================================================
# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options

url = 'https://stellarburgers.nomoreparties.site/'

@pytest.fixture(scope='function') # чтобы экземпляр браузера запускался по новой для каждого теста, потому что тесты должны быть изолированными
def driver(): # объявляем функцию driver потому что будем делать webdriver
    options = Options() # Импортировали Options из selenium.webdriver.chrome.options
    options.add_argument("--window-size=1200,600") # аргумент опции размера окна браузера

    browser = webdriver.Chrome(options=options)# будем консолидировать наш браузер и передаём в него опции
    browser.get(url) # чтобы откррыть ресурс пишем browser.get и указываем url

    yield browser   # фикстура должна быть yield, это декоратор который вешается на какую либо функцию,
    browser.quit()  # она меняет поведение функции не изменяя саму функцию, yield - используется в основном
# для итераторов. Дойдя до yield выполнение фикстуры остановится , и будет запущен первый
# тест после того как тест отработает, мы вернёмся обратно к фикстуре, к yield и
# броузер будет закрыт. После этого всё повторится но со вторым тестом, и так пока
# не пройдут все тесты






