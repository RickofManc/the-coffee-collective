# Manual Testing

[Back to README](README.md)

The purpose of this document is to summarise the process, results, bugs and fixes as part of manually testing The Coffee Collective website.



## Epics & functionality
* Epics & functionality - validating the requirements have been delivered for the MVP release.



## Page Validation
* Page validation - ensuring that all features are working, including all links perform as designed.



## Responsiveness
* Responsiveness - ensuring each page is responsive through the three media queries covering mobiles, tablets-laptops and desktop monitors.



## Accessibility 
* Accessibility - each page is tested for compliance with accessibility guidelines using the WAVE online assessment tool.



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


| File path                                                                                    | File Type | HTML | CSS | JavaScript | Python | GitPod errors |
| -------------------------------------------------------------------------------------------- | --------- | ---- | --- | ---------- | ------ | ------------- |
| bag/templates/bag/includes/bag-total.html                                                    | HTML      | PASS |     |            |        | PASS          |
| bag/templates/bag/includes/checkout-buttons.html                                             | HTML      | PASS |     |            |        | PASS          |
| bag/templates/bag/includes/product-image.html                                                | HTML      | PASS |     |            |        | PASS          |
| bag/templates/bag/includes/product-info.html                                                 | HTML      | PASS |     |            |        | PASS          |
| bag/templates/bag/includes/quantity-form.html                                                | HTML      | PASS |     |            |        | PASS          |
| bag/templates/bag/bag.html                                                                   | HTML      | PASS |     |            |        | PASS          |
| checkout/templates/checkout/checkout\_success.html                                           | HTML      | PASS |     |            |        | PASS          |
| checkout/templates/checkout/checkout.html                                                    | HTML      | PASS |     |            |        | PASS          |
| company/templates/accessibility\_statement.html                                              | HTML      | PASS |     |            |        | PASS          |
| company/templates/contact.html                                                               | HTML      | PASS |     |            |        | PASS          |
| company/templates/copyright\_statement.html                                                  | HTML      | PASS |     |            |        | PASS          |
| company/templates/faqs.html                                                                  | HTML      | PASS |     |            |        | PASS          |
| company/templates/our\_story.html                                                            | HTML      | PASS |     |            |        | PASS          |
| company/templates/sustainability.html                                                        | HTML      | PASS |     |            |        | PASS          |
| company/templates/terms\_and\_conditions.html                                                | HTML      | PASS |     |            |        | PASS          |
| [https://the-coffee-collective.herokuapp.com/](https://the-coffee-collective.herokuapp.com/) | HTML      | PASS |     |            |        | PASS          |
| products/templates/products/custom\_widget\_templates/custom\_clearable\_file\_input.html    | HTML      | PASS |     |            |        | PASS          |
| products/templates/products/includes/quantity\_input\_script.html                            | HTML      | PASS |     |            |        | PASS          |
| products/templates/products/add\_product.html                                                | HTML      | PASS |     |            |        | PASS          |
| products/templates/products/delete\_product\_page.html                                       | HTML      | PASS |     |            |        | PASS          |
| products/templates/products/edit\_product.html                                               | HTML      | PASS |     |            |        | PASS          |
| products/templates/products/product\_detail.html                                             | HTML      | PASS |     |            |        | PASS          |
| products/templates/products/products.html                                                    | HTML      | PASS |     |            |        | PASS          |
| profiles/templates/profiles/profile.html                                                     | HTML      | PASS |     |            |        | PASS          |
| templates/allauth/account/confirm-email.html                                                 | HTML      | PASS |     |            |        | PASS          |
| templates/allauth/account/login.html                                                         | HTML      | PASS |     |            |        | PASS          |
| templates/allauth/account/logout.html                                                        | HTML      | PASS |     |            |        | PASS          |
| templates/allauth/account/signup.html                                                        | HTML      | PASS |     |            |        | PASS          |
| templates/errors/403.html                                                                    | HTML      | PASS |     |            |        | PASS          |
| templates/errors/404.html                                                                    | HTML      | PASS |     |            |        | PASS          |
| templates/errors/405.html                                                                    | HTML      | PASS |     |            |        | PASS          |
| templates/errors/500.html                                                                    | HTML      | PASS |     |            |        | PASS          |
| templates/includes/toasts/toast\_error.html                                                  | HTML      | PASS |     |            |        | PASS          |
| templates/includes/toasts/toast\_info.html                                                   | HTML      | PASS |     |            |        | PASS          |
| templates/includes/toasts/toast\_success.html                                                | HTML      | PASS |     |            |        | PASS          |
| templates/includes/toasts/toast\_warning.html                                                | HTML      | PASS |     |            |        | PASS          |
| templates/includes/footer.html                                                               | HTML      | PASS |     |            |        | PASS          |
| templates/includes/main-nav.html                                                             | HTML      | PASS |     |            |        | PASS          |
| templates/includes/mobile-top\_head.html                                                     | HTML      | PASS |     |            |        | PASS          |
| templates/base.html                                                                          | HTML      | PASS |     |            |        | PASS          |

## Bugs