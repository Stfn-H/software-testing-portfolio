# GroceryMate Test Automation

This is my final project for the Test Automation part of the QA track. I automated some of the test cases from my earlier Test Plan & Test Case Design assignment, using Selenium and pytest with the Page Object Model pattern.

## What this project does

The site under test is grocerymate.masterschool.com. I automated 11 test cases covering three new features:

- Product Rating System
- Age Verification for alcoholic products
- Shipping Cost Logic

I didn't automate every test case from my original design. Some would have needed things like three separate user accounts, or the expected behavior was never really clarified (marked `[TBD]` in my test plan), so I left those out. More details on which test cases got automated and why (or why not) are in `PROJECT_NOTES.md`.

## Project structure

```
pages/
  base_page.py       # shared Selenium helper methods (click, type_text, waits, etc.)
  login_page.py
  shop_page.py        # the store page: age modal, add to cart
  checkout_page.py    # cart totals, shipping cost, clearing the cart
  product_page.py     # product detail page: rating

tests/
  conftest.py          # webdriver fixture
  test_shipping.py
  test_age_verification.py
  test_rating.py

utils/
  constants.py          # urls, test account, expected messages - nothing hardcoded in the tests
```

## How to run it

Install the requirements:
```
pip install selenium pytest pytest-html
```

Run all tests:
```
pytest tests/ -v
```

Generate an HTML report:
```
pytest tests/ --html=report.html --self-contained-html -v
```

## Test account

There's a dedicated test account (see `utils/constants.py`) that already bought "Pink Lady Apples", since the rating tests need a product that was actually purchased.

## A few things worth knowing

- The site's SSL certificate is expired, so the driver gets started with `--ignore-certificate-errors` in `conftest.py`.
- A couple of tests are written to pass *while* a known bug still exists, and this is on purpose. For example, the age verification deep-link bypass, and the fact that there's no separate "invalid format" message for the age field - both are documented as comments right above the test. If these ever get fixed on the site, these specific tests would start failing, which is expected behavior for a regression test.
- The shipping tests use 1 item vs. 30 items instead of testing the exact boundary value, because the real product prices don't add up cleanly to an exact 20€ threshold. So this ended up being closer to Equivalence Partitioning than the Boundary Value Analysis from my original test design.

## Known limitations

- Only one browser (Chrome) was tested.
- Tests run against the live grocerymate.masterschool.com site, not a local/staging copy, so they depend on that site being reachable.