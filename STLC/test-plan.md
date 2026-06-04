# **Test Plan: Market Mate Webshop – New Features**

---

## **1. Analyze the Product**

### **Objective**

The objective of this test plan is to verify the correct implementation of three new features added to the Market Mate webshop (`grocerymate.masterschool.com`):

- **Product Rating System**
- **Age Verification for Alcoholic Products**
- **Shipping Cost Logic**. 

Testing ensures that these features function reliably, are secure, provide a good user experience, and integrate correctly with existing shop functionality.

### **User Base**

The webshop is used by:

- **Guest users** – browsing products and potentially interacting with ratings (read-only)
- **Registered users** – placing orders, writing reviews, and going through the checkout process
- **Users of varying ages** – the age verification feature is specifically relevant for users attempting to access alcoholic product categories
- **All major device types** – desktop, laptop, tablet, and smartphone users

### **Hardware and Software Specifications**

- **Hardware Requirements:**
  - Devices: PCs, laptops, smartphones, tablets
  - Specifications: Standard configurations
  - Internet Access

- **Software Requirements:**
  - Operating Systems: Windows, macOS, Android, iOS
  - Browsers: Chrome, Firefox, Safari, Edge 
  - Dependencies: Session/cookie management, payment gateway, backend API

### **Product Functionality**

The webshop allows users to:

- Register and log in
- Search for products, filter by category, and sort by price
- Add products to a favorites/wishlist
- Add products to the shopping basket
- Check-out process: billing and sending information in a form, choose payment method. Calculation of costs (calculate total price)
- **[NEW]** Users should be able to rate products using a 5-star system and have the option to add written feedback
- **[NEW]** Alcoholic products require age verification; 18+
- **[NEW]** Free shipping applies to orders above a certain threshold. Orders below this amount will incur a shipping fee

---

## **2. Design the Test Strategy**

### **Scope of Testing**

**In Scope:**

- Product Rating System (star rating + written feedback)
- Age Verification Modal (alcoholic products category)
- Shipping Cost Logic (threshold-based free shipping, dynamic cart display)
- Regression testing of existing checkout and cart functionality affected by shipping cost changes

**Out of Scope:**

- Backend database operations not affecting the user interface
- Third-party payment gateway 
- Admin/moderation backend for rating approval
- Performance testing under heavy load 

### **Types of Testing**

- **Functional Testing** – core feature behavior matches requirements
- **Boundary Value Testing** – age inputs at/around 18, cart totals at/around the shipping threshold
- **Negative Testing** – invalid inputs, underage users, empty form fields
- **Regression Testing** – ensure existing cart and checkout flow is unaffected by shipping cost changes
- **Usability Testing** – modals, rating UI, and dynamic shipping display are intuitive
- **Security Testing** – age verification bypass (direct URL...)

### **Risks and Issues**

- **Unanswered Requirements (open QA questions):** Several behaviors are not yet specified (see requirements). These are flagged as `[TBD – clarification needed]` 
  - *Mitigation:* Escalate to Product Owner before test case execution begins
- **Test Data Availability:** Accounts of different types are needed (verified buyer, guest, underage) are needed
  - *Mitigation:* Create dedicated test accounts in the test enviromment
- **Environment Instability:** Test environment may not fully mirror production
  - *Mitigation:* Use a dedicated staging environment

### **Test Logistics**

| Role | Responsibility |
|---|---|
| Test Manager | Test planning, sign-off coordination |
| QA Engineer |  Functional, Regression, Security & Boundary Testing  |
| End User / UAT | User acceptance Test |

---

## **3. Define Test Objectives**

### **Objectives**

- **Functionality:** Ensure all three new features work as described in the requirements
- **Security:** Verify the age verification cannot be bypassed via direct URL 
- **Data Integrity:** Confirm ratings are stored correctly and average scores are calculated accurately
- **GUI/UX:** Verify that the rating UI, age modal, and shipping cost display are clear and consistent across browsers and devices
- **Regression:** Confirm no existing checkout or cart functionality is broken by the shipping cost changes

### **Expected Outcomes**

- **Rating System:** Users can submit a star rating (and optionally text); average ratings display correctly; unauthorized submissions are blocked
- **Age Verification:** Users under 18 cannot access alcoholic product pages; the website behaves correctly on cancellation and on direct links
- **Shipping Costs:** Shipping fee is correctly applied or waived based on cart total; the cart shows dynamic feedback on progress toward free shipping

---

## **4. Define Test Criteria**

### **Suspension Criteria**

- Testing will be suspended if critical defects are found that block further testing.
- Open QA questions (marked `[TBD]`) have not been answered before execution begins

### **Exit Criteria**

