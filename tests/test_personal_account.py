import time
import allure
from page_objects.main_page import MainPage
from conftest import driver
from page_objects.personal_account_locators_page import PersonalAccount


class TestPersonalAccount:

    @allure.title('Проверить, что возможен переход в профиль по клику на личный кабинет')
    def test_enter_profile_account(self, driver):
        main_page = MainPage(driver)
        personal_account_locators_page = PersonalAccount(driver)
        main_page.wait_button_enter_account()
        main_page.click_enter_account()
        personal_account_locators_page.order_data_form()
        personal_account_locators_page.click_button_enter_profil()
        time.sleep(2)
        main_page.click_button_personal_account()
        personal_account_locators_page.wait_visibility_of_description()
        assert personal_account_locators_page.check_displaying_of_description()


    @allure.title('Проверить переход в раздел историй по клику на кнопку "Раздел историй"')
    def test_enter_order_history(self, driver):
        main_page = MainPage(driver)
        main_page.click_enter_account()
        personal_account_locators_page = PersonalAccount(driver)
        personal_account_locators_page.order_data_form()
        personal_account_locators_page.click_button_enter_profil()
        main_page.wait_button_personal_account()
        time.sleep(2)
        main_page.click_button_personal_account()
        personal_account_locators_page.wait_visibility_of_description()
        time.sleep(2)
        personal_account_locators_page.click_order_history_button()
        personal_account_locators_page.wait_history_order()
        assert personal_account_locators_page.check_displaying_order_history()

    @allure.title('Проверить выход из аккаунта')
    def test_exit_personal_account(self, driver):
        main_page = MainPage(driver)
        main_page.click_enter_account()
        personal_account_locators_page = PersonalAccount(driver)
        personal_account_locators_page.order_data_form()
        personal_account_locators_page.click_button_enter_profil()
        time.sleep(2)
        main_page.wait_button_personal_account()
        main_page.click_button_personal_account()
        personal_account_locators_page.wait_button_exit()
        personal_account_locators_page.click_button_exit()
        personal_account_locators_page.wait_button_enter()
        assert personal_account_locators_page.check_displaying_enter()
