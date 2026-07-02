# XPath Task 2

1. Write the XPath for the highlighted icon/button.

```xpath
//div[@class="headerIcon"][1]
```

2. Write the XPath of all input fields (Email address, Password), sign in button, Create a new account link, and Go to Home link.

```xpath
//input[@type="email"]
//input[@type="password"]
//button[@class="submit-btn"]
//a[@class="switch-link"][text()="Create a new account"]
//a[@class="home-link"][text()="Go to Home"]
```

3. Write the XPath for all input fields (Full Name, Email address, Password), Sign Up button.

```xpath
//input[@type="text"][@placeholder="Full Name"]  # added placeholder bc type="text" seems too generic
//input[@type="email"]
//input[@type="password"]
//button[@class="submit-btn"]
```

4. Write the XPath of the Confirm button in the Modal.

```xpath
//button[text()="Confirm"]
```

5. Go to the **Shop** page, write the XPath for:

   1. Quantity input of Oranges

```xpath
   //p[@class="lead"][text()="Oranges"]/ancestor::div[@class="card"]//input[@class="quantity"]
```

   2. Add to cart button for Oranges

```xpath
   //p[@class="lead"][text()="Oranges"]/ancestor::div[@class="card"]//button[contains(@class, "btn-cart")]
```

   3. Add to wish list for Oranges

```xpath
   //p[@class="lead"][text()="Oranges"]/ancestor::div[@class="card"]//button[text()="❤"]
```

   Alternative:

```xpath
   //p[@class="lead"][text()="Oranges"]/ancestor::div[@class="card"]//div[@class="col-1"]/button
```