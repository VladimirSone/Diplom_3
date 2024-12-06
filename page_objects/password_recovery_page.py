from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from page_objects.base_page import BasePage
from locator.password_recovery_locators import PasswordRecoveryLocators
from helpers import random_password, random_email, random_name


class PasswordRecoveryPage(BasePage):
    # нажать на кнопку восстановить пароль
    def click_recovery_password(self):
        self.click_on_element(PasswordRecoveryLocators.button_recovery_password)

    # проверить, что загрузилась страница восстановить пароль (поле email)
    def check_displaying_page_password_recovery(self):
        return self.check_displaying_of_element(PasswordRecoveryLocators.field_email)

    # клик по полю email
    def click_field_email(self):
        self.click_on_element(PasswordRecoveryLocators.field_email)

    # ввести данные в поле email
    def enter_email(self):
        self.driver.find_element(*PasswordRecoveryLocators.field_email).send_keys(random_email())

    #  нажать кнопку восстановить
    def click_button_recovery(self):
        self.click_on_element(PasswordRecoveryLocators.button_recovery)

    # ожидание загрузки поля пароль
    def wait_field_password(self):
        WebDriverWait(self.driver, 6).until(expected_conditions.visibility_of_element_located(PasswordRecoveryLocators.field_password))

    # проверить, что появилось поле Пароль
    def check_displaying_field_password(self):
        return self.check_displaying_of_element(PasswordRecoveryLocators.field_password)

    # кликнуть на поле пароль
    def click_field_password(self):
        self.click_on_element(PasswordRecoveryLocators.field_password)

    # нажать на иконку показать пароль
    def click_icon_show_password(self):
        self.click_on_element(PasswordRecoveryLocators.icon_show_password)

        # ввести данные в поле пароль
    def enter_password(self):
        self.driver.find_element(*PasswordRecoveryLocators.field_email).send_keys(random_password())

    # проверить, что пароль видно
    def check_password_visible(self):
        return self.check_displaying_of_element(PasswordRecoveryLocators.password_visible)

    # проверить, что пароль не видно
    def check_password_hide(self):
        return self.check_displaying_of_element(PasswordRecoveryLocators.password_hide)
