from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    FIRST_NAME = (By.CSS_SELECTOR, '[data-test="firstName"]')
    LAST_NAME = (By.CSS_SELECTOR, '[data-test="lastName"]')
    POSTAL_CODE = (By.CSS_SELECTOR, '[data-test="postalCode"]')
    CONTINUE_BTN = (By.CSS_SELECTOR, '[data-test="continue"]')
    FINISH_BTN = (By.CSS_SELECTOR, '[data-test="finish"]')
    SUCCESS_HEADER = (By.CSS_SELECTOR, '[data-test="complete-header"]')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_shipping_info(self, first, last, zip_code):
        self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME)).send_keys(first)
        self.driver.find_element(*self.LAST_NAME).send_keys(last)
        self.driver.find_element(*self.POSTAL_CODE).send_keys(zip_code)
        self.driver.find_element(*self.CONTINUE_BTN).click()

    def finish_order(self):
        self.wait.until(EC.element_to_be_clickable(self.FINISH_BTN)).click()

    def get_success_message(self):
        return self.wait.until(EC.visibility_of_element_located(self.SUCCESS_HEADER)).text