# Проект автоматизации тестирования сервиса Яндекс Самокат
1. Основа для написания автотестов — фреймворк pytest.
2. Установить зависимости — pip install -r requirements.txt.
3. Команда для запуска — pytest tests/

Тесты проверяют функционал: 
1. работы раздела "Вопросы о важном"
2. Переход по ссылкам из лого "Яндекс" и "Самокат"
3. заказа самоката 

Структура проекта:
1. Директория page_objects содержит классы с методами-шагами 
2. Директрия tests содержит тестовые классы 
3. Директория locators содержит локаторы основной страницы и страницы заказа
4. Директория allure_reslults содержит отчеты с результатами тестов
5. Файл testdata.py содержит тестовые данные пользователей и faq 
