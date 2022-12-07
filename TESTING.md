# Manual Testing

[Back to README](README.md)

The purpose of this document is to summarise the process, results, bugs and fixes as part of manually testing The Coffee Collective website.



## Epics & functionality
* Epics & functionality - validating the requirements have been delivered for the MVP release.



## Page Validation
* Page validation - ensuring that all features are working, including all links perform as designed.


<br>


## Responsiveness

To test the websites layout and content remains well structured and accessible across differing screen sizes, I used Chrome's Developer Tools to virtualise how the website and all it's pages look and feel. In consideration that I opted to use Bootstrap which provides standard media queries for screen sizes from XS through to XL, I selected the following screens to test on; iPhone 4, iPhone SE, Samsung Galaxy S8, iPad, iPad Pro, Laptop at 1366x768, Monitor at 1920x1080 and iMac 5K.

In summary of the results, very few issues were identified; 
* Small changes to padding and margin sizes for the FAQ's section to ensure I was maximising the use of mobile screens.
* The homepage failed on mobile devices as the container for the nav-menu toggle button was too large and covering other navbar links. This was a simple resizing fix for the container.
The homepage failed on tablets as elements from both the mobile and desktop navbar were showing at the same time. The fix involved readdressing the out of the box class names from Bootstrap to ensure only the right elements showed on the right screen widths.

<br>

