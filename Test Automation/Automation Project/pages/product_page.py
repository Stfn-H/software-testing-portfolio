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

    OWN_RATING_COUNT = (
        By.XPATH,
        "//div[@class='comment'][.//div[@class='menu-icon']]//span[@class='small']"
    )
    OWN_COMMENT_TEXT = (
        By.XPATH,
        "//div[@class='comment'][.//div[@class='menu-icon']]/div[@class='comment-body']//p"
    )

    def _wait_for_menu_icon_or_empty_form(self):
        """Wait until the page has settled into ONE of two known states:
        an existing review (menu icon present) or the empty rating form.
        Whichever appears first — avoids blindly waiting out a fixed
        timeout for the branch that doesn't apply."""
        self.wait.until(
            lambda d: d.find_elements(*self.MENU_ICON) or d.find_elements(*self.INTERACTIVE_STARS)
        )

    def delete_review(self):
        """Delete any existing review from this account on this product."""
        self._wait_for_menu_icon_or_empty_form()
        while self.driver.find_elements(*self.MENU_ICON):
            menu_icons = self.driver.find_elements(*self.MENU_ICON)
            menu_icons[0].click()
            self.click(self.DELETE_BUTTON)
            self.wait_and_accept_alert()
            self.wait.until(EC.staleness_of(menu_icons[0]))
            self._wait_for_menu_icon_or_empty_form()

    def click_star(self, star_number):
        # star_number is 1-based: 1 = first star, 5 = fifth star
        self.click_js(self.STAR_LOCATORS[star_number])

    def enter_comment(self, text):
        self.type_text(self.COMMENT_INPUT, text)

    def send_rating(self):
        self.click(self.SEND_BUTTON)

    def get_own_rating_count(self):
        text = self.get_text(self.OWN_RATING_COUNT)  # e.g. "(5)"
        return int(text.strip("()"))

    def get_own_comment_text(self):
        return self.find(self.OWN_COMMENT_TEXT).text.strip()

    def get_rating_restriction_text(self):
        return self.get_text(self.RATING_RESTRICTION)

    def get_status_message(self):
        if self.is_visible(self.STATUS_MSG):
            return self.get_text(self.STATUS_MSG)
        return None