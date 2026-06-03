# Requirements Analysis: Webshop Portfolio

## Basic Functionalities
The webshop includes the following standard features:
* **Registration and login functionality**
* **Product search**, sorting by price, and product categories
* Add products to **favorites** (wishlist)
* Add products to the **shopping basket**
* **Check-out process**: billing and shipping information in a form, payment method selection, and cost calculation (total price computation).

---

## New Features

### 1. Product Rating System
**Requirement:** Users should be able to rate products using a 5-star system and have the option to add written feedback.

#### Critical Questions (QA Perspective):
* **Authorization:** Who is allowed to leave a rating (verified buyers vs. all visitors)?
* **Identity:** Is a login required or is anonymous feedback allowed?
* **Mandatory Fields:** Are the star rating and the text review independent or optional?
* **Moderation:** Is there an approval/moderation workflow for texts (spam prevention/hate speech filter)?
* **Calculation:** How are average ratings calculated? What are the rounding rules?
* **UI/UX:** Are half-stars displayed? How is a product with no ratings visualized (0 stars vs. "No ratings yet")?
* **Feedback Limits:** What is the character limit (min/max)? Are emojis supported?

---

### 2. Age Verification for Alcoholic Products
**Requirement:** Alcoholic products require age verification. A modal should appear when navigating to the alcoholic products category, asking if the user is 18+. Users must input their age before gaining access.

#### Critical Questions (QA Perspective):
* **Input Method:** Is it a free-text field, a dropdown menu, or a date picker? How do we prevent invalid characters (letters, special characters)?
* **Thresholds:** Does it check the birth year or the exact current calendar date? How does the system handle users turning exactly 18 today or tomorrow?
* **Error Scenarios:** What happens if a user enters an age under 18? Are they completely locked out, redirected to the homepage, or just blocked from this specific category?
* **Cancellation Behavior:** What happens if the user closes the modal without entering anything (e.g., clicking outside the window or pressing the ESC key)?
* **Session Management:** Does the age check trigger on every single visit to the category, or does the system remember the state via a session cookie?
* **Security:** Is the check enforced if a user lands directly on an alcoholic product via a search engine or a direct deep link, bypassing the category page?

---

### 3. Shipping Cost Changes
**Requirement:** Free shipping applies to orders above a certain threshold. Orders below this amount will incur a shipping fee.

#### Critical Questions (QA Perspective):
* **Thresholds:** What is the exact threshold for free shipping, and what is the fee below it? Are there different tiers (e.g., standard vs. express)?
* **Calculation Base:** Which amount is used for the calculation? Is it the cart value before or after applying discounts and voucher codes?
* **UI/UX:** Is there a dynamic display in the shopping basket showing the user how much more they need to spend to get free shipping?
* **Special Roles:** Are there specific user groups (e.g., premium members) who always get free shipping regardless of the order value?
* **Return Logic:** How does the system behave regarding partial returns if the remaining order value drops below the original free shipping threshold?