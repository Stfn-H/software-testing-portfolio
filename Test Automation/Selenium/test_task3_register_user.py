from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

USERNAME = "Test-User"


def test_register_user(driver):
    # Step 1&2: Launch browser and navigate to home page
    driver.get("https://automationexercise.com")

    # Step 3: Verify home page is visible
    assert driver.title == "Automation Exercise"

    # Handle cookie consent (not in task steps, but required for automation)
    try:
        cookie_button = driver.find_element(By.CSS_SELECTOR, ".fc-cta-consent")
        cookie_button.click()
    except:
        pass

    # Step 4: Click on 'Signup / Login' button
    login_link = driver.find_element(By.LINK_TEXT, "Signup / Login")
    # Using JavaScript click to bypass ad overlays
    driver.execute_script("arguments[0].click();", login_link)

    # Step 5: Verify 'New User Signup!' is visible
    signup_text = driver.find_element(By.CSS_SELECTOR, ".signup-form h2")
    assert signup_text.text == "New User Signup!"

    # Step 6: Enter name and email address
    name_field = driver.find_element(By.CSS_SELECTOR, "[data-qa='signup-name']")
    name_field.send_keys(USERNAME)
    email_field = driver.find_element(By.CSS_SELECTOR, "[data-qa='signup-email']")
    email_field.send_keys("testuser@test.de")

    # Step 7: Click 'Signup' button
    signup_button = driver.find_element(By.CSS_SELECTOR, "[data-qa='signup-button']")
    # Using JavaScript click to bypass ad overlays
    driver.execute_script("arguments[0].click();", signup_button)

    # Step 8: Verify 'ENTER ACCOUNT INFORMATION' is visible
    signup_form_text = driver.find_element(By.CSS_SELECTOR, ".login-form b")
    assert signup_form_text.text == "ENTER ACCOUNT INFORMATION"

    # Step 9: Fill details: Title, Password, Date of Birth
    title_selection = driver.find_element(By.ID, "uniform-id_gender1")
    title_selection.click()
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("password123")
    dropdown_day = driver.find_element(By.ID, "days")
    Select(dropdown_day).select_by_visible_text("19")
    dropdown_month = driver.find_element(By.ID, "months")
    Select(dropdown_month).select_by_visible_text("May")
    dropdown_year = driver.find_element(By.ID, "years")
    Select(dropdown_year).select_by_visible_text("1987")

    # Step 10: Select checkbox 'Sign up for our newsletter!'
    checkbox_newsletter = driver.find_element(By.ID, "newsletter")
    checkbox_newsletter.click()

    # Step 11: Select checkbox 'Receive special offers from our partners!'
    checkbox_offers = driver.find_element(By.ID, "optin")
    checkbox_offers.click()

    # Step 12: Fill address information
    first_name_field = driver.find_element(By.ID, "first_name")
    first_name_field.send_keys("Test-User")
    last_name_field = driver.find_element(By.ID, "last_name")
    last_name_field.send_keys("Selenium")
    company_field = driver.find_element(By.ID, "company")
    company_field.send_keys("Masterschool")
    address1 = driver.find_element(By.ID, "address1")
    address1.send_keys("Test Street")
    address2 = driver.find_element(By.ID, "address2")
    address2.send_keys("Test Building")
    country = driver.find_element(By.ID, "country")
    Select(country).select_by_visible_text("Canada")
    state_field = driver.find_element(By.ID, "state")
    state_field.send_keys("Test-State")
    city_field = driver.find_element(By.ID, "city")
    city_field.send_keys("Toronto")
    zipcode_field = driver.find_element(By.ID, "zipcode")
    zipcode_field.send_keys("10551")
    mobile_field = driver.find_element(By.ID, "mobile_number")
    mobile_field.send_keys("0123456789")

    # Step 13: Click 'Create Account' button
    create_acc_button = driver.find_element(By.CSS_SELECTOR, "[data-qa='create-account']")
    # Using JavaScript click to bypass ad overlays
    driver.execute_script("arguments[0].click();", create_acc_button)

    # Step 14: Verify 'ACCOUNT CREATED!' is visible
    account_created = driver.find_element(By.CSS_SELECTOR, "[data-qa='account-created'] b")
    assert account_created.text == "ACCOUNT CREATED!"

    # Step 15: Click 'Continue' button
    continue_button = driver.find_element(By.CSS_SELECTOR, "[data-qa='continue-button']")
    # Using JavaScript click to bypass ad overlays
    driver.execute_script("arguments[0].click();", continue_button)

    # Step 16: Verify 'Logged in as username' is visible
    login_check = driver.find_element(By.PARTIAL_LINK_TEXT, "Logged in as")
    assert USERNAME in login_check.text

    # Step 17: Click 'Delete Account' button
    delete_acc_button = driver.find_element(By.LINK_TEXT, "Delete Account")
    # Using JavaScript click to bypass ad overlays
    driver.execute_script("arguments[0].click();", delete_acc_button)

    # Step 18: Verify 'ACCOUNT DELETED!' is visible and click 'Continue'
    account_deleted = driver.find_element(By.CSS_SELECTOR, "[data-qa='account-deleted']")
    assert account_deleted.text == "ACCOUNT DELETED!"
    continue_button = driver.find_element(By.CSS_SELECTOR, "[data-qa='continue-button']")
    continue_button.click()