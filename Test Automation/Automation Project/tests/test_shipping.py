import pytest
from pages.login_page import LoginPage
from pages.shop_page import ShopPage
from pages.checkout_page import CheckoutPage
from utils.constants import AUTH_URL, SHOP_URL, CHECKOUT_URL, TEST_USER, SHIPPING_FEE


@pytest.mark.parametrize("quantity, expected_free", [
    (1, False),
    (30, True),
])
def test_shipping_cost(driver, quantity, expected_free):
    login_page = LoginPage(driver)
    login_page.open(AUTH_URL)
    login_page.login(TEST_USER["email"], TEST_USER["password"])

    checkout_page = CheckoutPage(driver)
    checkout_page.open(CHECKOUT_URL)
    checkout_page.clear_cart()

    shop_page = ShopPage(driver)
    shop_page.open(SHOP_URL)
    shop_page.confirm_age("01-01-1990")
    shop_page.add_first_product_to_cart(quantity)

    checkout_page.open(CHECKOUT_URL)
    shipping_value = float(checkout_page.get_shipping_cost().replace("€", ""))

    if expected_free:
        assert shipping_value == 0
    else:
        assert shipping_value == SHIPPING_FEE