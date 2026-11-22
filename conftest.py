import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-notifications")
    # Базовые флаги для стабильной работы в headless-режиме
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Selenium 4.6+ сам управляет драйвером, ChromeDriverManager нам больше не нужен! (не забыть)
    drv = webdriver.Chrome(options=options)
    yield drv
    drv.quit()