- All planned tetts have been executed
- Run Rate: At least **95%** of planned test cases have been executed
- Pass Rate: At least **90%** of executed test cases have passed
- All critical and high-priority defects have been resolved and closed.
- No severity 1 or severity 2 defects are open.
- All `[TBD]` items have been clarified and re-tested where applicable
- Regression suite passes with no new failures
- User acceptance testing has been completed, and sign-off has been obtained.

---

## **5. Resource Planning**

- **Human Resources:** QA team, Product Owner, Development team, End users for UAT
- **Hardware:** PCs, laptops, smartphones, tablets
- **Software:** Chrome, Firefox, Safari, Edge; Windows, macOS, Android, iOS
- **Test Data:** Test accounts (guest, registered buyer, underage user), products in alcoholic category, voucher/discount codes
- **Infrastructure:** Test environments, automation tools, performance testing tools

---

## **6. Plan Test Environment**

- **Test Environments:** Real devices installed with real browsers and operating systems to simulate user conditions.
- **Environments:** Development (DEV), Testing (TEST), Acceptance (ACC), Production (PROD)

---

## **7. Schedule and Estimation**

| Activity | Start Date | End Date | Environment | Responsible | Estimated Effort |
|---|---|---|---|---|---|
| Test Planning | [TBD] | [TBD] | All | Test Manager | [TBD] |
| Requirements Clarification | [TBD] | [TBD] | – | QA Engineer & PO | [TBD] |
| Test Case Design | [TBD] | [TBD] | All | QA Engineer | [TBD] |
| Unit Testing | [TBD] | [TBD] | DEV | Development Team | [TBD] |
| Integration Testing | [TBD] | [TBD] | TEST | QA Engineer | [TBD] |
| System Testing | [TBD] | [TBD] | TEST | QA Engineer | [TBD] |
| Regression Testing | [TBD] | [TBD] | TEST | QA Engineer | [TBD] |
| Performance Testing | [TBD] | [TBD] | TEST | QA Engineer | [TBD] |
| Security Testing | [TBD] | [TBD] | TEST | QA Engineer | [TBD] |
| UAT | [TBD] | [TBD] | ACC | End Users | [TBD] |
| Production Release | [TBD] | [TBD] | Production Release | DevOps Team| [TBD] |

---

## **8. Determine Test Deliverables**

Documents/tools that must be created to support testing activities in the project:

- **Test Plan Document**
- **Test Cases and Test Scripts**
- **Test Data**
- **Test Reports**
- **Defect Reports**
- **UAT Sign-off Document**

---

## **Appendix: Open Questions (`[TBD]`)**

The following questions from the [requirements analysis](https://github.com/Stfn-H/software-testing-portfolio/blob/main/STLC/requirements.md) have not yet been answered and must be clarified before test execution:

**Product Rating System:**
- **Authorization:** Who is allowed to leave a rating (verified buyers vs. all visitors)?
- **Identity:** Is a login required or is anonymous feedback allowed?
- **Mandatory Fields:** Are the star rating and the text review independent or optional?
- **Moderation:** Is there an approval/moderation workflow for texts (spam prevention/hate speech filter)?
- **Calculation:** How are average ratings calculated? What are the rounding rules?
- **UI/UX:** Are half-stars displayed? How is a product with no ratings visualized (0 stars vs. "No ratings yet")?
- **Feedback Limits:** What is the character limit (min/max)? Are emojis supported?

**Age Verification:**
- **Input Method:** Is it a free-text field, a dropdown menu, or a date picker? How do we prevent invalid characters (letters, special characters)?
- **Thresholds:** Does it check the birth year or the exact current calendar date? How does the system handle users turning exactly 18 today or tomorrow?
- **Error Scenarios:** What happens if a user enters an age under 18? Are they completely locked out, redirected to the homepage, or just blocked from this specific category?
- **Cancellation Behavior:** What happens if the user closes the modal without entering anything (e.g., clicking outside the window or pressing the ESC key)?
- **Session Management:** Does the age check trigger on every single visit to the category, or does the system remember the state via a session cookie?
- **Security:** Is the check enforced if a user lands directly on an alcoholic product via a search engine or a direct deep link, bypassing the category page?

**Shipping Cost Changes:**
- **Thresholds:** What is the exact threshold for free shipping, and what is the fee below it? Are there different tiers (e.g., standard vs. express)?
- **Calculation Base:** Which amount is used for the calculation? Is it the cart value before or after applying discounts and voucher codes?
- **UI/UX:** Is there a dynamic display in the shopping basket showing the user how much more they need to spend to get free shipping?
- **Special Roles:** Are there specific user groups (e.g., premium members) who always get free shipping regardless of the order value?
- **Return Logic:** How does the system behave regarding partial returns if the remaining order value drops below the original free shipping threshold?
