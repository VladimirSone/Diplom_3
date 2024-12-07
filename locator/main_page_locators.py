from selenium.webdriver.common.by import By

class MainPageLocators:
    # кнопка войти в аккаунт
    button_enter_account = (By.XPATH, './/button[text() = "Войти в аккаунт"]')
    # кнопка конструктор
    button_designer = (By.XPATH, '//p[text() = "Конструктор"]')
    # раздел булки
    chapter_buns = (By.XPATH, '//span[text() = "Булки"]')
    # кнопка "Лента заказов"
    order_feed = (By.XPATH, '//p[text()="Лента Заказов"]')
    # ингредиент
    ingredient = (By.XPATH, './/a[@class="BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8"]')
    # текст Детали ингедиента в всплывающем окне
    text_details_ingredient = (By.XPATH, './/h2[text()="Детали ингредиента"]')
    # крестик в окне Детали ингредиента
    button_closet_window_details_ingredient = (By.XPATH, './/button[@class="Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK"]')
    # крестик в окне Заказ оформлен
    button_closet_window_order = (By.XPATH, './/button[@class="Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK"]')
    # перетаскиваю ингредиент для покупки
    place_for_ingredients = (By.XPATH, '//section[contains(@class, "BurgerConstructor_basket")]')
    # количество добавленных ингредиентов
    quantity_ingredient = (By.XPATH, './/a[@class="BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8"]//p[''@class="counter_counter__num__3nue1"]')
    # кнопка Оформить заказ
    button_make_order = (By.XPATH, '//button[text()="Оформить заказ"]')
    # окно идентификатор заказа (текст Индетификатор заказа)
    order_identifier = (By.XPATH, './/p[@class="undefined text text_type_main-medium mb-15"]')
    # кнопка Личный кабинет перенести в маин
    button_personal_account = (By.XPATH, '//p[text()="Личный Кабинет"]/parent::a')
    # Номер созданного заказа в окне подтверждения
    number_of_order_in_modal_confirmation = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]//h2')


