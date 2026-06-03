# **Test Plan: Market Mate Webshop – New Features**

---

## **1. Analyze the Product**

### **Objective**

The objective of this test plan is to verify the correct implementation of three new features added to the Market Mate webshop (`grocerymate.masterschool.com`): a **Product Rating System**, an **Age Verification for Alcoholic Products**, and updated **Shipping Cost Logic**. Testing ensures that these features function reliably, are secure, provide a good user experience, and integrate correctly with existing shop functionality.

### **User Base**

The webshop is used by:

- **Guest users** – browsing products and potentially interacting with ratings (read-only)
- **Registered users** – placing orders, writing reviews, and going through the checkout process
- **Users of varying ages** – the age verification feature is specifically relevant for users attempting to access alcoholic product categories
- **All major device types** – desktop, laptop, tablet, and smartphone users

### **Hardware and Software Specifications**

- **Hardware Requirements:**
  - Devices: PCs, laptops, smartphones, tablets
  - Specifications: Standard configurations; min. 4 GB RAM, modern processor

- **Software Requirements:**
  - Operating Systems: Windows, macOS, Android, iOS
  - Browsers: Chrome, Firefox, Safari, Edge (latest stable versions)
  - Dependencies: Session/cookie management, payment gateway, backend API

### **Product Functionality**

The webshop allows users to:

- Register and log in
- Search for products, filter by category, and sort by price
- Add products to a favorites/wishlist
- Add products to the shopping basket
- Complete a checkout process (billing/shipping info, payment, cost calculation)
- **[NEW]** Rate products using a 5-star system and optionally add written feedback
- **[NEW]** Access the alcoholic products category only after completing an age verification modal (18+)
- **[NEW]** See dynamically calculated shipping costs based on order total (free shipping above a defined threshold)

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
- Third-party payment gateway internals
- Admin/moderation backend for rating approval (unless a UI exists)
- Performance testing under heavy load (separate phase)

### **Types of Testing**

- **Functional Testing** – core feature behavior matches requirements
- **Boundary Value Testing** – age inputs at/around 18, cart totals at/around the shipping threshold
- **Negative Testing** – invalid inputs, underage users, empty form fields
- **Regression Testing** – ensure existing cart and checkout flow is unaffected by shipping cost changes
- **Usability Testing** – modals, rating UI, and dynamic shipping display are intuitive
- **Security Testing** – age verification bypass attempts (direct URL, deep links)

### **Risks and Issues**

- **Unanswered Requirements (open QA questions):** Several behaviors are not yet specified (see requirements). These are flagged as `[⚠️ TBD – clarification needed]` throughout this plan.
  - *Mitigation:* Escalate to Product Owner before test case execution begins.
- **Test Data Availability:** Accounts of different types (verified buyer, guest, underage) are needed.
  - *Mitigation:* Create dedicated test accounts in the test environment.
- **Environment Instability:** Test environment may not fully mirror production.
  - *Mitigation:* Use a dedicated staging environment (TEST/ACC).

### **Test Logistics**

| Role | Responsibility |
|---|---|
| `[⚠️ TBD]` Test Manager | Test planning, sign-off coordination |
| `[⚠️ TBD]` QA Engineer 1 | Functional & Regression Testing |
| `[⚠️ TBD]` QA Engineer 2 | Security & Boundary Testing |
| `[⚠️ TBD]` End User / UAT | Usability acceptance |

---

## **3. Define Test Objectives**

### **Objectives**

- **Functionality:** Ensure all three new features work as described in the requirements
- **Security:** Verify the age verification cannot be bypassed via direct URL or deep links
- **Data Integrity:** Confirm ratings are stored correctly and average scores are calculated accurately
- **GUI/UX:** Verify that the rating UI, age modal, and shipping cost display are clear and consistent across browsers and devices
- **Regression:** Confirm no existing checkout or cart functionality is broken by the shipping cost changes

### **Expected Outcomes**

- **Rating System:** Users can submit a star rating (and optionally text); average ratings display correctly; unauthorized submissions are blocked
- **Age Verification:** Users under 18 cannot access alcoholic product pages; the modal behaves correctly on cancellation and on direct deep links
- **Shipping Costs:** Shipping fee is correctly applied or waived based on cart total; the cart shows dynamic feedback on progress toward free shipping

---

## **4. Define Test Criteria**

### **Suspension Criteria**

- Testing will be suspended if a blocker-level defect prevents access to a core feature under test
- Testing will be suspended if the test environment is unavailable or returns incorrect data
- Open QA questions (marked `[⚠️ TBD]`) have not been answered before execution begins

### **Exit Criteria**

