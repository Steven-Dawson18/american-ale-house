# American Ale House

## User Experience

### User Stories

* EPIC: American Ale House Authentication
1. As a new user I can easily register for the website so that I can purchase products quickly and easily
2. As a returning user I can log into the site with my login details so that I can access see my profile and previous orders
3. As a logged in user I can logout of the site easily so that my account is secure

* EPIC: American Ale House Product
4. As a user I can browse through all the products so that I can choose which one I want to know which one I may want to purchase
5. As a user I can select a product and view it in detail so that I can see more information that may persuade me to purchase
6. As a user I can filter the products so that so that I can view products by category and price
7. As a user I can search the site for products so that I can be directed straight to it easily saving me time scrolling through products
8. As a user I can see reviews and ratings of a product so that I can see other customer opinions on it to help me make up my mind
9. As a logged in user I can leave a product review once purchased so that I can share my experience with other customers
10. As a logged in user I can update a product review once purchased so that I can share my experience with other customers
11. As a logged in user I can delete my product review so that If I feel it is no longer relevant
12. As a Admin I can Create a new product so that I can increase the products I have for sale on the site
13. As a Admin I can Update a products details so that I can adjust the product information
14. As a Admin I can Delete a product so that I can change the products I have for sale on the site and if they are no longer available

* EPIC: American Ale House Product Purchasing
15. As a customer I can add a product to the shopping basket so that I can purchase it
16. As a customer I can adjust the quantity of items in my bag so that I can order more or less of an item
17. As a customer I can remove an item from my bag so that I am not charged for it
18. As a customer I can see the total of my basket so that I know how much I have spent
19. As a customer I can checkout securely so that I am notified the purchase has been successful


* EPIC: American Ale House User Experience
20. As a logged in user I can add or remove a product to my favourites so that it is quick and easy to purchase the item again
21. As a logged in user I can view my profile so that I can add default address and view orders
22. As a user I can receive discount codes so that I can get free delivery or money off my order
23. As a user I can see the same navigation menu on each page so that it is easy to understand and use
24. As a user I can signup to the newsletter so that I receive news and discounts from the site
25. As a user I can see the sites FAQ's so that rI may get some answers to my questions easily
26. As a user I can contact the American Ale House via phone or email so that I can make contact on any issues I might have
27. As a user I can view the sites policy so that I understand how my data will be used
28. As a user I can follow the business on social media so that I can keep up to date with latest news and offers
30. As a user I can understand the site meaning when I land on the home page so that I know I am on a site I want to purchase from


## Strategy

### Aim
The American Ale House is an ecommerce website allowing users to purchase American brewed beers developed for my Project 5 as part of the Code Institute - Diploma in Software Development (Full stack) Diploma.

### Description
The American Ale House websiteprovides the user the ability to purchaseAmerican brewed beers in the UK. Firstly upone landing on the site you are greeted with an elegant image which clearly protrays the purpose of the site. As a non logged in user you can browse all the products and add the ones you want into your bag ready for checkout. You can checkout by entering all your details and entering a valid credit card. Once your order is complete you will see a confirmation page and a confirmation email will be sent to your email. As a logged in user you will be able to checkout faster as your default address will be in your profile. You will also be able to view your order history and leave reviews on products that you have purchased. The logged in user will also be able to add products to their favourites for a quicker purchase next time. If you sign up to the newsletter you will recieve a Beer token which you will be able to redeem at checkout for a discount on your shop.

## Scope

 * A simple, straightforward, intuitive UX experience;
 * An explicit content; 
 * An easy navigation for the user through all the features;
 * A site that is visually appealing on most devices.


### Agile methodology

* All functionality and development of this project will be managed through GitHub issues, milestones and projects.

<summary>All sprints are described here.</summary>

* Sprint 1 - 15/03/2022 - 16/03/2022 (Finished at 15/03/2022)

  + Initial setup
    - Install django
    - Install Allauth
    - Add Allauth templates to project templates
    - Create base.html
    - Create Home app
    - Create index.html, view and style
    - Create responsice navigation
    - Add to README.md file
  
* Sprint 2 - 16/03/2022 - 18/03/2022 (Finished on 17/03/2022)

  + Add Product app
    - Set up all products view
    - Set up product dteail view
  + Add bag app
    - Set up add to bag
    - Set up adjust bag
    - Set up remove from bag
  + Add Responsive footer
    - Add mailchimp form
    - Create footer layout

* Sprint 3 - 21/03/2022 - 23/03/2022 (Finished on 23/03/2022)

  + Add Checkout app
    - Set up Models
    - Set up admin
    - Set up Signals
    - Set up templates
  + Add Stripe to project
    - Set up webhooks
  + Add Product form
    - Add Create product form
    - Set up create product view
    - Set up Update Product view
    - Set up Delete Product view
  + Add FAQ's
   - Create html
   - Add questions and answers
   - Add link to footer
  + Add Contact Us
   - Create HTML
   - Set up Email functionality
   - Add link to footer

  * Sprint 4 - 24/03/2022 - 27/03/2022 (Unfinished 27/03/2022)
    + Add Profile app
    - Set up Models
    - Set up admin
    - Set up views
    - Set up templates
    + Customise allauth templates
    - Set up templates
    - Add CSS
    + Add Toasts
    - Set up notifications with toasts

  +During this iteration I ran out of time to complete the Favourites app and therefore it has been placed back in the backlog and will be prioritised for the next iteration. Probably should have factored in Mothers Day!

* Sprint 5 - 28/03/2022 - 30/03/2022 (Finished on 30/03/2022)
    + Add Favourites app
    - Set up Models
    - Set up admin
    - Set up views
    - Set up templates
    + Add Product Reviews
    - Set up Models
    - Set up admin
    - Set up views
    - Set up templates

### Structure

* A clear and straightforward layout is in place to ensure users can navigate intuitively and have a leisurely experience.
* Navbar is fixed on top to facilitate users easily navigating through pages. Small navigation is the same on all pages to ensure easy navigation.
* Footer is fixed on the bottom with links to social media and newsletter subscription.

### Skeleton

Wireframes created with Balsamiq. The project was developed from initial wireframes

Click to see wireframes:

[HomePage](media/) TBD <br>

## Business Model

+ A traditional B2C (Business to Customer) application has been chosen, with a straightforward and user-friendly responsive interface.

+ This online store offers American Ale products to the final customer. 

## Marketing

+ This site has a Facebook Business Page with a link on the page footer. It can be viewed here:


+ Users can subscribe to our newsletter to receive all offers in their email box. Subscription links are available on the footer on all pages. 

+ Upon registering, the user is redirected to a new page confirming their subscription. The site owner can now see the new subscriber on their audience dashboard, and new campaigns will be sent to them too.

### Surface

* Colours

The Colour scheme was generated using the eyedropper plugin to get one colour from the logo image and [colours](https://coolors.co/) to create the colour palette.

[View Pallet Here](https://coolors.co/palette/9d3904-af0707-684c34-221e1f-c9b088-e6bb1a-ffffff)

* Font Selection
 
Two complimentary fonts were chosen with [Google Fonts](https://fonts.google.com/) to be used across the website.

The chosen fonts were Lobster for headings and navbar and Open Sans for lists, buttons and paragraphs.
