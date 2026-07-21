from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class ProductPage(BasePage):
    STAR_LOCATORS = {
        1: (By.XPATH, "//div[@class='interactive-rating']/span[1]"),
        2: (By.XPATH, "//div[@class='interactive-rating']/span[2]"),
        3: (By.XPATH, "//div[@class='interactive-rating']/span[3]"),
        4: (By.XPATH, "//div[@class='interactive-rating']/span[4]"),
        5: (By.XPATH, "//div[@class='interactive-rating']/span[5]"),
    }

    INTERACTIVE_STARS = (By.CSS_SELECTOR, ".interactive-rating .star")
    COMMENT_INPUT = (By.CSS_SELECTOR, "textarea[placeholder='What is your view?']")
    SEND_BUTTON = (By.CSS_SELECTOR, ".new-review-btn-send")

    MENU_ICON = (By.CSS_SELECTOR, "div.menu-icon")
    DELETE_BUTTON = (By.XPATH, "//div[@class='dropdown-menu']/button[text()='Delete']")

    RATING_RESTRICTION = (By.CSS_SELECTOR, "div.reviewRestriction p")
    STATUS_MSG = (By.XPATH, "//div[@role='status']")

    COMMENT_CARD = (By.CSS_SELECTOR, "div.comment")

    def delete_review(self):
        """Delete any existing review from this account on this product."""
        while self.is_visible(self.MENU_ICON, timeout=2):
            menu_icons = self.driver.find_elements(*self.MENU_ICON)
            menu_icons[0].click()
            self.click(self.DELETE_BUTTON)
            self.wait_and_accept_alert()
            self.wait.until(EC.staleness_of(menu_icons[0]))

    def click_star(self, star_number):
        # star_number is 1-based: 1 = first star, 5 = fifth star
        self.click_js(self.STAR_LOCATORS[star_number])

    def enter_comment(self, text):
        self.type_text(self.COMMENT_INPUT, text)

    def send_rating(self):
        self.click(self.SEND_BUTTON)

    def _find_own_comment(self):
        """Wait until our own review has rendered (menu icon appears),
        then loop through all comment cards and return the one that
        has a menu icon (only our own review shows one)."""
        self.wait.until(EC.presence_of_element_located(self.MENU_ICON))
        comments = self.driver.find_elements(*self.COMMENT_CARD)
        for comment in comments:
            if comment.find_elements(By.CSS_SELECTOR, "div.menu-icon"):
                return comment
        return None

    def get_own_rating_count(self):
        own_comment = self._find_own_comment()
        text = own_comment.find_element(By.CSS_SELECTOR, "span.small").text  # e.g. "(5)"
        return int(text.strip("()"))

    def get_own_comment_text(self):
        own_comment = self._find_own_comment()
        return own_comment.find_element(By.CSS_SELECTOR, "p").text.strip()

    def get_rating_restriction_text(self):
        return self.get_text(self.RATING_RESTRICTION)

    def get_status_message(self):
        if self.is_visible(self.STATUS_MSG):
            return self.get_text(self.STATUS_MSG)
        return None