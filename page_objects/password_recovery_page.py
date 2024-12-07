from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from page_objects.base_page import BasePage
from locator.password_recovery_locators import PasswordRecoveryLocators
from helpers import random_password, random_email
import allure


class PasswordRecoveryPage(BasePage):
    @allure.step('нажать на кнопку восстановить пароль')
    def click_recovery_password(self):
        self.click_on_element(PasswordRecoveryLocators.button_recovery_password)

    @allure.step('проверить, что загрузилась страница восстановить пароль (поле email)')
    def check_displaying_page_password_recovery(self):
        return self.check_displaying_of_element(PasswordRecoveryLocators.field_email)

    @allure.step('клик по полю email')
    def click_field_email(self):
        self.click_on_element(PasswordRecoveryLocators.field_email)

    @allure.step('ввести данные в поле email')
    def enter_email(self):
        self.driver.find_element(*PasswordRecoveryLocators.field_email).send_keys(random_email())

    @allure.step('нажать кнопку восстановить')
    def click_button_recovery(self):
        self.click_on_element(PasswordRecoveryLocators.button_recovery)

    @allure.step('ожидание загрузки поля пароль')
    def wait_field_password(self):
        WebDriverWait(self.driver, 6).until(expected_conditions.visibility_of_element_located(PasswordRecoveryLocators.field_password))

    @allure.step('проверить, что появилось поле Пароль')
    def check_displaying_field_password(self):
        return self.check_displaying_of_element(PasswordRecoveryLocators.field_password)

    @allure.step('кликнуть на поле пароль')
    def click_field_password(self):
        self.click_on_element(PasswordRecoveryLocators.field_password)

    @allure.step('нажать на иконку показать пароль')
    def click_icon_show_password(self):
        self.click_on_element(PasswordRecoveryLocators.icon_show_password)

    @allure.step('ввести данные в поле пароль')
    def enter_password(self):
        self.driver.find_element(*PasswordRecoveryLocators.field_email).send_keys(random_password())

    @allure.step('проверить, что пароль видно')
    def check_password_visible(self):
        return self.check_displaying_of_element(PasswordRecoveryLocators.password_visible)

    @allure.step('проверить, что пароль не видно')
    def check_password_hide(self):
        return self.check_displaying_of_element(PasswordRecoveryLocators.password_hide)