File path                                                                                    | Mobile | Tablet | Desktop
-------------------------------------------------------------------------------------------- | ------ | ------ | -------
bag/templates/bag/bag.html                                                                   | PASS   | PASS   | PASS   
checkout/templates/checkout/checkout\_success.html                                           | PASS   | PASS   | PASS   
checkout/templates/checkout/checkout.html                                                    | PASS   | PASS   | PASS   
company/templates/accessibility\_statement.html                                              | PASS   | PASS   | PASS   
company/templates/contact.html                                                               | PASS   | PASS   | PASS   
company/templates/copyright\_statement.html                                                  | PASS   | PASS   | PASS   
company/templates/faqs.html                                                                  | PASS   | PASS   | PASS   
company/templates/health\_benefits.html                                                      | PASS   | PASS   | PASS   
company/templates/our\_story.html                                                            | PASS   | PASS   | PASS   
company/templates/sustainability.html                                                        | PASS   | PASS   | PASS   
company/templates/terms\_and\_conditions.html                                                | PASS   | PASS   | PASS   
[https://the-coffee-collective.herokuapp.com/](https://the-coffee-collective.herokuapp.com/) | FAIL   | FAIL   | PASS   
products/templates/products/add\_product.html                                                | PASS   | PASS   | PASS   
products/templates/products/delete\_product\_page.html                                       | PASS   | PASS   | PASS   
products/templates/products/edit\_product.html                                               | PASS   | PASS   | PASS   
products/templates/products/product\_detail.html                                             | PASS   | PASS   | PASS   
products/templates/products/products.html                                                    | PASS   | PASS   | PASS   
profiles/templates/profiles/profile.html                                                     | PASS   | PASS   | PASS   
templates/allauth/account/confirm-email.html                                                 | PASS   | PASS   | PASS   
templates/allauth/account/login.html                                                         | PASS   | PASS   | PASS   
templates/allauth/account/logout.html                                                        | PASS   | PASS   | PASS   
templates/allauth/account/signup.html                                                        | PASS   | PASS   | PASS   
templates/errors/403.html                                                                    | PASS   | PASS   | PASS   
templates/errors/404.html                                                                    | PASS   | PASS   | PASS   
templates/errors/405.html                                                                    | PASS   | PASS   | PASS   
templates/errors/500.html                                                                    | PASS   | PASS   | PASS   
templates/includes/toasts/toast\_error.html                                                  | PASS   | PASS   | PASS   
templates/includes/toasts/toast\_info.html                                                   | PASS   | PASS   | PASS   
templates/includes/toasts/toast\_success.html                                                | PASS   | PASS   | PASS   
templates/includes/toasts/toast\_warning.html                                                | PASS   | PASS   | PASS   
templates/includes/footer.html                                                               | PASS   | PASS   | PASS   
templates/includes/main-nav.html                                                             | n/a    | n/a    | PASS   
templates/includes/mobile-top\_head.html                                                     | PASS   | PASS   | n/a       


<br> 


## Accessibility 

Key to any successful eCommerce website is ensuring its accessibility. Whilst in the design phase I consulted colour contrasting checkers to test for accessibility, it was pleasing to see the end results of this test. As well as using Chrome Developer Tools to test each html page, I also used the WAVE online assessment tool as I feel this provides a deeper level of insight and clearer in highlighting where improvements are required.

In summary of the results;
* Given the nature of the Django build, I tested the live web page as opposed to the code input validation method. This was successful for nearly all pages, however the tool would not test the checkout and checkout success pages. For these I relied on the Developer Tool assessment to provide insight.
* The forms for managing products came under scrutiny as they are not supported by screen readers as standard and hence received a sub 90% score. For a future release the forms will be rebuilt to ensure compliance. 
* Within the homepage I had incorrectly used 'Arial-labellby' to describe an element. This was resolved by amending to use 'Arial-label' to support visual impaired visitors.

<br>

File path                                                                                    | WAVE Tool | Lighthouse Mobile | Lighthouse Desktop
-------------------------------------------------------------------------------------------- | --------- | ---------- | ----------
bag/templates/bag/bag.html                                                                   | PASS      | 89         | 90        
checkout/templates/checkout/checkout\_success.html                                           | NP        | 100        | 100       
checkout/templates/checkout/checkout.html                                                    | NP        | 96         | 94        
company/templates/accessibility\_statement.html                                              | PASS      | 100        | 100       
company/templates/contact.html                                                               | PASS      | 100        | 100       
company/templates/copyright\_statement.html                                                  | PASS      | 100        | 100       
company/templates/faqs.html                                                                  | PASS      | 100        | 100       
company/templates/health\_benefits.html                                                      | PASS      | 100        | 100       
company/templates/our\_story.html                                                            | PASS      | 100        | 100       
company/templates/sustainability.html                                                        | PASS      | 100        | 100       
company/templates/terms\_and\_conditions.html                                                | PASS      | 100        | 100       
[https://the-coffee-collective.herokuapp.com/](https://the-coffee-collective.herokuapp.com/) | PASS      | 98         | 98                  
products/templates/products/add\_product.html                                                | PASS      | 91         | 92        
products/templates/products/delete\_product\_page.html                                       | PASS      | 98         | 100       
products/templates/products/edit\_product.html                                               | PASS      | 81         | 84        
products/templates/products/product\_detail.html                                             | PASS      | 89         | 89        
products/templates/products/products.html                                                    | PASS      | 100        | 100       
profiles/templates/profiles/profile.html                                                     | PASS      | 100        | 100       
templates/allauth/account/confirm-email.html                                                 | PASS      | 100        | 100       
templates/allauth/account/login.html                                                         | PASS      | 100        | 100       
templates/allauth/account/logout.html                                                        | PASS      | 100        | 100       
templates/allauth/account/signup.html                                                        | PASS      | 100        | 100       
templates/errors/403.html                                                                    | PASS      | NP         | NP        
templates/errors/404.html                                                                    | PASS      | NP         | NP        
templates/errors/405.html                                                                    | PASS      | NP         | NP        
templates/errors/500.html                                                                    | PASS      | NP         | NP        


<br>

 
## Performance
* Performance - using Chrome's developer tool 'Lighthouse Testing' pages are tested for performance, best-practice, SEO and accessibility.
Tested footer, mobile nav and main nav as part of index homepage testing
tested using incognito for lighthouse testing


## Browser
* Browser - pages are tested for layout, features and general performance across Chrome, Firefox, Edge, Internet Explorer 11 and Opera.



## Device
* Device - manual testing will be performed on an iOS and Android mobile, Tablet, Laptop and Desktop to ensure all users have a positive experience no matter which device or browser they prefer to use. 



## Code
* Code validation - ensuring the code base is validated using industry standard tools for HTML, CSS, JavaScript and Python code.
Pycodestyle



## Bugs