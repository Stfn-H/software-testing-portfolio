from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Setup
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

# Login
username = driver.find_element(By.ID, "user-name")
password = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "login-button")
username.send_keys("standard_user")
password.send_keys("secret_sauce")
login_button.click()
time.sleep(2)

# Verify Login
login_verification = driver.find_element(By.CSS_SELECTOR, "[data-test='title']")
assert login_verification.text == "Products"

# Verify presence of "Sauce Labs Backpack" on Product Page
products = driver.find_elements(By.CSS_SELECTOR,"[data-test='inventory-item-name']")
product_names = []
for p in products:
    product_names.append(p.text)
assert "Sauce Labs Backpack" in product_names

driver.quit()