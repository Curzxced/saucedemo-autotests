import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage


@pytest.fixture
def login_page(driver):
    """Фикстура для инициализации и открытия страницы логина перед каждым тестом."""
    return LoginPage(driver).open()


class TestLogin:
    """Набор тестов для проверки авторизации на SauceDemo."""

    def test_successful_login(self, driver, login_page):
        login_page.login("standard_user", "secret_sauce")

        # Пометка: в реальных проектах URL проверяют через явное ожидание, чтобы избежать флаки-тестов
        WebDriverWait(driver, 5).until(EC.url_contains("/inventory.html"))
        assert driver.current_url.endswith("/inventory.html"), (
            f"Ожидался переход в каталог, но текущий URL: {driver.current_url}"
        )

    def test_locked_out_user_cannot_login(self, login_page):
        login_page.login("locked_out_user", "secret_sauce")

        error_text = login_page.get_error_text()
        assert "Sorry, this user has been locked out" in error_text, (
            f"Некорректный текст ошибки при блокировке: '{error_text}'"
        )

    @pytest.mark.parametrize(
        "username, password, expected_error",
        [
            pytest.param("", "", "Username is required", id="both_fields_empty"),
            pytest.param("standard_user", "", "Password is required", id="empty_password"),
            pytest.param("", "secret_sauce", "Username is required", id="empty_username"),
        ],
    )
    def test_login_validation_errors(self, login_page, username, password, expected_error):
        login_page.login(username, password)

        actual_error = login_page.get_error_text()
        assert expected_error in actual_error, (
            f"Ожидалась ошибка '{expected_error}', но получили '{actual_error}'"
        )
