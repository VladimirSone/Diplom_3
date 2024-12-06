from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locator.order_feed_locators import OrderFeedLocators
from page_objects.base_page import BasePage

class OrderFeedPage(BasePage):

    # дождаться загрузки текста в ленте заказов
    def wait_text_order_feed(self):
        WebDriverWait(self.driver, 6).until(expected_conditions.visibility_of_element_located(OrderFeedLocators.text_order_feed))

    # проверить, что появился текст лента заказов
    def check_displaying_order_feed(self):
        return self.check_displaying_of_element(OrderFeedLocators.text_order_feed)

    # кликнуть по первому/последнему заказу в ленте
    def click_order_card(self):
        WebDriverWait(self.driver, 6).until(expected_conditions.visibility_of_element_located(OrderFeedLocators.order_card))
        self.click_on_element(OrderFeedLocators.order_card)

    # проверить карточку заказа в ленте
    def check_displaying_card_order(self):
        return self.check_displaying_of_element(OrderFeedLocators.order_number_in_card)

        # получить номер заказа в карточке
    def get_id_order_card(self):
        return self.get_text_on_element(OrderFeedLocators.order_card_id)

    # проверить наличие номера заказа в списке ленты
    def check_id_order_in_feed(self, order_id):
        locator = OrderFeedLocators.id_order_card_in_feed_with_substitutions
        locator_with_order_id = (locator[0], locator[1].format(order_id=order_id))
        self.find_element_with_wait(locator_with_order_id)
        return self.check_displaying_of_element(locator_with_order_id)

    # получить количество заказов, выполненных за все время
    def get_quantity_of_orders(self):
        self.find_element_with_wait(OrderFeedLocators.quantity_of_orders)
        return self.get_text_on_element(OrderFeedLocators.quantity_of_orders)

    # получить количество заказов, выполненных за сегодня
    def get_daily_quantity_of_orders(self):
        self.find_element_with_wait(OrderFeedLocators.daily_quantity_of_orders)
        return self.get_text_on_element(OrderFeedLocators.daily_quantity_of_orders)

    # проверить получение номера последнего заказа в разделе в работе
    def check_order_number_feed_progress_section(self):
        return self.get_text_on_element(OrderFeedLocators.number_of_order_in_progress)
