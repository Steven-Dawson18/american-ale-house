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
