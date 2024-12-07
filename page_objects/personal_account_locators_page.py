from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from page_objects.base_page import BasePage
from locator.personal_account_locators import PersonalAccountLocators
from locator.password_recovery_locators import PasswordRecoveryLocators
from data import User
import allure

class PersonalAccount(BasePage):

    @allure.step('заполнение полей в профиле')
    def order_data_form(self):
        self.click_on_element(PasswordRecoveryLocators.field_email)
        self.driver.find_element(*PasswordRecoveryLocators.field_email).send_keys(User.EMAIL)
        self.click_on_element(PasswordRecoveryLocators.field_password)
        self.driver.find_element(*PasswordRecoveryLocators.field_password).send_keys(User.PASSWORD)

    @allure.step('ожидание кнопки войти')
    def wait_button_enter_profil(self):
        self.wait_visibility_of_element(PersonalAccountLocators.button_enter)

    @allure.step('нажать на кнопку войти')
    def click_button_enter_profil(self):
        self.click_on_element(PersonalAccountLocators.button_enter)

    @allure.step('ожидание истории заказов кнопки')
    def wait_order_history_button(self):
        self.wait_visibility_of_element(PersonalAccountLocators.order_history)

    @allure.step('кликнуть по кнопке история заказов')
    def click_order_history_button(self):
        self.click_on_element(PersonalAccountLocators.order_history)

    @allure.step('кликнуть по кнопке выход')
    def click_button_exit(self):
        self.click_on_element(PersonalAccountLocators.button_exit)

    @allure.step('ожидание загрузки кнопки выход')
    def wait_button_exit(self):
        self.wait_visibility_of_element(PersonalAccountLocators.button_exit)

    @allure.step('подождать прогрузки текста описания раздела')
    def wait_visibility_of_description(self):
        self.wait_visibility_of_element(PersonalAccountLocators.description_of_section)

    @allure.step('проверить отображение описания раздела')
    def check_displaying_of_description(self):
        return self.check_displaying_of_element(PersonalAccountLocators.description_of_section)

    @allure.step('проверить историю заказов')
    def check_displaying_order_history(self):
        return self.check_displaying_of_element(PersonalAccountLocators.text_history_order)

    @allure.step('ожидание загрузки истории заказов')
    def wait_history_order(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(PersonalAccountLocators.text_history_order))

    @allure.step('дождаться загрузки кнопи войти')
    def wait_button_enter(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(PersonalAccountLocators.button_enter))

    @allure.step('проверить, что появилась кнопка войти')
    def check_displaying_enter(self):
        return self.check_displaying_of_element(PersonalAccountLocators.button_enter)
