import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('кликнуть по элементу (для Firefox)')
    def click_on_element(self, locator):
        target = self.check_element_is_clickable(locator)
        click = ActionChains(self.driver)
        click.move_to_element(target).click().perform()

    @allure.step('проверить кликабельность элемента')
    def check_element_is_clickable(self, locator):
        WebDriverWait(self.driver, 15).until(expected_conditions.element_to_be_clickable(locator))
        return self.driver.find_element(*locator)

    @allure.step('проверить, что элемент появился')
    def check_displaying_of_element(self, locator):
        return self.driver.find_element(*locator).is_displayed()

    @allure.step('подождать прогрузки элемента')
    def wait_visibility_of_element(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('найти элемент на странице')
    def find_element_with_wait(self, locator):
        self.wait_visibility_of_element(locator)
        return self.driver.find_element(*locator)

    @allure.step('перетащить элемент')
    def drag_and_drop_element(self, source_element, target_element):
        ActionChains(self.driver).drag_and_drop(source_element, target_element).pause(5).perform()

    @allure.step('получить текст на элементе')
    def get_text_on_element(self, locator):
        self.wait_visibility_of_element(locator)
        return self.driver.find_element(*locator).text

    @allure.step('подождать смену текста на элементе')
    def wait_for_element_to_change_text(self, locator, value):
        return WebDriverWait(self.driver, 10).until_not(expected_conditions.text_to_be_present_in_element(locator, value))