- At least **95%** of planned test cases have been executed
- At least **90%** of executed test cases have passed
- All **Severity 1 and Severity 2** defects have been resolved and closed
- All `[⚠️ TBD]` items have been clarified and re-tested where applicable
- Regression suite passes with no new failures
- UAT sign-off obtained from a designated end user

---

## **5. Resource Planning**

- **Human Resources:** QA team (2–3 engineers), Product Owner (for open questions), Development team (for defect fixes), End users for UAT
- **Hardware:** PCs, laptops, smartphones, tablets
- **Software:** Chrome, Firefox, Safari, Edge; Windows, macOS, Android, iOS
- **Test Data:** Test accounts (guest, registered buyer, underage user), products in alcoholic category, voucher/discount codes
- **Infrastructure:** Staging environment (TEST), Acceptance environment (ACC)
- **Tools:** Bug tracking tool (e.g. Jira), test case management (e.g. TestRail or spreadsheet)

---

## **6. Plan Test Environment**

| Environment | Purpose | Who |
|---|---|---|
| DEV | Developer unit testing | Development Team |
| TEST | Functional, regression, security, and boundary testing | QA Team |
| ACC | User Acceptance Testing (UAT) | End Users |
| PROD | Final production release | DevOps / Release Manager |

Testing will be conducted on real browsers and devices to simulate actual user conditions. Both desktop and mobile viewports must be covered for the age verification modal and shipping cost display.

---

## **7. Schedule and Estimation**

> Note: Dates are placeholders and should be replaced with actual project dates.

| Activity | Start Date | End Date | Environment | Responsible | Estimated Effort |
|---|---|---|---|---|---|
| Test Planning | `[⚠️ TBD]` | `[⚠️ TBD]` | All | Test Manager | 10 hours |
| Requirements Clarification | `[⚠️ TBD]` | `[⚠️ TBD]` | – | QA + PO | 5 hours |
| Test Case Design | `[⚠️ TBD]` | `[⚠️ TBD]` | – | QA Team | 15 hours |
| Functional Testing | `[⚠️ TBD]` | `[⚠️ TBD]` | TEST | QA Team | 20 hours |
| Boundary & Negative Testing | `[⚠️ TBD]` | `[⚠️ TBD]` | TEST | QA Team | 10 hours |
| Security Testing (Age Bypass) | `[⚠️ TBD]` | `[⚠️ TBD]` | TEST | QA Team | 5 hours |
| Regression Testing | `[⚠️ TBD]` | `[⚠️ TBD]` | TEST | QA Team | 10 hours |
| UAT | `[⚠️ TBD]` | `[⚠️ TBD]` | ACC | End Users | 8 hours |
| Production Release | `[⚠️ TBD]` | `[⚠️ TBD]` | PROD | DevOps | 2 hours |

---

## **8. Determine Test Deliverables**

| Deliverable | Description |
|---|---|
| **This Test Plan** | Documents the overall test strategy and scope |
| **Test Cases** | Detailed test cases per feature (see Test Case Design document) |
| **Test Data Setup Guide** | Instructions for creating required test accounts and data |
| **Bug/Defect Reports** | Logged in bug tracking tool for each discovered defect |
| **Test Execution Report** | Summary of pass/fail results after each test cycle |
| **UAT Sign-off Document** | Formal approval from end user representative |

---

## **Appendix: Open Questions (`[⚠️ TBD]`)**

The following questions from the requirements analysis have not yet been answered and must be clarified with the Product Owner before test execution:

**Product Rating System:**
- Who may submit a rating – verified buyers only, or all logged-in users?
- Is a star rating required, or can a user submit text-only feedback?
- Is there a character minimum/maximum for text reviews?
- What are the rounding rules for average ratings?
- Are half-stars displayed in the UI?
- How is a product with no ratings displayed?

**Age Verification:**
- What input method is used (free-text, dropdown, or date picker)?
- Does the check use birth year only, or the exact calendar date?
- What happens to underage users – full lockout, redirect, or category block only?
- What happens if the modal is closed without input (ESC, click outside)?
- Is the verification session-persistent (cookie) or triggered on every visit?
- Is the check enforced when landing directly on an alcoholic product via direct URL or search engine?

**Shipping Costs:**
- What is the exact free shipping threshold (e.g. €30, €50)?
- What is the shipping fee below the threshold?
- Are there multiple shipping tiers (standard vs. express)?
- Is the threshold calculated on the cart total before or after discounts/vouchers?
- Is there a dynamic progress indicator in the cart ("Spend €X more for free shipping")?
- Do premium/special user groups always get free shipping?
- How are partial returns handled if the remaining order falls below the threshold?
