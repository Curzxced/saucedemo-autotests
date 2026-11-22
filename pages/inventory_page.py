from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class InventoryPage:
    # локаторы
    BACKPACK_ADD_BTN = (By.CSS_SELECTOR, '[data-test="add-to-cart-sauce-labs-backpack"]')
    BIKE_LIGHT_ADD_BTN = (By.CSS_SELECTOR, '[data-test="add-to-cart-sauce-labs-bike-light"]')
    CART_BADGE = (By.CSS_SELECTOR, '[data-test="shopping-cart-badge"]')
    CART_LINK = (By.CSS_SELECTOR, '[data-test="shopping-cart-link"]')
    SORT_DROPDOWN = (By.CSS_SELECTOR, '[data-test="product-sort-container"]')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # методы
    def add_backpack_to_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.BACKPACK_ADD_BTN)).click()

    def add_bike_light_to_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.BIKE_LIGHT_ADD_BTN)).click()

    def get_cart_badge_count(self):
        # Если товаров нет, бейдж исчезает, значит ловим исключение
        try:
            return self.driver.find_element(*self.CART_BADGE).text
        except:
            return "0"

    def go_to_cart(self):
        self.driver.find_element(*self.CART_LINK).click()

    def sort_by_price_high_to_low(self):
        dropdown = self.wait.until(EC.element_to_be_clickable(self.SORT_DROPDOWN))
        Select(dropdown).select_by_value("hilo")