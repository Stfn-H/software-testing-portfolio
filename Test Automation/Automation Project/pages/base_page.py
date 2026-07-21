from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    DEFAULT_TIMEOUT = 10

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, self.DEFAULT_TIMEOUT)

    def open(self, url):
        self.driver.get(url)
        return self

    def get_url(self):
        return self.driver.current_url

    def find(self, locator):
        """Wait for and return a single element."""
        return self.wait.until(EC.presence_of_element_located(locator))

    def is_visible(self, locator, timeout=5):
        """Return True if element is visible within timeout."""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    def click(self, locator):
        """Wait for element to be clickable, then click it."""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def click_js(self, locator):
        """Click via JavaScript, bypassing simulated mouse movement.
        Use this when a real click works but Selenium's native click
        doesn't (e.g. widgets that react to hover on the path to the target)."""
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].click();", element)

    def type_text(self, locator, text):
        """Clear field and type text."""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        """Return visible text of an element."""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text.strip()

    def scroll_into_view(self, locator):
        """Scroll the given element into the visible viewport."""
        element = self.find(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def wait_and_accept_alert(self, timeout=10):
        """Wait for a native browser alert (e.g. delete confirmation) and accept it."""
        alert = WebDriverWait(self.driver, timeout).until(EC.alert_is_present())
        alert.accept()