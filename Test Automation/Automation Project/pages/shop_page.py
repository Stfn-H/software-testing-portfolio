from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class ShopPage(BasePage):
    AGE_INPUT = (By.CSS_SELECTOR, "input[placeholder='DD-MM-YYYY']")
    AGE_CONFIRM_BUTTON = (By.XPATH, "//button[text()='Confirm']")
    AGE_MODAL_CONTAINER = (By.CSS_SELECTOR, ".modal-overlay")

    STATUS_MSG = (By.XPATH, "//div[@role='status']")
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, ".btn-cart")
    QUANTITY_INPUT = (By.CSS_SELECTOR, "input[type='number']")

    def confirm_age(self, birthdate):
        self.type_text(self.AGE_INPUT, birthdate)
        self.click(self.AGE_CONFIRM_BUTTON)
        self.wait.until(EC.invisibility_of_element_located(self.AGE_MODAL_CONTAINER))
        return self

    def submit_age(self, birthdate):
        self.type_text(self.AGE_INPUT, birthdate)
        self.click(self.AGE_CONFIRM_BUTTON)
        self.wait.until(EC.visibility_of_element_located(self.STATUS_MSG))
        return self

    def get_status_message(self):
        if self.is_visible(self.STATUS_MSG):
            return self.get_text(self.STATUS_MSG)
        return None

    def add_first_product_to_cart(self, quantity=1):
        if quantity > 1:
            self.type_text(self.QUANTITY_INPUT, str(quantity))
        self.scroll_into_view(self.ADD_TO_CART_BTN)
        self.click(self.ADD_TO_CART_BTN)
        self.wait.until(EC.visibility_of_element_located(self.STATUS_MSG))
        return self