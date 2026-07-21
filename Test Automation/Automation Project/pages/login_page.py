from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class LoginPage(BasePage):
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[type='email']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[type='password']")
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, "button.submit-btn")
    ERROR_MSG = (By.XPATH, "//div[@role='status']")

    def login(self, email, password):
        self.type_text(self.EMAIL_INPUT, email)
        self.type_text(self.PASSWORD_INPUT, password)
        current_url = self.get_url()
        self.scroll_into_view(self.SIGN_IN_BUTTON)
        self.click(self.SIGN_IN_BUTTON)
        self.wait.until(EC.url_changes(current_url))
        return self

    def get_error_message(self):
        if self.is_visible(self.ERROR_MSG):
            return self.get_text(self.ERROR_MSG)
        return None