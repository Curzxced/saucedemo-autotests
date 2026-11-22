import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-notifications")
    # базовые флаги для стабильной работы в headless-режиме
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # отключаем всплывающие окна сохранения и проверки пароля в Chrome
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False,
    }
    options.add_experimental_option("prefs", prefs)

    # Selenium 4.6+ сам управляет драйвером, ChromeDriverManager не нужен
    drv = webdriver.Chrome(options=options)
    yield drv
    drv.quit()


@pytest.fixture
def auth_user(driver):
    # открываем сайт и сразу авторизуемся под стандартным юзером
    LoginPage(driver).open().login("standard_user", "secret_sauce")
    return driver
