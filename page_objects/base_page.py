from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    # кликнуть по элементу
    def click_on_element_1(self, locator):
        self.driver.find_element(*locator).click()

    # кликнуть по элементу (для Firefox)
    def click_on_element(self, locator):
        target = self.check_element_is_clickable(locator)
        click = ActionChains(self.driver)
        click.move_to_element(target).click().perform()

     # проверить кликабельность элемента
    def check_element_is_clickable(self, locator):
        return WebDriverWait(self.driver, 15).until(expected_conditions.element_to_be_clickable(locator))

    # проверить, что элемент появился
    def check_displaying_of_element(self, locator):
        return self.driver.find_element(*locator).is_displayed()

    # подождать прогрузки элемента
    def wait_visibility_of_element(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))

    # найти элемент на странице
    def find_element_with_wait(self, locator):
        self.wait_visibility_of_element(locator)
        return self.driver.find_element(*locator)

    # перетащить элемент
    def drag_and_drop_element(self, source_element, target_element):
        ActionChains(self.driver).drag_and_drop(source_element, target_element).pause(5).perform()

    # получить текст на элементе
    def get_text_on_element(self, locator):
        self.wait_visibility_of_element(locator)
        return self.driver.find_element(*locator).text

    # подождать смену текста на элементе
    def wait_for_element_to_change_text(self, locator, value):
        return WebDriverWait(self.driver, 10).until_not(expected_conditions.text_to_be_present_in_element(locator, value))
