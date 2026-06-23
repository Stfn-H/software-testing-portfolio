import pytest
from selenium import webdriver

@pytest.fixture()
def driver():
    # Setup: Initialize the WebDriver
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
