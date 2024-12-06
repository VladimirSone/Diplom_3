import time
import allure
from page_objects.main_page import MainPage
from conftest import driver
from page_objects.order_feed_page import OrderFeedPage
from page_objects.personal_account_locators_page import PersonalAccount


class TestMainFunctionality:

    @allure.title('Проверить, что возможен переход по клику на конструктор')
    def test_transition_designer(self, driver):
        main_page = MainPage(driver)
        main_page.click_enter_account()
        main_page.click_button_designer()
        assert main_page.check_displaying_text_main_order()

    @allure.title('Проверить, что возможен переход по клику на «Лента заказов»')
    def test_transition_order_feed(self, driver):
        main_page = MainPage(driver)
        main_page.click_order_feed()
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.wait_text_order_feed()
        assert order_feed_page.check_displaying_order_feed()

    @allure.title('Проверить,если кликнуть на ингредиент, появится всплывающее окно с деталями')
    def test_ingredient_window_details(self, driver):
        main_page = MainPage(driver)
        #main_page.wait_button_ingredient()
        main_page.click_button_ingredient()
        main_page.wait_details_ingredient()
        assert main_page.check_displaying_details_ingredient()

    @allure.title('Проверить, что всплывающее окно закрывается кликом по крестику')
    def test_closet_window_ingredient_details(self, driver):
        main_page = MainPage(driver)
        main_page. wait_button_ingredient()
        main_page.click_button_ingredient()
        main_page.wait_details_ingredient()
        main_page.click_button_closet_window_detail_ingredient()
        assert main_page.check_displaying_text_main_order()

    @allure.title('Проверить,что при добавлении ингредиента в заказ, увеличивается оплата данного ингредиента')
    def test_adding_and_increasing_counter_ingredient(self, driver):
        main_page = MainPage(driver)
        main_page.adding_igredient_to_purchase()
        assert main_page.check_quantity_ingredient()

    @allure.title('Проверить, что залогиненный пользователь может оформить заказ')
    def test_user_makes_order(self, driver):
        main_page = MainPage(driver)
        time.sleep(2)
        main_page.click_enter_account()
        personal_account_page = PersonalAccount(driver)
        personal_account_page.order_data_form()
        personal_account_page.click_button_enter_profil()
        main_page.adding_igredient_to_purchase()
        main_page.click_button_make_order()
        assert main_page.check_displaying_order_identifier()
