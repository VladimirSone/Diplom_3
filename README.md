# Diplom_3
Дипломный проект.
Курс по автоматизации тестирования на Python, «Яндекс Практикум»
Проект по автоматизации UI-тестов для сервиса Stellar Burgers https://stellarburgers.nomoreparties.site/

Структура проекта:
1. Папка test содержит тесты;
2. Папка page_objects - содержит методы;
3. Папка locator - содержит путь к элементам;
4. Файл conftest - содержит фикстуру drive;
5. Файд helpers - содержит рандомные значения;
6. Файл data - содержит неизменяемые вводные данные.

Реализация тестов:
1. test_main_functionality.py - проверяет основные функции сайта;
2. test_oder_feed_siction.py -проверка заказов;
3. test_password_recovery.py - проверяет видимость пароля, восстановление входа;
4. test_personal_account.py - проверка аккаунта.
Установка зависимостей

$ pip install -r requirements.txt

Allure-отчет о тестировании в формате веб-страницы

allure serve allure_results
