from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckoutPage(BasePage):
    SHIPPING_VALUE = (By.XPATH, "//h5[text()='Shipment:']/following-sibling::h5")
    REMOVE_ITEM = (By.XPATH, "//a[@class='remove-icon']")

    def get_shipping_cost(self):
        return self.get_text(self.SHIPPING_VALUE)

    def clear_cart(self):
        while self.is_visible(self.REMOVE_ITEM, timeout=1):
            buttons = self.driver.find_elements(*self.REMOVE_ITEM)
            buttons[0].click()