# Примеры автотестов веб SauceDemo UI

UI-автотесты для https://www.saucedemo.com на Python + pytest + Selenium.

## Стек
- Python, Selenium WebDriver, pytest, pytest-html, webdriver-manager
- Page Object Model
- Явные ожидания (WebDriverWait)

## Покрытые сценарии
- Валидный логин
- Заблокированный пользователь
- Пустые поля (параметризация)
- Проверка сообщений об ошибках

## Запуск
pip install -r requirements.txt
pytest -v
