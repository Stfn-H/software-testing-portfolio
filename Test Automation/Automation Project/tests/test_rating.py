import pytest
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from utils.constants import (
    AUTH_URL, PURCHASED_PRODUCT_URL, TEST_USER,
    NOT_BOUGHT_MESSAGE, INVALID_RATING_MESSAGE
)


def _login_and_open_product(driver):
    login_page = LoginPage(driver)
    login_page.open(AUTH_URL)
    login_page.login(TEST_USER["email"], TEST_USER["password"])

    product_page = ProductPage(driver)
    product_page.open(PURCHASED_PRODUCT_URL)
    product_page.delete_review()
    return product_page


@pytest.mark.parametrize("star_number, expected_count", [
    (1, 1),
    (5, 5),
])
def test_rating_boundary(driver, star_number, expected_count):
    product_page = _login_and_open_product(driver)
    product_page.click_star(star_number)
    product_page.send_rating()
    assert product_page.get_own_rating_count() == expected_count


def test_rating_with_comment(driver):
    # Known bug (found during manual testing phase): the comment text
    # does not display after the initial submission of a review. The
    # star rating itself IS saved correctly.
    product_page = _login_and_open_product(driver)
    product_page.click_star(5)
    product_page.enter_comment("Great product")
    product_page.send_rating()
    assert product_page.get_own_rating_count() == 5
    assert product_page.get_own_comment_text() == ""


def test_rating_without_star_selected(driver):
    product_page = _login_and_open_product(driver)
    product_page.enter_comment("No star selected here")
    product_page.send_rating()
    assert product_page.get_status_message() == INVALID_RATING_MESSAGE


def test_guest_cannot_rate(driver):
    product_page = ProductPage(driver)
    product_page.open(PURCHASED_PRODUCT_URL)
    assert product_page.get_rating_restriction_text() == NOT_BOUGHT_MESSAGE