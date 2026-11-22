from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class LoginPage:
    """Page Object для страницы авторизации SauceDemo."""

    URL = "https://saucedemo.com"

    # Локаторы
    _USERNAME_INPUT = (By.CSS_SELECTOR, '[data-test="username"]')
    _PASSWORD_INPUT = (By.CSS_SELECTOR, '[data-test="password"]')
    _LOGIN_BUTTON = (By.CSS_SELECTOR, '[data-test="login-button"]')
    _ERROR_CONTAINER = (By.CSS_SELECTOR, '[data-test="error"]')

    def __init__(self, driver: WebDriver, timeout: int = 10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self) -> "LoginPage":
        self.driver.get(self.URL)
        return self

    def enter_username(self, username: str) -> None:
        field = self.wait.until(EC.visibility_of_element_located(self._USERNAME_INPUT))
        field.clear()
        field.send_keys(username)

    def enter_password(self, password: str) -> None:
        field = self.wait.until(EC.visibility_of_element_located(self._PASSWORD_INPUT))
        field.clear()
        field.send_keys(password)

    def click_login(self) -> None:
        btn = self.wait.until(EC.element_to_be_clickable(self._LOGIN_BUTTON))
        btn.click()

    def login(self, username: str, password: str) -> None:
        """Выполняет полный сценарий входа в систему."""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def get_error_text(self) -> str:
        try:
            error_el = self.wait.until(EC.visibility_of_element_located(self._ERROR_CONTAINER))
            return error_el.text
        except TimeoutException:
            return ""
