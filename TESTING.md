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
* The inclusion of the third party element in MailChimp raised an error as the brand logo did not have an alt attribute.

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

Performing cross browser testing is key to ensuring a positive user experience no matter which browser users prefer to use. To perform a thorough test, I used Firefox, Chrome and Edge on my local machine, which uses Windows 10 as the operating system. To gain further coverage I used Lambda Testing, a browser best tool that virtualises browsers, devices and screen sizes. Here I could test the site on Safari and Opera. IE11 or previous versions were not tested at this time as Microsoft has ceased supporting this browser as they look to embed Edge.

Reassuringly the tests proved the website loads on all 5 browser types. All elements such as buttons, forms, menus and images loaded and were functional were required. Despite getting poor lighthouse performance results for the website loading on mobile devices, I didn't experience this in reality from either browser or device testing.

There was one isolated issue whereby the inherit styles for the Mailchimp element didn't load completely correct on my local machine when using Firefox. This also included the 'Subscribe' button not being functional. I tried to replicate this virtually using Firefox within the Lambda tool, however the feature loaded correctly and was functional.

<br>

| File path                                                                                    | Chrome (v107) | Firefox (v107 win 10) | Edge (v104 Win 10) | Safari (v15 macOS Monterey) | Opera (v89 macOS Monterey) |
| -------------------------------------------------------------------------------------------- | ------------- | --------------------- | ------------------ | --------------------------- | -------------------------- |
| bag/templates/bag/bag.html                                                                   | PASS          | PASS                  | PASS               | PASS                        | PASS                       |
| checkout/templates/checkout/checkout\_success.html                                           | PASS          | PASS                  | PASS               | PASS                        | PASS                       |
| checkout/templates/checkout/checkout.html                                                    | PASS          | PASS                  | PASS               | PASS                        | PASS                       |
| company/templates/accessibility\_statement.html                                              | PASS          | PASS                  | PASS               | PASS                        | PASS                       |
| company/templates/contact.html                                                               | PASS          | PASS                  | PASS               | PASS                        | PASS                       |
| company/templates/copyright\_statement.html                                                  | PASS          | PASS                  | PASS               | PASS                        | PASS                       |
| company/templates/faqs.html                                                                  | PASS          | PASS                  | PASS               | PASS                        | PASS                       |
| company/templates/health\_benefits.html                                                      | PASS          | PASS                  | PASS               | PASS                        | PASS                       |
| company/templates/our\_story.html                                                            | PASS          | PASS                  | PASS               | PASS                        | PASS                       |
| company/templates/sustainability.html                                                        | PASS          | PASS                  | PASS               | PASS                        | PASS                       |
| company/templates/terms\_and\_conditions.html                                                | PASS          | PASS                  | PASS               | PASS                        | PASS                       |
| [https://the-coffee-collective.herokuapp.com/](https://the-coffee-collective.herokuapp.com/) | PASS          | FAIL                  | PASS               | PASS                        | PASS                       |
| products/templates/products/add\_product.html                                                | PASS          | PASS                  | PASS               | PASS                        | PASS                       |
| products/templates/products/delete\_product\_page.html                                       | PASS          | PASS                  | PASS               | PASS                        | PASS                       |
| products/templates/products/edit\_product.html                                               | PASS          | PASS                  | PASS               | PASS                        | PASS                       |
| products/templates/products/product\_detail.html                                             | PASS          | PASS                  | PASS               | PASS                        | PASS                       |
| products/templates/products/products.html                                                    | PASS          | PASS                  | PASS               | PASS                        | PASS                       |
| profiles/templates/profiles/profile.html                                                     | PASS          | PASS                  | PASS               | PASS                        | PASS                       |
| templates/allauth/account/confirm-email.html                                                 | PASS          | PASS                  | PASS               | PASS                        | PASS                       |
| templates/allauth/account/login.html                                                         | PASS          | PASS                  | PASS               | PASS                        | PASS                       |
| templates/allauth/account/logout.html                                                        | PASS          | PASS                  | PASS               | PASS                        | PASS                       |
| templates/allauth/account/signup.html                                                        | PASS          | PASS                  | PASS               | PASS                        | PASS                       |
| templates/errors/403.html                                                                    | PASS          | PASS                  | PASS               | PASS                        | PASS                       |
| templates/errors/404.html                                                                    | PASS          | PASS                  | PASS               | PASS                        | PASS                       |
| templates/errors/405.html                                                                    | PASS          | PASS                  | PASS               | PASS                        | PASS                       |
| templates/errors/500.html                                                                    | PASS          | PASS                  | PASS               | PASS                        | PASS                       |
| templates/includes/toasts/toast\_error.html                                                  | PASS          | PASS                  | PASS               | PASS                        | PASS                       |
| templates/includes/toasts/toast\_info.html                                                   | PASS          | PASS                  | PASS               | PASS                        | PASS                       |
| templates/includes/toasts/toast\_success.html                                                | PASS          | PASS                  | PASS               | PASS                        | PASS                       |
| templates/includes/toasts/toast\_warning.html                                                | PASS          | PASS                  | PASS               | PASS                        | PASS                       |

<br>


## Device

Similar to the aims of browser testing, I wanted to tests users experience of the website across conventional devices. For this I used an iPhone SE, iPad, Laptop, 27" Monitor and lastly a virtual environment for a mobile phone using an Android operating system.

The only major issue here was identified when opening the vertical accordion style FAQ's as the boxes were too narrow on mobile devices. This resulted in very few words per line and therefore too much scrolling for the user. The fix was to widen the boxes that contain the questions and answers, making better use of the screen width and in turn increasing the fluidity that users can read the content.

<br>

| File path                                                                                    | Mobile (iOS) | Mobile (Android) | Tablet | Desktop |
| -------------------------------------------------------------------------------------------- | ------------ | ---------------- | ------ | ------- |
| bag/templates/bag/bag.html                                                                   | PASS         | PASS             | PASS   | PASS    |
| checkout/templates/checkout/checkout\_success.html                                           | PASS         | PASS             | PASS   | PASS    |
| checkout/templates/checkout/checkout.html                                                    | PASS         | PASS             | PASS   | PASS    |
| company/templates/accessibility\_statement.html                                              | PASS         | PASS             | PASS   | PASS    |
| company/templates/contact.html                                                               | PASS         | PASS             | PASS   | PASS    |
| company/templates/copyright\_statement.html                                                  | PASS         | PASS             | PASS   | PASS    |
| company/templates/faqs.html                                                                  | FAIL         | PASS             | PASS   | PASS    |
| company/templates/health\_benefits.html                                                      | PASS         | PASS             | PASS   | PASS    |
| company/templates/our\_story.html                                                            | PASS         | PASS             | PASS   | PASS    |
| company/templates/sustainability.html                                                        | PASS         | PASS             | PASS   | PASS    |
| company/templates/terms\_and\_conditions.html                                                | PASS         | PASS             | PASS   | PASS    |
| [https://the-coffee-collective.herokuapp.com/](https://the-coffee-collective.herokuapp.com/) | PASS         | PASS             | PASS   | PASS    |
| products/templates/products/add\_product.html                                                | PASS         | PASS             | PASS   | PASS    |
| products/templates/products/delete\_product\_page.html                                       | PASS         | PASS             | PASS   | PASS    |
| products/templates/products/edit\_product.html                                               | PASS         | PASS             | PASS   | PASS    |
| products/templates/products/product\_detail.html                                             | PASS         | PASS             | PASS   | PASS    |
| products/templates/products/products.html                                                    | PASS         | PASS             | PASS   | PASS    |
| profiles/templates/profiles/profile.html                                                     | PASS         | PASS             | PASS   | PASS    |
| templates/allauth/account/confirm-email.html                                                 | PASS         | PASS             | PASS   | PASS    |
| templates/allauth/account/login.html                                                         | PASS         | PASS             | PASS   | PASS    |
| templates/allauth/account/logout.html                                                        | PASS         | PASS             | PASS   | PASS    |
| templates/allauth/account/signup.html                                                        | PASS         | PASS             | PASS   | PASS    |
| templates/errors/403.html                                                                    | PASS         | PASS             | PASS   | PASS    |
| templates/errors/404.html                                                                    | PASS         | PASS             | PASS   | PASS    |
| templates/errors/405.html                                                                    | PASS         | PASS             | PASS   | PASS    |
| templates/errors/500.html                                                                    | PASS         | PASS             | PASS   | PASS    |
| templates/includes/toasts/toast\_error.html                                                  | PASS         | PASS             | PASS   | PASS    |
| templates/includes/toasts/toast\_info.html                                                   | PASS         | PASS             | PASS   | PASS    |
| templates/includes/toasts/toast\_success.html                                                | PASS         | PASS             | PASS   | PASS    |
| templates/includes/toasts/toast\_warning.html                                                | PASS         | PASS             | PASS   | PASS    |


<br>


## Code

Writing well formed, quality code is essential for the future development of this, or any website. To support this aim I have used industry standard tools [list below] to validate every line of code using the input method. As well as using this tools, using GitPod as IDE allowed me to utilise the inbuilt code checkers such as Pycodestyle for Python. 

* W3 Validator for HTML
* W3 Jigsaw for CSS
* JS Hint for JavaScript
* CI Python Linter for Python

To gain passes across the code base I had to address minor issues such as;

* General formatting and resolving E501 line length errors
* Removing unnecessary trailing slashes from elements e.g. <br/>
* Removing unnecessary 'type' attribute from script tags
* Remove an anchor tag from within a HTML button and change the anchor to look like a button.
* Adding new lines to the end of Python files to resolve W292 errors.
* More details of these minor infringements can be found within the (TCC Testing document in the repo)[].

The following issues were identified and not resolved so carry an EXC = pass with an acceptable exception.

* env.py - E501 as line breached 79 characters, however when I tried to split the Database URL over two lines it not longer functioned. As a result I have chosen to allow this exception for the MVP.
* profiles.js and stripe_elements.js - ES6 warning to use 'esverions:6'. I research a fix and added JSHint ES6 to the settings.JSON file, however this did not clear the warning. As this was a warning and I could not identify any issues with functionality I chose to allow this exception for the MVP.

<br>

| File path                                                                                    | File Type | HTML | CSS  | JavaScript | Python | GitPod errors |
| -------------------------------------------------------------------------------------------- | --------- | ---- | ---- | ---------- | ------ | ------------- |
| bag/static/css/bag.css                                                                       | CSS       |      | PASS |            |        | PASS          |
| bag/templates/bag/includes/bag-total.html                                                    | HTML      | PASS |      |            |        | PASS          |
| bag/templates/bag/includes/checkout-buttons.html                                             | HTML      | PASS |      |            |        | PASS          |
| bag/templates/bag/includes/product-image.html                                                | HTML      | PASS |      |            |        | PASS          |
| bag/templates/bag/includes/product-info.html                                                 | HTML      | PASS |      |            |        | PASS          |
| bag/templates/bag/includes/quantity-form.html                                                | HTML      | PASS |      |            |        | PASS          |
| bag/templates/bag/bag.html                                                                   | HTML      | PASS |      |            |        | PASS          |
| bag/templatetags/bag\_tools.py                                                               | PY        |      |      |            | PASS   | PASS          |
| bag/apps.py                                                                                  | PY        |      |      |            | PASS   | PASS          |
| bag/contexts.py                                                                              | PY        |      |      |            | PASS   | PASS          |
| bag/urls.py                                                                                  | PY        |      |      |            | PASS   | PASS          |
| bag/views.py                                                                                 | PY        |      |      |            | PASS   | PASS          |
| checkout/static/css/checkout.css                                                             | CSS       |      | PASS |            |        | PASS          |
| checkout/static/js/stripe\_elements.js                                                       | JS        |      |      | EXC        |        | PASS          |
| checkout/templates/checkout/checkout\_success.html                                           | HTML      | PASS |      |            |        | PASS          |
| checkout/templates/checkout/checkout.html                                                    | HTML      | PASS |      |            |        | PASS          |
| checkout/admin.py                                                                            | PY        |      |      |            | PASS   | PASS          |
| checkout/apps.py                                                                             | PY        |      |      |            | PASS   | PASS          |
| checkout/forms.py                                                                            | PY        |      |      |            | PASS   | PASS          |
| checkout/models.py                                                                           | PY        |      |      |            | PASS   | EXC           |
| checkout/signals.py                                                                          | PY        |      |      |            | PASS   | PASS          |
| checkout/urls.py                                                                             | PY        |      |      |            | PASS   | PASS          |
| checkout/views.py                                                                            | PY        |      |      |            | PASS   | PASS          |
| checkout/webhook\_handler.py                                                                 | PY        |      |      |            | PASS   | EXC           |
| checkout/webhooks.py                                                                         | PY        |      |      |            | PASS   | EXC           |
| company/static/css/company\_pages.css                                                        | CSS       |      | PASS |            |        | PASS          |
| company/templates/accessibility\_statement.html                                              | HTML      | PASS |      |            |        | PASS          |
| company/templates/contact.html                                                               | HTML      | PASS |      |            |        | PASS          |
| company/templates/copyright\_statement.html                                                  | HTML      | PASS |      |            |        | PASS          |
| company/templates/faqs.html                                                                  | HTML      | PASS |      |            |        | PASS          |
| company/templates/health\_benefits.html                                                      | HTML      | PASS |      |            |        | PASS          |
| company/templates/our\_story.html                                                            | HTML      | PASS |      |            |        | PASS          |
| company/templates/sustainability.html                                                        | HTML      | PASS |      |            |        | PASS          |
| company/templates/terms\_and\_conditions.html                                                | HTML      | PASS |      |            |        | PASS          |
| company/admin.py                                                                             | PY        |      |      |            | PASS   | PASS          |
| company/apps.py                                                                              | PY        |      |      |            | PASS   | PASS          |
| company/forms.py                                                                             | PY        |      |      |            | PASS   | PASS          |
| company/models.py                                                                            | PY        |      |      |            | PASS   | PASS          |
| company/urls.py                                                                              | PY        |      |      |            | PASS   | PASS          |
| company/views.py                                                                             | PY        |      |      |            | PASS   | PASS          |
| [https://the-coffee-collective.herokuapp.com/](https://the-coffee-collective.herokuapp.com/) | HTML      | PASS |      |            |        | PASS          |
| home/apps.py                                                                                 | PY        |      |      |            | PASS   | PASS          |
| home/urls.py                                                                                 | PY        |      |      |            | PASS   | PASS          |
| home/views.py                                                                                | PY        |      |      |            | PASS   | PASS          |
| products/static/css/products.css                                                             | CSS       |      | PASS |            |        | PASS          |
| products/templates/products/custom\_widget\_templates/custom\_clearable\_file\_input.html    | HTML      | PASS |      |            |        | PASS          |
| products/templates/products/includes/quantity\_input\_script.html                            | HTML      | PASS |      |            |        | PASS          |
| products/templates/products/add\_product.html                                                | HTML      | PASS |      |            |        | PASS          |
| products/templates/products/delete\_product\_page.html                                       | HTML      | PASS |      |            |        | PASS          |
| products/templates/products/edit\_product.html                                               | HTML      | PASS |      |            |        | PASS          |
| products/templates/products/product\_detail.html                                             | HTML      | PASS |      |            |        | PASS          |
| products/templates/products/products.html                                                    | HTML      | PASS |      |            |        | PASS          |
| products/admin.py                                                                            | PY        |      |      |            | PASS   | PASS          |
| products/apps.py                                                                             | PY        |      |      |            | PASS   | PASS          |
| products/forms.py                                                                            | PY        |      |      |            | PASS   | PASS          |
| products/models.py                                                                           | PY        |      |      |            | PASS   | PASS          |
| products/urls.py                                                                             | PY        |      |      |            | PASS   | PASS          |
| products/views.py                                                                            | PY        |      |      |            | PASS   | PASS          |
| products/widgets.py                                                                          | PY        |      |      |            | PASS   | PASS          |
| profiles/static/css/profiles.css                                                             | CSS       |      | PASS |            |        | PASS          |
| profiles/static/js/profiles.js                                                               | JS        |      |      | EXC        |        | PASS          |
| profiles/templates/profiles/profile.html                                                     | HTML      | PASS |      |            |        | PASS          |
| profiles/apps.py                                                                             | PY        |      |      |            | PASS   | PASS          |
| profiles/forms.py                                                                            | PY        |      |      |            | PASS   | PASS          |
| profiles/models.py                                                                           | PY        |      |      |            | PASS   | PASS          |
| profiles/urls.py                                                                             | PY        |      |      |            | PASS   | PASS          |
| profiles/views.py                                                                            | PY        |      |      |            | PASS   | PASS          |
| static/css/style.css                                                                         | CSS       |      | PASS |            |        | PASS          |
| tcc/settings.py                                                                              | PY        |      |      |            | PASS   | PASS          |
| tcc/urls.py                                                                                  | PY        |      |      |            | PASS   | PASS          |
| tcc/views.py                                                                                 | PY        |      |      |            | PASS   | PASS          |
| tcc/wsgi.py                                                                                  | PY        |      |      |            | PASS   | PASS          |
| templates/allauth/account/confirm-email.html                                                 | HTML      | PASS |      |            |        | PASS          |
| templates/allauth/account/login.html                                                         | HTML      | PASS |      |            |        | PASS          |
| templates/allauth/account/logout.html                                                        | HTML      | PASS |      |            |        | PASS          |
| templates/allauth/account/signup.html                                                        | HTML      | PASS |      |            |        | PASS          |
| templates/errors/403.html                                                                    | HTML      | PASS |      |            |        | PASS          |
| templates/errors/404.html                                                                    | HTML      | PASS |      |            |        | PASS          |
| templates/errors/405.html                                                                    | HTML      | PASS |      |            |        | PASS          |
| templates/errors/500.html                                                                    | HTML      | PASS |      |            |        | PASS          |
| templates/includes/toasts/toast\_error.html                                                  | HTML      | PASS |      |            |        | PASS          |
| templates/includes/toasts/toast\_info.html                                                   | HTML      | PASS |      |            |        | PASS          |
| templates/includes/toasts/toast\_success.html                                                | HTML      | PASS |      |            |        | PASS          |
| templates/includes/toasts/toast\_warning.html                                                | HTML      | PASS |      |            |        | PASS          |
| templates/includes/footer.html                                                               | HTML      | PASS |      |            |        | PASS          |
| templates/includes/main-nav.html                                                             | HTML      | PASS |      |            |        | PASS          |
| templates/includes/mobile-top\_head.html                                                     | HTML      | PASS |      |            |        | PASS          |
| templates/base.html                                                                          | HTML      | PASS |      |            |        | PASS          |
| custom\_storages.py                                                                          | PY        |      |      |            | PASS   | PASS          |
| env.py                                                                                       | PY        |      |      |            | PASS   | EXC           |

<br>


## Bugs