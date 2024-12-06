from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from page_objects.base_page import BasePage
from locator.personal_account_locators import PersonalAccountLocators
from locator.password_recovery_locators import PasswordRecoveryLocators
from data import User

class PersonalAccount(BasePage):

    # заполнение полей в профиле
    def order_data_form(self):
        self.click_on_element(PasswordRecoveryLocators.field_email)  # нажать на поле имя
        self.driver.find_element(*PasswordRecoveryLocators.field_email).send_keys(User.EMAIL)  # ввести имя
        self.click_on_element(PasswordRecoveryLocators.field_password)  # клик по полю фамилия
        self.driver.find_element(*PasswordRecoveryLocators.field_password).send_keys(User.PASSWORD)  # ввести фамилию

   # ожидание кнопки войти
    def wait_button_enter_profil(self):
        self.wait_visibility_of_element(PersonalAccountLocators.button_enter)

    # нажать на кнопку войти
    def click_button_enter_profil(self):
        self.click_on_element(PersonalAccountLocators.button_enter)

    # ожидание истории заказов кнопки
    def wait_order_history_button(self):
        self.wait_visibility_of_element(PersonalAccountLocators.order_history)

    # кликнуть по кнопке история заказов
    def click_order_history_button(self):
        self.click_on_element(PersonalAccountLocators.order_history)

    # кликнуть по кнопке выход
    def click_button_exit(self):
        self.click_on_element(PersonalAccountLocators.button_exit)

    # ожидание загрузки кнопки выход
    def wait_button_exit(self):
        self.wait_visibility_of_element(PersonalAccountLocators.button_exit)
        # WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(PersonalAccountLocators.button_exit))

    # подождать прогрузки текста описания раздела
    def wait_visibility_of_description(self):
        self.wait_visibility_of_element(PersonalAccountLocators.description_of_section)
        # WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(PersonalAccountLocators.description_of_section))

    # проверить отображение описания раздела
    def check_displaying_of_description(self):
        return self.check_displaying_of_element(PersonalAccountLocators.description_of_section)

    # проверить историю заказов
    def check_displaying_order_history(self):
        return self.check_displaying_of_element(PersonalAccountLocators.text_history_order)

    # ожидание загрузки истории заказов
    def wait_history_order(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(PersonalAccountLocators.text_history_order))

    # дождаться загрузки кнопи войти
    def wait_button_enter(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(PersonalAccountLocators.button_enter))

    # проверить, что появилась кнопка войти
    def check_displaying_enter(self):
        return self.check_displaying_of_element(PersonalAccountLocators.button_enter)
