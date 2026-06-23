from selenium.webdriver.common.by import By
import pytest

PASSWORD = "secret_sauce"

@pytest.mark.parametrize("username", [
    "standard_user",
    "locked_out_user",
    "problem_user",
    "performance_glitch_user",
    "error_user",
    "visual_user"
])

def test_login(driver, username):
    # Navigate to login page
    driver.get("https://www.saucedemo.com/")
    # Login with parametrized username
    username_field = driver.find_element(By.ID, "user-name")
    password_field = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")
    username_field.send_keys(username)
    password_field.send_keys(PASSWORD)
    login_button.click()

    # Verify successful login
    login_verification = driver.find_element(By.CSS_SELECTOR, "[data-test='title']")
    assert login_verification.text == "Products"

