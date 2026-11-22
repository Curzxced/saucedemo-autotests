from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class InventoryPage:
    # локаторы
    BACKPACK_ADD_BTN = (By.CSS_SELECTOR, '[data-test="add-to-cart-sauce-labs-backpack"]')
    BACKPACK_REMOVE_BTN = (By.CSS_SELECTOR, '[data-test="remove-sauce-labs-backpack"]')
    BIKE_LIGHT_ADD_BTN = (By.CSS_SELECTOR, '[data-test="add-to-cart-sauce-labs-bike-light"]')
    CART_BADGE = (By.CSS_SELECTOR, '[data-test="shopping-cart-badge"]')
    CART_LINK = (By.CSS_SELECTOR, '[data-test="shopping-cart-link"]')
    SORT_DROPDOWN = (By.CSS_SELECTOR, '[data-test="product-sort-container"]')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_backpack_to_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.BACKPACK_ADD_BTN)).click()
        # ждем пока кнопка сменится на Remove
        self.wait.until(EC.visibility_of_element_located(self.BACKPACK_REMOVE_BTN))

    def add_bike_light_to_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.BIKE_LIGHT_ADD_BTN)).click()

    def get_cart_badge_count(self):
        # если товаров нет, бейдж пропадает из DOM
        try:
            return self.driver.find_element(*self.CART_BADGE).text
        except NoSuchElementException:
            return "0"

    def go_to_cart(self):
        cart_btn = self.wait.until(EC.element_to_be_clickable(self.CART_LINK))
        # плавно наводим курсор и кликаем как реальный пользователь
        ActionChains(self.driver).move_to_element(cart_btn).click().perform()
        self.wait.until(EC.url_contains("/cart.html"))

    def sort_by_price_high_to_low(self):
        dropdown = self.wait.until(EC.element_to_be_clickable(self.SORT_DROPDOWN))
        Select(dropdown).select_by_value("hilo")
