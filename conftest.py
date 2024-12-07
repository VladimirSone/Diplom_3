import allure
import pytest
from url import Url
from selenium import webdriver


#  фикстура веб-драйвера
@pytest.fixture(params=[webdriver.Chrome, webdriver.Firefox], ids=['chrome', 'firefox'])
def driver(request):
    with allure.step(f'Открываем браузер'):
        driver = request.param()
        driver.maximize_window()
        driver.get(Url.BASE_URL)
        yield driver
    with allure.step('Закрываем браузер'):
        driver.quit()
