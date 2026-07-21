import datetime

BASE_URL = "http://grocerymate.masterschool.com"
AUTH_URL = f"{BASE_URL}/auth"
SHOP_URL = f"{BASE_URL}/store"
CHECKOUT_URL = f"{BASE_URL}/checkout"

# Fake Test User for Testing Purpose - No Sensible Data
TEST_USER = {
    "email": "testing10@grocerymate.com",
    "password": "yJu7eyvpI9XcEjD"
}

SHIPPING_FEE = 5.00

AGE_OK_MESSAGE = "You are of age. You can now view all products, even alcohol products."
UNDERAGE_MESSAGE = "You are underage. You can still browse the site, but you will not be able to view alcohol products."

TODAY = datetime.date.today()
AGE_18 = TODAY.replace(year=TODAY.year - 18).strftime("%d-%m-%Y")
AGE_17 = TODAY.replace(year=TODAY.year - 17).strftime("%d-%m-%Y")
INVALID_AGE_INPUT = "abc"

ALCOHOL_PRODUCT_URL = f"{BASE_URL}/product/66b3a57b3fd5048eacb47a7b"

PURCHASED_PRODUCT_URL = f"{BASE_URL}/product/66b3a57b3fd5048eacb4799b"
NOT_BOUGHT_MESSAGE = "You need to buy this product to tell us your opinion!"
INVALID_RATING_MESSAGE = "Invalid input for the field 'Rating'. Please check your input."