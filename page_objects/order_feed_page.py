from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locator.order_feed_locators import OrderFeedLocators
from page_objects.base_page import BasePage
import allure

class OrderFeedPage(BasePage):

    @allure.step('дождаться загрузки текста в ленте заказов')
    def wait_text_order_feed(self):
        WebDriverWait(self.driver, 6).until(expected_conditions.visibility_of_element_located(OrderFeedLocators.text_order_feed))

    @allure.step('проверить, что появился текст лента заказов')
    def check_displaying_order_feed(self):
        return self.check_displaying_of_element(OrderFeedLocators.text_order_feed)

    @allure.step('кликнуть по первому/последнему заказу в ленте')
    def click_order_card(self):
        WebDriverWait(self.driver, 6).until(expected_conditions.visibility_of_element_located(OrderFeedLocators.order_card))
        self.click_on_element(OrderFeedLocators.order_card)

    @allure.step('проверить карточку заказа в ленте')
    def check_displaying_card_order(self):
        return self.check_displaying_of_element(OrderFeedLocators.order_number_in_card)

    @allure.step('получить номер заказа в карточке')
    def get_id_order_card(self):
        return self.get_text_on_element(OrderFeedLocators.order_card_id)

    @allure.step('получить количество заказов, выполненных за все время')
    def get_quantity_of_orders(self):
        self.find_element_with_wait(OrderFeedLocators.quantity_of_orders)
        return self.get_text_on_element(OrderFeedLocators.quantity_of_orders)

    @allure.step('получить количество заказов, выполненных за сегодня')
    def get_daily_quantity_of_orders(self):
        self.find_element_with_wait(OrderFeedLocators.daily_quantity_of_orders)
        return self.get_text_on_element(OrderFeedLocators.daily_quantity_of_orders)

    @allure.step('проверить получение номера последнего заказа в разделе в работе')
    def check_order_number_feed_progress_section(self):
        return self.get_text_on_element(OrderFeedLocators.number_of_order_in_progress)

    @allure.step('получить номер заказа в ленте')
    def get_order_number_list(self):
        element = self.wait_visibility_of_element(OrderFeedLocators.order_number_history_list)
        return element.text

    @allure.step('получить номер заказа в истории заказов')
    def get_order_number(self):
        element = self.wait_visibility_of_element(OrderFeedLocators.order_number_history)
        return element.text
