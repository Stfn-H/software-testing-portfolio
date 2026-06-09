# **Test Case Design: Market Mate Webshop – New Features**

---

**Design your test cases, based on the features that will be developed for the upcoming release of the online grocery shop!**

**You only have to *design* them, the execution will happen in a later phase.**

**Add the test design technique, if applicable.**

---

## **1. Product Rating System**

**Test Design Techniques**: Boundary Value Analysis (BVA), Error Guessing, Use Case Testing

### **Test Cases:**

1. **Use Case Testing**:
    - **Test Case**: Verify that a registered user can submit a 5-star rating on a product.
        - **Input**: Logged-in user selects 5 stars on a product and submits.
        - **Expected Outcome**: Rating is saved and displayed on the product page.

2. **Use Case Testing**:
    - **Test Case**: Verify that a registered user can submit a written review alongside a star rating.
        - **Input**: Logged-in user selects 3 stars and enters written feedback, then submits.
        - **Expected Outcome**: Star rating and written feedback are both saved and displayed.

3. **Use Case Testing**:
    - **Test Case**: Verify that a guest user cannot submit a rating.
        - **Input**: Non-logged-in user attempts to submit a star rating.
        - **Expected Outcome**: User is prompted to log in or an error message is displayed.

4. **Use Case Testing**:
    - **Test Case**: Verify that the average rating is calculated correctly after multiple submissions.
        - **Input**: Three users submit ratings of 2, 4 and 5 stars.
        - **Expected Outcome**: Average rating displayed is 3.7 (or rounded per system rules).

5. **Boundary Value Analysis**:
    - **Test Case**: Verify that a user can submit the minimum (1 star) and maximum (5 stars) rating.
        - **Input**: Logged-in user submits a rating of 1 star. Repeated with 5 stars.
        - **Expected Outcome**: Both ratings are accepted and saved successfully.

6. **Error Guessing**:
    - **Test Case**: Verify system behavior when a user attempts to submit a rating without selecting stars.
        - **Input**: Logged-in user submits the rating form without selecting a star rating.
        - **Expected Outcome**: Error message is displayed indicating a star rating is required.

7. **Error Guessing**:
    - **Test Case**: Verify system behavior when a user submits written feedback only, without a star rating.
        - **Input**: Logged-in user enters text feedback but does not select stars, then submits.
        - **Expected Outcome**: Error message displayed or submission blocked (behavior [TBD] per requirements).

---

## **2. Age Verification for Alcoholic Products**

**Test Design Techniques**: Boundary Value Analysis (BVA), Equivalence Partitioning (EP), Error Guessing, Use Case Testing

### **Test Cases:**

1. **Boundary Value Analysis**:
    - **Test Case**: Verify that a user entering exactly 18 years of age is granted access to the alcoholic products category.
        - **Input**: User enters age = 18 in the verification modal.
        - **Expected Outcome**: Access to the alcoholic products category is granted.

2. **Boundary Value Analysis**:
    - **Test Case**: Verify that a user entering 17 years of age is denied access to the alcoholic products category.
        - **Input**: User enters age = 17 in the verification modal.
        - **Expected Outcome**: Access is denied and an appropriate message is displayed.

3. **Equivalence Partitioning**:
    - **Test Case**: Verify that a user well above the age threshold (e.g. 30 years) is granted access.
        - **Input**: User enters age = 30 in the verification modal.
        - **Expected Outcome**: Access to the alcoholic products category is granted.

4. **Error Guessing**:
    - **Test Case**: Verify system behavior when the user closes the modal without entering an age.
        - **Input**: User opens the age verification modal and closes it without input (e.g. ESC or click outside).
        - **Expected Outcome**: Access is denied and the user is redirected away from the category (behavior [TBD] per requirements).

5. **Error Guessing**:
    - **Test Case**: Verify system behavior when invalid characters are entered in the age field.
        - **Input**: User enters letters or special characters (e.g. "abc") in the age field.
        - **Expected Outcome**: Error message is displayed and submission is blocked.

6. **Use Case Testing (Security)**:
    - **Test Case**: Verify that the age verification is enforced when a user navigates directly to an alcoholic product via a deep link.
        - **Input**: User pastes a direct URL to an alcoholic product page into the browser without going through the category page.
        - **Expected Outcome**: Age verification modal appears before the product is accessible.

---

## **3. Shipping Cost Logic**

**Test Design Techniques**: Boundary Value Analysis (BVA), Equivalence Partitioning (EP), Error Guessing, Use Case Testing

### **Test Cases:**

1. **Boundary Value Analysis**:
    - **Test Case**: Verify that a cart total exactly at the free shipping threshold results in free shipping.
        - **Input**: Cart total = free shipping threshold (exact amount, [TBD] per requirements).
        - **Expected Outcome**: Shipping cost displayed as €0.00 / free.

2. **Boundary Value Analysis**:
    - **Test Case**: Verify that a cart total one cent below the free shipping threshold incurs a shipping fee.
        - **Input**: Cart total = free shipping threshold minus €0.01.
        - **Expected Outcome**: Shipping fee is applied and displayed in the cart.

3. **Equivalence Partitioning**:
    - **Test Case**: Verify that a cart total well below the threshold incurs the correct shipping fee.
        - **Input**: Cart total = €5.00.
        - **Expected Outcome**: Shipping fee is applied and correct amount is displayed.

4. **Equivalence Partitioning**:
    - **Test Case**: Verify that a cart total well above the threshold results in free shipping.
        - **Input**: Cart total = €100.00.
        - **Expected Outcome**: Shipping cost displayed as €0.00 / free.

5. **Use Case Testing**:
    - **Test Case**: Verify that the shipping cost updates dynamically when items are added or removed from the cart.
        - **Input**: User adds items until cart crosses the free shipping threshold, then removes one item to drop below it.
        - **Expected Outcome**: Shipping cost updates dynamically in real time to reflect the correct fee or free shipping.

6. **Error Guessing**:
    - **Test Case**: Verify that applying a discount voucher does not incorrectly grant free shipping when the post-discount total is below the threshold.
        - **Input**: Cart total before discount = above threshold. Cart total after discount = below threshold.
        - **Expected Outcome**: Shipping fee is applied based on the post-discount total (behavior [TBD] per requirements).

---

## **Automation Candidates**

The following test cases would be suitable for automation:

- **Rating System – Test Case 5** (boundary value 1 and 5 stars): The input and expected outcome are fixed and straightforward. This test is quick to run and should be repeated after any changes to the rating feature.
- **Rating System – Test Case 4** (average rating calculation): This test checks a calculation with a clear input and a clear expected result. It does not depend on the UI and can be run repeatedly without much effort.
- **Shipping Cost Logic – Test Cases 1 and 2** (boundary value at threshold): These tests use specific numbers and always expect the same result. They should be re-run whenever something changes in the cart or pricing logic.
- **Age Verification – Test Case 6** (deep link security check): This test should be automated to make sure the age check is not accidentally removed in a future update.

Tests that involve UI interactions, such as the age verification modal, the dynamic shipping display, or submitting written feedback, are better tested manually in the early stages, as the UI is likely to change during development.