from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from page_objects.base_page import BasePage
from locator.personal_account_locators import PersonalAccountLocators
from locator.main_page_locators import MainPageLocators

class MainPage(BasePage):

    # ожидание появления кнопки войти в аккаунт
    def wait_button_enter_account(self):
        self.wait_visibility_of_element(MainPageLocators.button_enter_account)

    # нажать на кнопку Войти в аккаунт
    def click_enter_account(self):
        self.click_on_element(MainPageLocators.button_enter_account)

    # ожидание кнопки личный кабинет
    def wait_button_personal_account(self):
        self.wait_visibility_of_element(PersonalAccountLocators.button_personal_account)

    # нажать на кнопку личный кабинет
    def click_button_personal_account(self):
        self.click_on_element(PersonalAccountLocators.button_personal_account)

    # нажать на кнопку конструктор
    def click_button_designer(self):
        self.click_on_element(MainPageLocators.button_designer)

    # проверить, что появился текст на главной странице
    def check_displaying_text_main_order(self):
        return self.check_displaying_of_element(MainPageLocators.chapter_buns)

    # нажать на кнопку Лента заказов
    def click_order_feed(self):
        self.click_on_element(MainPageLocators.order_feed)

    # подождать появления кнопки ингредиент в меню булки
    def wait_button_ingredient(self):
        self.wait_visibility_of_element(MainPageLocators.ingredient)

    # клик по кнопке ингредиент в меню булки
    def click_button_ingredient(self):
        self.click_on_element(MainPageLocators.ingredient)

    # ожидание загрузки текста Детали ингредиента
    def wait_details_ingredient(self):
        self.wait_visibility_of_element(MainPageLocators.text_details_ingredient)

    # проверить, что появляется текст в окне Детали ингредиента
    def check_displaying_details_ingredient(self):
        return self.check_displaying_of_element(MainPageLocators.text_details_ingredient)

    # нажать на крестик окна детали ингредиента
    def click_button_closet_window_detail_ingredient(self):
        self.click_on_element(MainPageLocators.button_closet_window_details_ingredient)

    # добавить ингредиент для покупки
    def adding_igredient_to_purchase(self):
        source = WebDriverWait(self.driver, 6).until(expected_conditions.visibility_of_element_located(MainPageLocators.ingredient))
        target = WebDriverWait(self.driver, 6).until(expected_conditions.visibility_of_element_located(MainPageLocators.place_for_ingredients))
        self.drag_and_drop_element(source, target)

    # получить количество ингредиентов
    def check_quantity_ingredient(self):
        return WebDriverWait(self.driver, 6).until(expected_conditions.visibility_of_element_located(MainPageLocators.quantity_ingredient))

    # нажать на кнопку оформить заказ
    def click_button_make_order(self):
        self.click_on_element(MainPageLocators.button_make_order)

    # проверить появления текста идентификатор заказа в окне заказа
    def check_displaying_order_identifier(self):
        return self.check_displaying_of_element(MainPageLocators.order_identifier)

    # дождаться загрузки окна заказ оформлен
    def wait_window_order_identifier(self):
        self.wait_visibility_of_element(MainPageLocators.button_closet_window_order)

    # нажать крестик для закрытия окна заказ оформлен
    def click_button_closet_window_order(self):
        self.click_on_element(MainPageLocators.button_closet_window_order)

    # дождаться загрузки окна заказ оформлен
    #def wait_window_order_identifier(self):
        #WebDriverWait(self.driver, 60).until(expected_conditions.visibility_of_element_located(MainPageLocators.button_closet_window_order))

    # 'Получить номер в окне о создании заказа')
    def get_number_of_order_in_modal_confirmation(self):
        self.wait_for_element_to_change_text(MainPageLocators.number_of_order_in_modal_confirmation, '9999')
        return self.get_text_on_element(MainPageLocators.number_of_order_in_modal_confirmation)
