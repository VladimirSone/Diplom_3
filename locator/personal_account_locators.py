from selenium.webdriver.common.by import By
class PersonalAccountLocators:
    # раздел История заказов
    order_history = (By.XPATH, '//a[@href = "/account/order-history"]')
    # кнопка "Выход"
    button_exit = (By.XPATH, '//button[@type = "button"]')
    # Описание раздела: "В этом разделе вы можете изменить свои персональные данные"
    description_of_section = (By.XPATH, '//p[contains(@class, "Account_text")]')
    # кнопка Войти
    button_enter = (By.XPATH, '//button[text() = "Войти"]')
    # кнопка Личный кабинет перенести в маин
    button_personal_account = (By.XPATH, '//p[text()="Личный Кабинет"]/parent::a')
    # текст заказа в разделе История заказов
    text_history_order = (By.XPATH, './/p[@class="Account_text__fZAIn text text_type_main-default"]')  #  (By.XPATH, '/html/body/div/div/main/div/div/div/ul/li/a/h2')
