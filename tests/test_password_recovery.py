import allure
from page_objects.password_recovery_page import PasswordRecoveryPage
from page_objects.main_page import MainPage
from conftest import driver


class TestPasswordRecovery:
    @allure.title('Проверить, что возможен переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_transition_window_password_recovery(self, driver):
        main_page = MainPage(driver)
        main_page.click_enter_account()
        password_recovery_page = PasswordRecoveryPage(driver)
        password_recovery_page.click_recovery_password()
        assert password_recovery_page.check_displaying_page_password_recovery()

    @allure.title('Проверить, что возможен ввод почты и клик по кнопке Восстановить')
    def test_input_email_and_click_recovery(self, driver):
        main_page = MainPage(driver)
        main_page.click_enter_account()
        password_recovery_page = PasswordRecoveryPage(driver)
        password_recovery_page.click_recovery_password()
        password_recovery_page.enter_email()
        password_recovery_page.click_button_recovery()
        password_recovery_page.wait_field_password()
        assert password_recovery_page.check_displaying_field_password()

    @allure.title('Проверить, что клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    def test_click_icon_show(self, driver):
        main_page = MainPage(driver)
        main_page.click_enter_account()
        password_recovery_page = PasswordRecoveryPage(driver)
        password_recovery_page.click_recovery_password()
        password_recovery_page.enter_email()
        password_recovery_page.click_button_recovery()
        password_recovery_page.wait_field_password()
        password_recovery_page.click_field_password()
        password_recovery_page.enter_password()
        password_recovery_page.click_icon_show_password()
        assert password_recovery_page.check_password_visible()

    @allure.title('Проверить, что клик по кнопке показать/скрыть пароль делает поле неактивным — скрывает пароль')
    def test_click_icon_show_click_icon_hide(self, driver):
        main_page = MainPage(driver)
        main_page.click_enter_account()
        password_recovery_page = PasswordRecoveryPage(driver)
        password_recovery_page.click_recovery_password()
        password_recovery_page.enter_email()
        password_recovery_page.click_button_recovery()
        password_recovery_page.wait_field_password()
        password_recovery_page.click_field_password()
        password_recovery_page.enter_password()
        password_recovery_page.click_icon_show_password()
        password_recovery_page.click_icon_show_password()
        assert password_recovery_page.check_password_hide()
