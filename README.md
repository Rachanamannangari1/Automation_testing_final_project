Project: Automating the Sauce Labs Website using Selenium & Python
Introduction
https://www.saucedemo.com/ is a sample website designed for testing purposes. It includes a user login page and an inventory page, where customers can select and purchase products.
The goal of this test automation project is to validate the functionality of the Sauce Labs website using Selenium and Python. I followed a structured approach using the Page Object Model (POM) and Pytest framework to ensure maintainability, reusability. 
The goals included:
•	Validating login functionality 
•	Automating product selection and checkout process
•	Ensuring UI elements are working correctly

Technologies Used:
•	Python – Programming language
•	Selenium WebDriver – Automating UI actions
•	Pytest – Test execution and reporting
•	Page Object Model (POM) – Improves maintainability
•	Poetry – Dependency management
•	HTML Report– Test reporting
•	GitHub – for version control
Folder structure
•	pages/ → Contains page classes (POM)
•	resources/ → Contains Constants.py
•	tests/ → Contains test cases, test_utils.py, conftest.py → Driver setup and fixtures

Test Cases
Test Case ID	Test Scenario	Test Case	Test Steps	Test Data 	Expected Result
TC-1	Verify Login Page	Verify whether user can login successfully using valid data	1.Open the Login page
2.Fill the “username” field with valid input
3.Fill the “password” field with valid password
4. Click on Login Button	1.https://www.saucedemo.com/"
2. standard_user
3. secret_sauce
4.Login Button
	User navigate in to inventory page https://www.saucedemo.com/inventory.html

TC-2	Verify products page	Verify the drop-down list checking whether the price (low to high) is working properly	1.Login using valid username and password
2.select price low to high from drop down list
3. Fetch all product prices and check whether all are sorted properly		1.https://www.saucedemo.com/"
2. standard_user
3. secret_sauce
4.Login Button
5.click on drop down list
6.select price low to high	 1.https://www.saucedemo.com/inventory.html
2.price”: [7.99, 9.99, 15.99, 15.99, 29.99, 49.99]

TC-3	Verify products page	Verify selected item from the product list and verify add to cart button and checking correct number of items displayed on the cart 	1.Login using valid username and password
2.select price low to high from drop down list
3.Click on one item name

4.click on add to cart
5.select number displayed on the cart	1.https://www.saucedemo.com/"
2. standard_user
3. secret_sauce
4.Login Button
5.click on product name” Sauce Labs Bike Light”
6.Button “Add to cart”
7.verify the number displayed on the cart
	1.https://www.saucedemo.com/inventory.html

2.User navigate in to item page https://www.saucedemo.com/inventory-item.html?id=0
3. expected cart_number":"1"


TC-4	Verify Shopping cart page	Verify the item and price displayed in the shopping cart and verify “Checkout” button	1.Login using valid username and password
2.select price low to high from drop down list
3.Click on one item name

4.click on add to cart
5.Verify name and price of the selected Item.
6.click on Checkout button	1.https://www.saucedemo.com/"
2. standard_user
3. secret_sauce
4.Login Button
5.click on product name” Sauce Labs Bike Light”
6.Button “Add to cart
7.user navigate in to shopping cart page
8.Verify price and Name of the selected items
9.checkout button	
        1.https://www.saucedemo.com/inventory.html

2.User navigate in to item page https://www.saucedemo.com/inventory-item.html?id=0
3.Redirect in to https://www.saucedemo.com/cart.html
4. "item_name":"Sauce Labs Bike Light",
"item_price":"$9.99"
5.Navigate in to check out page” https://www.saucedemo.com/checkout-step-one.html

        
TC-5	Verify check out page	Verify checkout step one and two pages	1.Login using valid username and password
2.select price low to high from drop down list
3.Click on one item name

4.click on add to cart
5.Verify name and price of the selected Item.
6.click on Checkout button
7.Enter First Name
8.Enter second name
9.Enter postal code
10.click on continue button
11. Navigate in to checkout-step-two page,
12.check Total price	1.https://www.saucedemo.com/"
2. standard_user
3. secret_sauce
4.Login Button
5.click on product name” Sauce Labs Bike Light”
6.Button “Add to cart
7.user navigate in to shopping cart page
8.Verify price and Name of the selected items
9.checkout button
10.Enter” Rachana”
11.”M”
12. 112233
13.continue Button
14.verify current URL and Total price	
        1.https://www.saucedemo.com/inventory.html

2.User navigate in to item page https://www.saucedemo.com/inventory-item.html?id=0
3.Redirect in to https://www.saucedemo.com/cart.html
4. "item_name":"Sauce Labs Bike Light",
"item_price":"$9.99"
5.Navigate in to check out page” https://www.saucedemo.com/checkout-step-one.html
6.Navigate in to “https://www.saucedemo.com/checkout-step-two.html
Price Total”: “Total: $10.79"



        
TC-6	Verify Check out complete page	Verify the finish button and make sure order has been dispatched	1.Login using valid username and password
2.select price low to high from drop down list
3.Click on one item name

4.click on add to cart
5.Verify name and price of the selected Item.
6.click on Checkout button
7.Enter First Name
8.Enter second name
9.Enter postal code
10.click on continue button
11. Navigate in to checkout-step-two page,
12.click on Finish button
13.Verify order complete URL and text	1.https://www.saucedemo.com/"
2. standard_user
3. secret_sauce
4.Login Button
5.click on product name” Sauce Labs Bike Light”
6.Button “Add to cart
7.user navigate in to shopping cart page
8.Verify price and Name of the selected items
9.checkout button
10.Enter” Rachana”
11.”M”
12. 112233
13.continue Button
14.Finish Button	https://www.saucedemo.com/inventory.html

2.User navigate in to item page https://www.saucedemo.com/inventory-item.html?id=0
3.Redirect in to https://www.saucedemo.com/cart.html
4. "item_name":"Sauce Labs Bike Light",
"item_price":"$9.99"
5.Navigate in to check out page” https://www.saucedemo.com/checkout-step-one.html
6.Navigate in to 7. “https://www.saucedemo.com/checkout-step-two.html
8. order complete message”: “Thank you for your order!"
9. https://www.saucedemo.com/checkout-complete.html






TC-7	Verify Log Out functionality	Verify whether user can log out successfully	1.Open the Login page
2.Fill the “username” field with valid input
3.Fill the “password” field with valid password
4. Click on Login Button
5.Click on Menu link
6.Click on “Logout link”	1.https://www.saucedemo.com/"
2. standard_user
3. secret_sauce
4.Login Button
5.Menu Link
6.” Logout” link
	1.User navigate in to inventory page https://www.saucedemo.com/inventory.html
2. User navigate in to https://www.saucedemo.com/

GitHub Link
https://github.com/Rachanamannangari1/Automation_testing_final_project
Conclusion
To summarize, this project showcased how Selenium and Python can be used to automate web application testing efficiently. Automation not only speeds up the testing process but also ensures higher software quality.
