from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    CHECKOUT_BTN = (By.CSS_SELECTOR, '[data-test="checkout"]')
    REMOVE_BACKPACK_BTN = (By.CSS_SELECTOR, '[data-test="remove-sauce-labs-backpack"]')
    CART_ITEMS = (By.CSS_SELECTOR, '[data-test="inventory-item"]')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_items_count(self):
        return len(self.driver.find_elements(*self.CART_ITEMS))

    def remove_backpack(self):
        self.wait.until(EC.element_to_be_clickable(self.REMOVE_BACKPACK_BTN)).click()

    def click_checkout(self):
        self.driver.find_element(*self.CHECKOUT_BTN).click()