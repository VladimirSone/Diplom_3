import allure
import pytest
from selenium import webdriver



#  фикстура веб-драйвера
@pytest.fixture(params=[webdriver.Chrome, webdriver.Firefox], ids=['chrome', 'firefox'])
def driver(request):
    with allure.step(f'Открываем браузер'):
        driver = request.param()
        driver.maximize_window()
    #driver.window('--window-size=1920,1080')
        driver.get('https://stellarburgers.nomoreparties.site/')
        yield driver
    with allure.step('Закрываем браузер'):
        driver.quit()
