from selenium.webdriver.common.by import By


class OrderFeedLocators:
    # текст Лента заказов на странице лента заказов
    text_order_feed = (By.XPATH, '//h1[text()="Лента заказов"]')
    # карточка заказа в ленте
    order_card = (By.XPATH, '//li[contains(@class, "OrderHistory_listItem")]')
    # номер карточки в ленте заказа
    order_number_in_card = (By.XPATH, './/p[@class="text text_type_digits-default mb-10 mt-5"]')
    # Номер заказа в карточке заказа
    order_card_id = (By.XPATH, '(//div[contains(@class, "OrderHistory_textBox")]' '/p[contains(@class, "text_type_digits-default")])')
    # Номеh заказа вленте — заготовка, вкоторуюнужноподставитьidискомогозаказа
    id_order_card_in_feed_with_substitutions = (By.XPATH, './/*[text()="{order_id}"]')
    # Счетчик заказов "Выполнено за все время"
    quantity_of_orders = (By.XPATH, '//p[text()="Выполнено за все время:"]/following-sibling::p')
    # Счетчик заказов "Выполнено за сегодня"
    daily_quantity_of_orders = (By.XPATH, '//p[text()="Выполнено за сегодня:"]/following-sibling::p')
    # Номер заказа в разделе "В работе"
    number_of_order_in_progress = (By.XPATH, '//ul[contains(@class, ''"OrderFeed_orderListReady")]/li[contains(@class, ''"text_type_digits-default")]')














