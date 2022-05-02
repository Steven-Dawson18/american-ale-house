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
