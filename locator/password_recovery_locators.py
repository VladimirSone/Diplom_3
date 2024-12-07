from selenium.webdriver.common.by import By
class PasswordRecoveryLocators:
    # кнопка восстановить пароль
    button_recovery_password = (By.XPATH, '//a[text() = "Восстановить пароль"]')
    # текст поля Email
    field_email = (By.CLASS_NAME, 'input__textfield')
    # кнопка восстановить
    button_recovery = (By.XPATH, './/button[text() = "Восстановить"]')
    # поле Пароль
    field_password = (By.CSS_SELECTOR, '.input_type_password .input__textfield')
    # иконка показать/скрыть пароль
    icon_show_password = (By.XPATH, '//div[@class="input__icon input__icon-action"]/*[local-name() = "svg"]')
    # пароль видно
    password_visible = (By.XPATH, '//label[text()="Пароль"]/parent::div[contains(@class,''"input_status_active")]')
    # пароль скрыт
    password_hide = (By.XPATH, '//label[text()="Пароль"]/parent::div[contains(@class,''"input_type_password")]')

