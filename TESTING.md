# Full Testing
## Contents
+ [Validator Testing](#validator-testing)
+ [Lighthouse Testing](#lighthouse-testing)
+ [Testing From User Stories](#testing-from-user-stories)
+ [Testing Automated Tests](#testing-automated-tests)
+ [Manually Testing Functionality](#manually-testing-functionality)
+ [Responsive Testing](#responsive-testing)
+ [Bugs and Fixes](#bugs-and-fixes)
+ [Known Bugs](#known-bugs)
+ [Credentials](#kcredentials)

---
---

## Validator Results <a name="validator-testing"></a>

### HTML Results:
#### Home
* Home Page
![Home](testing_images/home-html-validator.png)<br>
* Sign up Page
![Signup](testing_images/register-page-html-validation.png)<br>
* Sign in Page
![Signin](testing_images/login-page-html-validation.png)<br>
* sign out Page
![Sign out](testing_images/logout-page-html-validation.png)<br>
* Contact Page
![Contact](testing_images/contact-page-html-validation.png)<br>
* Frequently Asked Questions Page
![Frequently Asked Questions](testing_images/faq-page-html-validation.png)<br>
#### Products
* Products Page
![Products](testing_images/products-html-validation.png)<br>
* Product Details Page
![Product Details](testing_images/product-detail-html-validation.png)<br>
* Update Product Review Page
![Update Product Review](testing_images/update-review-page-html-validation.png)<br>
* Delete Product Review Page
![Delete Product Review](testing_images/delete-review-page-html-validation.png)<br>
#### Favourites
* Favourites Page
![Favourite Page](testing_images/favourites-page-html-validation.png)<br>
#### Bag
* Bag Page
![Bag Page](testing_images/bag-page-html-validation.png)<br>
#### Checkout
* Checkout Summary Page
![Checkout Summary Page](testing_images/checkout-summary-html-validation.png)<br>
* Checkout Page
![Checkout Page](testing_images/checkout-html-validation.png)<br>
* Checkout Success Page
![Checkout Success Page](testing_images/checkout-success-html-validation.png)<br>
#### Profiles
* Profiles Page
* Could not verify this page as it containes private information<br>
Some of the validator tests show a warning. This warning read - The type attribute is unnecessary for JavaScript resources. I have decided to ignore these warnings as they do not harm the site.
### CSS Results:
![CSS](testing_images/css-validation.png)<br>

### JavaScript Results:
![Bag js](testing_images/bag-jshint-validation.png)<br>
![Countryfield js](testing_images/countryfield-js-jshint-validation.png)<br>
![Products js](testing_images/products-js-validation.png)<br>
![Quantity js](testing_images/quantity-input-jshint-validation.png)<br>
![Stripe js](testing_images/stripe-elements-jshint-validation.png)<br>
* Some JSHint validation results show an unused vairable "$" this is because I was using JQuery. These also were taken from the Boutique Ado material and so I did not alter.

### Python Results:
#### Home App
![Home Views](testing_images/home-views.png)<br>
![Test Home Views](testing_images/home-test-views.png)<br>
![Home URLS](testing_images/home-urls.png)<br>
#### Bag App
![Bag URLS](testing_images/bag-urls.png)<br>
![Bag Views](testing_images/menu-views-pep8-validation.png)<br>
![Bag Contexts](testing_images/bag-context.png)<br>
![Test Bag Views](testing_images/bag-views.png)<br>
#### Checkout App
![Checkout Forms](testing_images/checkout-forms.png)<br>
![Checkout Models](testing_images/checkout-models.png)<br>
![Test Checkout Models](testing_images/checkout-modesl-tests.png)<br>
![Checkout Signals](testing_images/checkout-signals.png)<br>
![Checkout Test Forms](testing_images/checkout-test-forms.png)<br>
![Checkout URLS](testing_images/checkout-urls.png)<br>
![Checkout Views](testing_images/checkout-views.png)<br>
![Test Checkout Views](testing_images/checkout-views-test.png)<br>
![Checkout Webhook Handler](testing_images/checkout-webhook-handler.png)<br>
![Checkout Webhooks](testing_images/checkout-webhooks.png)<br>
#### Favourites App
![Favourites Models](testing_images/favourites-models.png)<br>
![Favourites Views](testing_images/favourites-views.png)<br>
![Test Favourites Models](testing_images/favourites-test-models.png)<br>
![Test Favourites Views](testing_images/favourites-test-views.png)<br>
![Favourites URLS](testing_images/favourites-urls.png)<br>
#### Products App
![Products Models](testing_images/products-models.png)<br>
![Products Views](testing_images/products-views.png)<br>
![Products Forms](testing_images/products-forms.png)<br>
![Test Products Models](testing_images/products-test-models.png)<br>
![Test Products Views](testing_images/products-test-views.png)<br>
![Products URLS](testing_images/products-urls.png)<br>
![Products widgegts](testing_images/products-widgets.png)<br>
#### Profiles App
![Profiles Models](testing_images/profiles-models.png)<br>
![Profiles Views](testing_images/profiles-views.png)<br>
![Profiles Forms](testing_images/profiles-forms.png)<br>
![Test Profiles Models](testing_images/profiles-test-models.png)<br>
![Test Profiles Views](testing_images/profiles-test-views.png)<br>
![Profiles URLS](testing_images/profiles-urls.png)<br>

---
---

## Lighthouse Testing <a name="lighthouse-testing"></a>

After getting the bulk of the site in place, I ran it through Chrome Lighthouse.

![Lighthouse score](testing_images/american-ale-house-lighthouse-testing.png)

---
---

### Testing User Stories <a name="testing-from-user-stories"></a>

1. As a new user I can easily register for the website so that I can purchase products quickly and easily.

![Site Registration](testing_images/storey-1.png)

* When the user navigates to the register button in the navigation bar they are directed to the register page. Filling in the form is quick and easy. Once filled out the user is displayed a message to say they have been sent a confirmation email. The new user will need to click the link in that email inorder to complete the signup. Once the email is confirmed the user will then enter their login details and be redirected to the home page.
* This has been tested manually to ensure it works as it should.

2. As a returning user I can log into the site with my login details so that I can access see my profile and previous orders.

![Account Log In](testing_images/login.png)
![Profile & Past orders](testing_images/profile-orders.png)

* If the user is a returning user they will be able Log in easily and view their past orders in the profile tab in the navigation, if they have made any orders.
* This has been tested manually to ensure it works as it should.

3. As a logged in user I can logout of the site easily so that my account is secure

![Account Logout](testing_images/logout.png)

* A logged in user can select to log out of their account so that their information is secure.
* This has been tested manually to ensure it works as it should.

4. As a user I can browse through all the products so that I can choose which one I want to know which one I may want to purchase.

![Browse Products](testing_images/browse-products.png)

* By clicking the All Products button the user can select different ways to view the products. By selecting All Products again the user will be shown all the products on one page with simple information about each one..
* This has been tested manually to ensure it works as it should.

5. As a user I can select a product and view it in detail so that I can see more information that may persuade me to purchase.

![Product Detail](testing_images/storey-5.png)

* The user can select any product to view the product in detail. On this page the user is able to increase/ decrease the quantity and add the product to their basket. They will also be able to see if the product has any rating or reviews and add it to their favourites.
* This has been tested manually to ensure it works as it should.

6. As a user I can filter the products so that so that I can view products by category and price

![Filter products](testing_images/storey-6.png)

* The user is able to filter the products by category, price andrating by selecting the appropriate tab in the sort box in the top right corner of the products window.
* This has been tested manually to ensure it works as it should.


7. As a user I can search the site for products so that I can be directed straight to it easily saving me time scrolling through products

![Search Bar](testing_images/storey-7.png)

* The user is able to enter words in the search bar to quickly search for a product.
* This has been tested manually to ensure it works as it should.

8. As a user I can see reviews and ratings of a product so that I can see other customer opinions on it to help me make up my mind

![Read Product Reviews](testing_images/storey-8-review.png)

* On the product details page a user is able to see any reviews left by other users. This will help customers decisions a little easier to make.
* This has been tested manually to ensure it works as it should.

9. As a logged in user I can leave a product review once purchased so that I can share my experience with other customers

![Leave a Product Review and Rating](testing_images/storey-8-review.png)

* As a logged in user I can leave a review and rating of a product on the product details page. Once reviewed I can update/delete my review if I wanted to.
* This has been tested manually to ensure it works as it should.

10. As a logged in user I can update a product review once purchased so that I can share my experience with other customers.

![Update a Product Review and Rating](testing_images/storey-8-review.png)

* As a logged in user, if I have left a review of a product I can update the review by clicking the update button on the review.
* This has been tested manually to ensure it works as it should.

11. As a logged in user I can delete my product review so that If I feel it is no longer relevant

![Delete a Product Review and Rating](testing_images/storey-8-review.png)

* As a logged in user, if I have left a review of a product I can delete the review by clicking the delete button on the review.
* This has been tested manually to ensure it works as it should.

12. As a Admin I can Create a new product so that I can increase the products I have for sale on the site

![Product Management](testing_images/storey-12.png)

* The admin, once logged in can add a new product by selecting the product management tab in the nav bar.
* This has been tested manually to ensure it works as it should.

13. As a Admin I can Update a products details so that I can adjust the product information

![Edit Product](testing_images/storey-13.png)

* The admin, once logged in can edit a product by selecting the edit button on the product details page. Once this is clicked they are taken to a form to edit the product details.
* This has been tested manually to ensure it works as it should.

14. As a Admin I can Delete a product so that I can change the products I have for sale on the site and if they are no longer available.

![Delete Product](testing_images/storey-13.png)

* The admin is able to delete a product by selecting the delete button on the products or product detail page.
* This has been tested manually to ensure it works as it should.

15. As a customer I can add a product to the shopping basket so that I can purchase it.

![Add to Bag](testing_images/storey-15.png)

* A customer can add a product to their bag either as a logged in user or as a non logged in user by selecting the quantity and clicking the add to bag button.
* This has been tested manually to ensure it works as it should.

16. As a customer I can adjust the quantity of items in my bag so that I can order more or less of an item

![Adjust quantity in bag](testing_images/storey-15.png)

* A customer can add a product to their bag either as a logged in user or as a non logged in user by selecting the quantity by clicking the pluss or minus buttons or entering a number and clicking the add to bag button.
* This has been tested manually to ensure it works as it should.

17. As a customer I can remove an item from my bag so that I am not charged for it

![Remove product from bag](testing_images/storey-17.png)

* A customer can rermove a product to their bag either as a logged in user or as a non logged in user by selecting the remove button for the product on the bag page.
* This has been tested manually to ensure it works as it should.

18. As a customer I can see the total of my basket so that I know how much I have spent

![Bag Total](testing_images/storey-18.png)

* As a customer I can see the total cost of items in my basket from any page on the site. This is visible in the nav bar at the top right of the screen.
* This has been tested manually to ensure it works as it should.

19. As a customer I can checkout securely so that I am notified the purchase has been successful

![Checkout Securely](testing_images/storey-19.png)

* As a customer I can checkout securely and am notified with a success message and confirmation email that the purchase has been successful
* This has been tested manually to ensure it works as it should.

20. As a logged in user I can add or remove a product to my favourites so that it is quick and easy to purchase the item again

![Add or Remove product to to favourites](testing_images/storey-20.png)

* As a logged in user I can add a product to my favourites and remove them by clicking the heart on the product details page. If the user is not logged in they will be asked to log in first. You can also remove the product from the favourites page.
* This has been tested manually to ensure it works as it should.

21. As a logged in user I can view my profile so that I can add default address and view orders

![Add or update personal details in Profiles](testing_images/storey-22.png)

* As a logged in user I can add or update default delivery information that will make the checkout process faster.
* This has been tested manually to ensure it works as it should.

22. As a user I can receive discount codes so that I can get free delivery or money off my order

![Receive discount codes](testing_images/storey-22.png)

* Once signed up for the site the user will receive a code FIRST_TIMER that can be added ar checkout for £5 off their order. Codes will also be able to be sent out in marketing emails.
* This has been tested manually to ensure it works as it should.

23. As a user I can see the same navigation menu on each page so that it is easy to understand and use

![Site wide navigation](testing_images/storey-23.png)

* The navigation for the site is the same on every page so that it is easy for the user to navigate around
* This has been tested manually to ensure it works as it should.

24. As a user I can signup to the newsletter so that I receive news and discounts from the site

![Newsletter sign up](testing_images/storey-24.png)

* By entering an email address into the Hop on Board section in the footer a user can sign up to receive the newsletter and get all the news, special offers and discount codes.
* This has been tested manually to ensure it works as it should.

25. As a user I can see the sites FAQ's so that I may get some answers to my questions easily

![Frequently asked questions Footer](testing_images/storey-25.png)
![Frequently asked questions Page](testing_images/faq-page.png)

* In the footer on every page there is a link to the frequently asked questions page where the user can get answeres to common questions. If there is no answer for their question they are provided with a link to contact us.
* This has been tested manually to ensure it works as it should.

26. As a user I can contact the American Ale House via phone or email so that I can make contact on any issues I might have

![Contact us](testing_images/storey-26.png)

* In the footer on every page there is a link to the contact us page. On the page the user will find an address and phone number and email address as well as a geet in touch form that they can fill out to send a direct message to the site owners.
* This has been tested manually to ensure it works as it should.

27. As a user I can view the sites policy so that I understand how my data will be used

![Site Policy](testing_images/storey-27.png)

* In the footer on every page there is a link to the Site policy. This opens in a separate tab in their browser.
* This has been tested manually to ensure it works as it should.

28. As a user I can follow the business on social media so that I can keep up to date with latest news and offers

![Site socials](testing_images/storey-28.png)
![Site socials Facebook](testing_images/facebook.png)

* The user is able to view the sites social networks by clicking on the icons at the bottom of the newsletter signup in the footer, this will help keep them up to date with any offers or news the American Ale House has. These links will open in a new tab. The Facebookpage has been created for the American Ale House and links to the page.
* This has been tested manually to ensure it works as it should.

29. As a user I can understand the site meaning when I land on the home page so that I know I am on a site I want to purchase from

![Site Meaning](testing_images/storey-29.png)

* It is obvious what the site is about as soon as a new user lands on the site. There is a background image that is linked to the sites purpose of Beer and the site name is very descriptive. The main tesx on the home page also clearly states what the site is about.
* This has been tested manually to ensure it works as it should.

30. As a User/admin I can be notified of my actions so that I know if my actions have been successful or not

![User notifications](testing_images/storey-30.png)

* Users are notified with messages so they know if they have been successful or not, For example if the user is adding a product to their bag , as in the picture above, they will get a success message.
* This has been tested manually to ensure it works as it should.

31. As a user I can view the footer on different devices so that I can still see all the content

![Responsive Footer](testing_images/storey-31.png)

* The footer is responsive to the size of the devise it is being viewed on. Customer services, contact us and opening hours are side by side  and stack on smaller devices.
* This has been tested manually to ensure it works as it should.

---
---
## Automated Testing <a name="testing-automated-tests"></a>
![Automated Tests](testing_images/automated-tests.png)

Automated Unit Testing was carried out with Djangos testing tools and written to cover as much of the site as possible. Below is an overview of each app and what was tested:

### Home App

+ Views
   + test that the home view works
   + test that the contact view works
   + test that the email sends in contact view
   + test that faq view works

### Bag App

+ Views
   + Test that all users can view the bag page
   + Test that all users can add a product to the bag
   + Test that all users can update a product on the bag
   + Test that all users can remove a product from the bag
  

### Checkout App

+ Models
   + Test the order number string
   + Test the Coupon code

+ Views
   + Test that the user gets an error message if they try to checkout with an empty bag

+ Forms
   + Test the form does not submit without full_name field
   + Test the form does not submit without email field
   + Test the form does not submit without phone_number
   + Test the form does not submit without country field
   + Test the form does not submit without town_or_city field
   + Test the form does not submit without street_address field
   
### Favourites App

+ Models
   + Test tests the favourites str method

+ Views
   + Tests the user can view their favourites page
   + Test for adding a product to favourites
   + Test remove a product from the users favourites

### Products App

+ Models
   + Test model returns Category name and friendly name as a string
   + Test model returns Product name as a string

+ Views
   + Check users are set up
   + Test URL response success
   + Test users can view all products
   + Test users can view the Product details page
   + Test superuser can access the add a product page
   + Test non superuser can't access the add a product page
   + Test a superuser can delete a product
   + Test a non superuser can't delete a product
   + Test a logged in user can add a review to a product
   + Test a logged in user can update a review on a product
   + Test a logged in user can delete a review on a product

### Profiles App

+ Models
   + tests the users profile username returned as a string

+ Views
   + Test logged in user can access their profile page
   + Test using correct template in profile page
   + Test user can see their order history
   + Test that default delivery info updates

---
---

## Manually Testing Functionality <a name="manually-testing-functionality"></a>
### **Navigation**

|Element               |Action|Expected Result               |Pass/Fail|
|:-------------         |:----|:----------------------------------|:---|
| **NavBar**            |                                         |    |
|Site Name              |Click|Redirect to home                   |Pass|
|My profile Dropdown    |Click|Open profile dropdown              |Pass|
|Register Link          |Click|Redirect to register page          |Pass|
|                       |     |(Not visible if user logged in)    |Pass|
|Log In Link            |Click|Redirect to log in page            |Pass|
|                       |     |(Not visible if user logged in)    |Pass|
|Product Management Link|Click|Redirect to add_product page       |Pass|
|                       |     |(Only visble if admin logged in)   |Pass|
|My Profile Link        |Click|Redirect to user profile page      |Pass|
|                       |     |(Only visble if user in session)   |Pass|
|My Favourites Link     |Click|Redirect to user favourites page   |Pass|
|                       |     |(Only visble if user logged in)    |Pass|
|Logout Link            |Click|Redirect to logout confirm  page   |Pass|
|                       |     |(Only visble if user logged in)    |Pass|
|Bag Link               |Click|Redirect to bag page               |Pass|
|Search Bar             |     |Enter key words to search products |Pass|
| **Mobile Nav**        |     |                                   |    |
|Hamburger Icon         |Click|Open Dropdown                      |Pass|
|- Home                 |Click|Redirect to home                   |Pass|
|- All Products Dropdown|Click|Displays links to All products     |Pass|
|                       |     |and filtered options and redirects |Pass|
|- All American Beers   |Click|Displays links to the different    |Pass|
|Dropdown               |     |styles of beers and redirects      |Pass|
|                       |     |                                   |Pass|
|Search Link            |Click|Enter key words to search products |Pass|
|My Account Dropdown    |Click|Open account dropdown              |Pass|
|Register Link          |Click|Redirect to register page          |Pass|
|                       |     |(Not visible if user logged in)    |Pass|
|Log In Link            |Click|Redirect to log in page            |Pass|
|                       |     |(Not visible if user logged in)    |Pass|
|Product Management Link|Click|Redirect to add_product page       |Pass|
|                       |     |(Only visble if admin logged in)   |Pass|
|My Favourites Link     |Click|Redirect to user favourites page   |Pass|
|                       |     |(Only visble if user logged in)    |Pass|
|My Profile Link        |Click|Redirect to user profile page      |Pass|
|                       |     |(Only visble if user logged in)    |Pass|
|Logout Link            |Click|Redirect to logout confirm  page   |Pass|
|                       |     |(Only visble if user logged in)    |Pass|
|Bag Link               |Click|Redirect to bag page               |Pass|
| **MainNav**           |     |                                   |    |
|All Products           |Click|Displays links to All products     |Pass|
|Dropdown               |     |and filtered options and redirects |Pass|
|American Beers         |Click|Displays links to the different    |Pass|
|Dropdown               |     |styles of beers and redirects      |Pass|
| **Footer**            |     |                                   |    |
|*Customer Services*    |     |                                   |    |
|FAQ's Link             |Click|Redirect to FAQ's page.            |Pass|
|Site Policy Link       |Click|Opens new tab to display policy    |Pass|
|Log in Link            |Click|Redirect to login page             |Pass|
|Register Link          |Click|Redirect to signup page            |Pass|
|*Contact us*           |     |                                   |    |
|Contact Us Link        |Click|Redirect to contact page           |Pass|
|*Mailchimp subscribe*  |     |                                   |    |
|Subscribe to newsletter|Click|Enter email to subscribe to site   |Pass|
|*Socials*              |     |                                   |    |
|Facebook Link          |Click|Open on external page (live page)  |Pass|
|Instagram Link         |Click|Open on external page              |Pass|
|LinkedIn               |Click|Open on external page              |Pass|
|Twitter Link           |Click|Open on external page              |Pass|

---
### **Home Page**
| Element               | Action| Expected Result           | Pass/Fail|
|:-------------         |:-----|:-----                            |:---|
|Shop Now button        |Click|Redirects to products page         |Pass|
|Selection carosel      |Click|Redirects to product details page  |Pass|
|Selection carosel      |Click|manually rotate through products   |Pass|
|                       |Seipe|using arrow buttons or swiping     |Pass|
|                       |     |on phone                           |    |

---

### **Products Page**

| Element               | Action | Expected Result          | Pass/Fail|
|:-------------         |:-------|:-----                          |:---|
|'Sort By' Dropdown     |Click|Open 'sort by' options             |Pass|
|'Sort By' Options (x8) |Click|Re-order products                  |Pass|
|Product Card           |Click|Redirect to product detail page    |Pass|

---

### **Product Detail Page**

| Element               | Action |Expected Result           | Pass/Fail|
|:-------------         |:-------|:-----                          |:---|
|Qty control buttons    |Click|Increase/decrease quantity         |Pass|
|Keep Shopping button   |Click|Redirect to products page          |    |
|Add to bag button      |Click|Add item to bag                    |Pass|
|                       |     |Toast Success appears              |Pass|
|                       |     |Item visible in toast success      |Pass|
|Rate Product           |Click|Hover over the stars to rate       |Pass|
|                       |     |and click to confirm               |    |
|                       |     |(if logged in)                     |    |
|Review Product         |Enter|Leave a review of the product      |Pass|
|                       |     |(if logged in)                     |    |
|                       |     |Redirect to login page if not      |Pass|
|Read Review            |     |If a review has been left all users|Pass|
|                       |     |can read them                      |    |
|Update Review          |Click|If a review is yours update button |Pass|
|                       |     |visible and redirects to form      |    |
|Delete Review          |Click|If a review is yours delete button |Pass|
|                       |     |visible and redirects to form      |    |
|**admin only:**        |     |                                   |    |
|Edit product button    |Click|Redirect to edit product page      |Pass|
|Delete product button  |Click|Open delete confirmation modal     |Pass|

---

### **Add Product Page**

| Element               |Action| Expected Result             |Pass/Fail|
|:-------------         |:----|:-----                             |:---|
|Form Dropdown          |Click|Show dropdown category options     |Pass|
|Name field             |Enter|Field must be filled in or warning |Pass|
|Description field      |Enter|Field must be filled in or warning |Pass|
|Price field            |Enter|Field must be filled in or warning |Pass|
|Rating field           |Enter|Field must be filled in or warning |Pass|
|Abv field              |Enter|Field not needed to be filled      |Pass|
|Image select button    |Click|Open device storage                |Pass|
|                       |     |Chosen image name displayed        |Pass|
|                       |     |If no image set, placeholder set   |Pass|
|Cancel button          |Click|Redirect to products page          |Pass|
|Add Product button     |Click|Form submit                        |Pass|
|                       |     |Redirect to product detail page    |Pass|
|                       |     |Product uploaded toast appears     |Pass|
|Add Product button     |Click|Form doesn't submit                |Pass|
|                       |     |Error messages on invalid fields   |Pass|

---