import time
import allure
from conftest import driver
from page_objects.main_page import MainPage
from page_objects.order_feed_page import OrderFeedPage
from page_objects.personal_account_locators_page import PersonalAccount


class TestOrderFeedSection:

    @allure.title('Проверка открытия всплывающего окна с деталями при клике на заказ')
    def test_displaying_modal_order_details_success(self, driver):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)
        main_page.click_order_feed()
        order_feed_page.click_order_card()
        assert order_feed_page.check_displaying_order_feed()

    # тест падает неверный assert
    @allure.title('Проверить, что заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    @allure.title('Падает тест. Неверный assert - не смог сделать скролл до нужного элемента')
    def test_user_history_order_in_order_feed(self, driver):
        main_page = MainPage(driver)
        main_page.click_enter_account()
        personal_account_page = PersonalAccount(driver)
        personal_account_page.order_data_form()
        personal_account_page.click_button_enter_profil()
        main_page.adding_igredient_to_purchase()
        main_page.click_button_make_order()
        time.sleep(3)
        main_page.click_button_closet_window_order()
        main_page.click_button_personal_account()
        time.sleep(3)
        personal_account_page.click_order_history_button()
        time.sleep(3)
        order_feed_page = OrderFeedPage(driver)
        order_id = order_feed_page.get_id_order_card()
        time.sleep(3)
        main_page.click_order_feed()
        #time.sleep(3)
        assert order_feed_page.check_id_order_in_feed(order_id)


    @allure.title('Проверить, что при создании нового заказа счётчик выполнено за всё время увеличивается')
    @allure.title('Падает тест на Firefox')
    def test_creating_new_order_completed_counter_increases(self, driver):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)
        main_page.click_enter_account()
        personal_account_page = PersonalAccount(driver)
        personal_account_page.order_data_form()
        personal_account_page.click_button_enter_profil()
        time.sleep(3)
        main_page.click_order_feed()
        orders_count = order_feed_page.get_quantity_of_orders()
        main_page.click_button_designer()
        time.sleep(3)
        main_page.adding_igredient_to_purchase()
        main_page.click_button_make_order()
        time.sleep(3)
        main_page.click_button_closet_window_order()
        time.sleep(3)
        main_page.click_order_feed()
        orders_count_2 = order_feed_page.get_quantity_of_orders()
        time.sleep(2)
        assert orders_count < orders_count_2

    @allure.title('Проверить, что при создании нового заказа счётчик выполнено за сегодня увеличивается')
    @allure.title('Падает тест на Firefox')
    def test_new_order_counter_completed_today_increasing(self, driver):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)
        time.sleep(3)
        main_page.click_enter_account()
        personal_account_page = PersonalAccount(driver)
        personal_account_page.order_data_form()
        personal_account_page.click_button_enter_profil()
        time.sleep(3)
        main_page.click_order_feed()
        orders_count = order_feed_page.get_daily_quantity_of_orders()
        main_page.click_button_designer()
        time.sleep(3)
        main_page.adding_igredient_to_purchase()
        main_page.click_button_make_order()
        time.sleep(3)
        main_page.click_button_closet_window_order()
        time.sleep(3)
        main_page.click_order_feed()
        orders_count_2 = order_feed_page.get_daily_quantity_of_orders()
        time.sleep(2)
        assert orders_count < orders_count_2

    @allure.title('Проверить, что после оформления заказа его номер появляется в разделе в работе')
    @allure.title('Номер заказа не появляется в разделе в работе в Firefox, тест падает')
    def test_order_number_section_work(self, driver):
        main_page = MainPage(driver)
        time.sleep(2)
        main_page.click_enter_account()
        personal_account_page = PersonalAccount(driver)
        time.sleep(2)
        personal_account_page.order_data_form()
        personal_account_page.click_button_enter_profil()
        main_page.adding_igredient_to_purchase()
        main_page.click_button_make_order()
        time.sleep(2)
        main_page.get_number_of_order_in_modal_confirmation()
        main_page.click_button_closet_window_order()
        main_page.click_order_feed()
        order_feed_page = OrderFeedPage(driver)
        assert order_feed_page.check_order_number_feed_progress_section()
