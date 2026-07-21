import pytest
from pages.shop_page import ShopPage
from utils.constants import (
    SHOP_URL, AGE_18, AGE_17, INVALID_AGE_INPUT, ALCOHOL_PRODUCT_URL,
    AGE_OK_MESSAGE, UNDERAGE_MESSAGE
)


@pytest.mark.parametrize("birthdate, expected_message", [
    (AGE_18, AGE_OK_MESSAGE),
    (AGE_17, UNDERAGE_MESSAGE),
])
def test_age_boundary(driver, birthdate, expected_message):
    shop_page = ShopPage(driver)
    shop_page.open(SHOP_URL)
    shop_page.submit_age(birthdate)
    assert shop_page.get_status_message() == expected_message


def test_invalid_age_input(driver):
    # The site has no dedicated "invalid format" state (matches a bug
    # found during manual testing): any input that isn't a valid 18+
    # date is treated as underage.
    shop_page = ShopPage(driver)
    shop_page.open(SHOP_URL)
    shop_page.submit_age(INVALID_AGE_INPUT)
    assert shop_page.get_status_message() == UNDERAGE_MESSAGE


def test_age_verification_deep_link_bypass(driver):
    # Known bug (found during manual testing phase): the age verification
    # modal does not appear when navigating directly to an alcoholic
    # product URL, bypassing the age check entirely.
    shop_page = ShopPage(driver)
    shop_page.open(ALCOHOL_PRODUCT_URL)
    assert shop_page.is_visible(shop_page.AGE_MODAL_CONTAINER, timeout=3) is False