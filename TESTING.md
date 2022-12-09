# Manual Testing

[Back to README](README.md)

The purpose of this document is to summarise the process, results, bugs and fixes as part of manually testing The Coffee Collective website.

Where a feature or functionality requires the support of multiple html files, for example the mobile/main-navs supporting the index page, I have tested the homepage page in its entirety, including the footer (as opposed to testing this files separately).

All tests were performed using the live environment deployed from Heroku.



## User Story Testing

The objective of this test is to validate that the user requirements have been delivered for the MVP release.
Further details of the Epics, Features and User Story tasks can be found either in the [GitHub Projects Kanban Board](https://github.com/users/RickofManc/projects/5/views/1), as an overview within the Design Thinking section of the [README](README.md) or within the TCC_Planning excel file in the [GitHub Repo](https://github.com/RickofManc/the-coffee-collective).

<br>


Ref  | User Story                                                                                                                                                                                                                             | Acceptance Criteria                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Result       | Rationale                                                                                                                                                                                                                                                                                                                                                  
---- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ | -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
US01 | As a Site User, I can understand what the site aim is and my options from viewing the homepage, so that I can intuitively navigate the site and have a good e-commerce experience                                                      | 1\. The site structure and layout should be clear and simple to navigate - all features within 2 clicks<br>2\. Site Users should be able to find products either from homepage adverts, Nav menu or Search function<br>3\. Site Users will have an option to register for a user account from the Navbar                                                                                                                                                                                                 | PASS         | Positive feedback from UAT evidenced that the sites aims are clear.                                                                                                                                                                                                                                                                                        
US03 | As a Site User, I can use the Footer for navigation, so that I can learn more about the business                                                                                                                                       | 1\. Footer is located at the bottom of every page<br>2\. Footer provides links that are clear and accessible                                                                                                                                                                                                                                                                                                                                                                                             | PASS         | There are links to company information within the footer. However from an accessibility perspective it is advised not to repeat menus within the same screen. As the navbar with links to company information is fixed to each page, only selective links have been added to the footer.                                                                   
US04 | As Site Owner, I want a brand logo, so Site Users can easily learn the type of products being sold                                                                                                                                     | 1\. A logo that is identifiable as relating to coffee products that will help build the brand<br>2\. Logo to be used within the Navbar                                                                                                                                                                                                                                                                                                                                                                   | PASS         | The company name is clear within the navbar and throughout the homepage. A logo has been used sparingly for the MVP.                                                                                                                                                                                                                                       
US05 | As a Site Owner, I can add products to the site, so I can manage the content and adapt to changes in stock and competition                                                                                                             | 1\. Successfully add a product from either the back or front end                                                                                                                                                                                                                                                                                                                                                                                                                                         | PASS         | A site owner can add new products either from a front end form when signed in, or from using the Django admin panel.                                                                                                                                                                                                                                       
US06 | As a Site Owner, I can edit existing products on the site, so I can manage the content and adapt to changes in stock and competition                                                                                                   | 1\. Successfully edit a product from either the back or front end                                                                                                                                                                                                                                                                                                                                                                                                                                        | PASS         | A site owner can edit existing products either from a front end form when signed in, or from using the Django admin panel.                                                                                                                                                                                                                                 
US07 | As a Site Owner, I can remove products from the site, so I can manage the content and adapt to changes in stock and competition                                                                                                        | 1\. Successfully remove a product from either the back or front end                                                                                                                                                                                                                                                                                                                                                                                                                                      | PASS         | A site owner can remove existing products either from a front end form when signed in, or from using the Django admin panel.                                                                                                                                                                                                                               
US08 | As a Site User, I can learn about a product from the details provided, so that I can make an informed decision to purchase                                                                                                             | 1\. Sufficient details on the product category pages that offer Title, Subtitle, Price with a view to enticing the user to click and learn more<br>2\. Product page with full descriptions in addition to those highlighted in 1.                                                                                                                                                                                                                                                                        | PASS         | Every product can be viewed in isolation complete with a subtitle and description. Other key pieces of information are contained within the product details page such as size (if applicable) and price.                                                                                                                                                   
US09 | As a Site User, I can easily navigate to the differing product lines by using clear and conventional categories, so that I can find specific items with ease, and move between sections of the shop                                    | 1\. Category views that are accessible from the Navbar menu<br>2\. Category views that correctly dissect product lines<br><br>                                                                                                                                                                                                                                                                                                                                                                           | PASS         | Drop-down menus from the fixed Navbar allow users to navigate to specific categories or see all products. To help users further the first main categories is either 'fresh coffee' or 'coffee making'.                                                                                                                                                     
US14 | As a Site Owner, I would like to use the homepage to promote items and key messages to users, so that I can drive traffic to the most beneficial areas                                                                                 | 1\. The revolving carousal has an hero image with a banner advertising sale items<br>2\. A button within the banner allows Site Users to be navigated to the product listing for sale items                                                                                                                                                                                                                                                                                                              | PASS         | A carousal has been incorporated into the homepage and offers the ability to navigate users to specific pages.                                                                                                                                                                                                                                             
US15 | As a Site User, I can view recommendations from existing customers, as it will help to inform my trust in the business                                                                                                                 | 1\. A dedicated section of the homepage, where Site Users will see recommendations from existing customers                                                                                                                                                                                                                                                                                                                                                                                               | PASS         | Product reviews are enabled for all products. To leave a review you must be registered and have verified the account through email confirmation.                                                                                                                                                                                                           
US16 | As a Site User, I can learn more about the business, so that I can assess trustworthiness and culture that may import a decision to purchase                                                                                           | 1\. A dedicated section of the homepage, where Site Users will learn more about the business, their location and opening times for a visit or free order collection                                                                                                                                                                                                                                                                                                                                      | PASS         | There is a dedicated menu to learn all 'about' the business, their history and values.                                                                                                                                                                                                                                                                     
US17 | As a Site User, I can find out where the coffee shop is located, so that I can collect an order or visit for a coffee                                                                                                                  | 1\. A dedicated section of the homepage for the business location and opening times, plus details on collecting orders placed online                                                                                                                                                                                                                                                                                                                                                                     | PASS         | The business's physical location is clearly displayed on the homepage.                                                                                                                                                                                                                                                                                     
US18 | As a Site User, I would like to make a transaction without registering for a user account, as this is either a one off purchase or is my preference not to have a company hold my details                                              | 1\. Not registered users can checkout without an account whilst still maintaining all checkout functionality<br>                                                                                                                                                                                                                                                                                                                                                                                         | PASS         | Site users can checkout without being a registered user.                                                                                                                                                                                                                                                                                                   
US19 | As a Site User, I would like my delivery details to be pre-populated when I come to pay, as this would be more convenient and ease my experience and time to purchase                                                                  | 1\. Pre-populated delivery details that can be overridden manually in the checkout area for authenticated users                                                                                                                                                                                                                                                                                                                                                                                          | PASS         | Site users with a registered account will either have their delivery details stored following their first transaction, or can add them manually to their profile before a transaction.                                                                                                                                                                     
US20 | As a Site User, I would like to adjust the quantity or remove items from my shopping bag, in case I change my mind when assessing all my items before purchasing                                                                       | 1\. Site Users can increase or decrease the quantity of items within them shopping bag as part of the checkout process                                                                                                                                                                                                                                                                                                                                                                                   | PASS         | Site users have the functionality to increase or decrease items within their bag before checking out. Users can also remove items completely.                                                                                                                                                                                                              
US21 | As a Site User, I can register an account, so that I can add reviews                                                                                                                                                                   | 1\. Site Users are provided with a simple Form to complete in order to register an account<br>2\. Form fields should follow convention for sign-up forms<br>3\. Form buttons should enable the Form to be submitted or reset if an error has been made                                                                                                                                                                                                                                                   | PASS         | Users can sign-up for an account using a simple form and following instructions within to verify their account.                                                                                                                                                                                                                                            
US22 | As a Site User, I can sign-in to my account, so that I can utilise member benefits                                                                                                                                                     | 1\. Site Users will be able to sign-in from clicking a link in the Navbar menu<br>2\. Sites Users will be required to enter their Username and Password to sign-in<br>3\. A message should confirm to Site Users when they have successfully signed in<br>4\. A message should inform Site Users if the information entered was not valid, and to try again                                                                                                                                              | PASS         | Site users can register for an account. Whilst for MVP the features are limited to storing default delivery details and viewing previous transactions, further benefits can be introduced for later releases as the foundations are built.                                                                                                                 
US23 | As a Site User, I can be asked to confirm my request to sign-out, so that I can cancel if requested in error                                                                                                                           | 1\. Site Users will be able to sign-out from clicking a link in Navbar menu<br>2\. A page will display asking Site Users to confirm they would like to proceed to sign-out, or continue using the site<br>3\. If Site Users confirm they would like to sign-out they will be signed out and redirected to the home page<br>4\. A message should confirm to Site Users when they have successfully signed out<br>5\. If Site Users choose to continue using their account, access to features will remain | PASS         | Using the inbuilt functionality of Django, users are asked to confirm their request to sign-out.                                                                                                                                                                                                                                                           
US24 | As a Site User, I can view and change profile details, so that they are correct when I come to checkout                                                                                                                                | 1\. Site Users can navigate to a restricted page that provides all the relevant profile details<br>2\. Site Users can amend any part of the information and save the changes<br>3\. A success message will confirm the changes have been saved                                                                                                                                                                                                                                                           | PASS         | Registered site users can edit their default delivery details within the profile area. A success message confirm the changes have been saved.                                                                                                                                                                                                              
US25 | As a Site User, I can add a product review, so that I can inform potential customers of what they might expect<br><br>                                                                                                                 | 1\. Authenticated users will be able to post a review on a detailed product page<br>2\. Site Users will be limited to a conventional 280 characters<br>3\. A button clearly stating to 'Submit' their review will be available<br>4\. Site Users will be able to see their post instantly<br>                                                                                                                                                                                                            | PASS         | Registered site users can add a product review directly to the website. Consideration was given to adding an approval step before publishing the comment, however to provide a positive user experience, I opted to publish the review straight away. These can be reviewed by the business owner and deleted from the Django admin area if deemed abusive.
US27 | As a Site User, I can view my recent activity, so that I can learn behaviour traits i.e. which podcast categories I like most, where I have posted comments etc.                                                                       | 1\. Site Users profile page has an additional section that provides an overview of recent activity                                                                                                                                                                                                                                                                                                                                                                                                       | PASS         | Site users can view previous transactions from within their profile section (if signed in).                                                                                                                                                                                                                                                                
US30 | As Site Owner, I would like Site Users to register for a monthly newsletter, so that I can build a relationship with customers and promote specific products                                                                           | 1\. Site User can enter an email address and receive a success message within the browser<br>2\. Site Users will receive confirmation of sign-up to their inbox                                                                                                                                                                                                                                                                                                                                          | PASS         | Site users can subscribe to the newsletter using the Mailchimp feature on the homepage. Users do not have to register to subscribe and stay updated with products and news.                                                                                                                                                                                
US31 | As Site Owner, I would like to provide Site Users with more information on the business, so that Site Users can understand the history, manufacturing process, culture etc. with a view to increasing trust and building relationships | 1\. Site Users will be able to access this page from either the Footer<br>2\. Site Users will be navigated to a new page which informs of who, when, why and what the business is about<br>3\. Site Users will be offered an opportunity to register an account following learning more about the business                                                                                                                                                                                               | PASS         | There is a dedicated section to learn about the story  of the business and the owners during the years.                                                                                                                                                                                                                                                    
US32 | As Site Owner, I can provide a contact form for Site Users, so they can provide feedback, request products, features etc.                                                                                                              | 1\. Site Users will be able to access this page from the Footer<br>2\. Site Users will be introduced to the FAQ page in case they hadn't already viewed this information and could of had their question answered<br>3\. Site Users will be provided with a Form to complete, learning where the Form is sent and when to expect a response<br>4\. Site Users will be redirected to the homepage when the form has been successfully submitted                                                           | PASS         | There is a contact form available for Site Users to send a query, concern or request to the business owners.<br>Feedback is provided to the users to confirm the form has been sent successfully.                                                                                                                                                          
US33 | As a Site User, I can find answers to general questions, so that I don't have to wait for a response from the Site Owner                                                                                                               | 1\. Site Users most popular questions can be answered in a single page that is conveniently accessed from the Main Menu or Footer<br>2\. Site Users will be provided with a link to contact Site Admin if a question cannot be answered                                                                                                                                                                                                                                                                  | PASS         | The FAQ's provide a broad range of answers to typical questions. These can be added to by the developers as required. FAQ's can be navigated to from the Footer and About menu in the navbar.                                                                                                                                                              
US34 | As a Site User, I can find out how the Site Owner has made content accessible, so that I can interact as designed                                                                                                                      | 1\. Site Users will be able to learn how the business cares are about accessibility and about users, plus provide information about the accessibility of our content<br>                                                                                                                                                                                                                                                                                                                                 | PASS         | The Accessibility Statement can be found within the 'About' menu from the main navbar.                                                                                                                                                                                                                                                                     
US35 | As a Site User, I can learn the terms and conditions of having a user account and transacting with this e-commerce site, so that I can understand by obligations and responsibilities pre and post purchase                            | 1\. Clicking a Footer link will navigate Site Users to a page that displays the Terms & Conditions                                                                                                                                                                                                                                                                                                                                                                                                       | PASS         | T&C's information can be found within the 'About' menu from the main navbar. It was considered unnecessary to have another link within the footer.                                                                                                                                                                                                         
US36 | As a Site User, I can learn about the Copyright aspects of this site, so that I do not infringe on copyright rules                                                                                                                     | 1\. Site Users will be able to learn about the Copyright use for The Coffee Collective by clicking on a link within the Footer<br>2\. Clicking the link will navigate Site Users to a page that displays the Copyright statement                                                                                                                                                                                                                                                                         | PASS         | Copyright information can be found within the 'About' menu from the main navbar.                                                                                                                                                                                                                                                                           
US37 | As a Site User, I can access the site on differing devices, so I can interact with content on my preferred device                                                                                                                      | 1\. Successful tests for Responsiveness using Developer Tools<br>2\. Successful tests for Responsiveness through manual testing on differing devices                                                                                                                                                                                                                                                                                                                                                     | PASS         | Primarily using the Bootstrap framework the website is responsive across devices. This has been tested through a dedicated test for responsiveness.                                                                                                                                                                                                        
US02 | As a Site User, I can search for products by entering descriptive words, so that I can find what I want quickly                                                                                                                        | 1\. Search functionality is accessible from the Navbar<br>2\. All keywords, names, descriptions return results                                                                                                                                                                                                                                                                                                                                                                                           | PARTIAL PASS | Whilst the search functionality is operational, more than one search word produces zero results. This is being taken forward as a bug to fix.                                                                                                                                                                                                              

<br>


## User Acceptance Testing

To ensure the website is meeting real world expectations, I asked other developers to review and feedback on their user experience. 

These tests provided rich insight into the practicalities and behaviours of the features and functions. From the issues identified (below) I will change some features to improve the user experience ahead of MVP release.

1. Whilst the user enjoyed the success feedback from leaving a product review, they felt it was strange to be reminded of what had been added to the shopping bag at the same time. Can we decouple the bag from the toast success - so that a bag toast is only displayed when adding or removing items from the bag.
1. One user whilst testing on an iPhone expected to see the homepage article on the owner Luca to be centralised to follow the format of the business location and opening times above. To fix I will centralise these items for mobile devices only.
1. When testing the 'search' feature, users highlighted results only seemed to be found if the search criteria was a single word. I could replicate the issue, and it will take some further investigation to resolve.
1. The use of a product rating is misleading as users were looking to be able to add a rating as well as, or as part of adding a product review. Consider removing the rating unless we can provide functionality for users to interact with the rating. Possibly change this to a 'like' system which would provide a method for leaving quick feedback.
1. The use of the 'Intensity' field as a method of sorting products works well if sorting coffee products. However it loses its value and is a little misleading for non-coffee products. To fix I will investigate whether we can limit the displaying of this field to only show on the coffee relating pages, otherwise it may be clearer to remove as a sorting options.

<br>


## Page Validation

This test aims to check all features and links from across the site are working as designed and developed.

To perform the test I used a Chrome browser, and validated each page from a mobile and desktop perspective using the inbuilt developer tool as some features were unique to a particular screen size.

The results were largely positive with two noticeable fails.
* As a site admin performing a product delete from the front end, a 500 Internal Server Error was triggered after clicking submit on the final screen. This requires further investigation.
* A link contained on the Our Story page to navigate users to sign-in/register is broken as it directs users to the homepage.

<br>

File path                                                                                    | Features working | Links active
-------------------------------------------------------------------------------------------- | ---------------- | ------------
bag/templates/bag/bag.html                                                                   | PASS             | PASS        
checkout/templates/checkout/checkout\_success.html                                           | PASS             | PASS        
checkout/templates/checkout/checkout.html                                                    | PASS             | PASS        
company/templates/accessibility\_statement.html                                              | PASS             | PASS        
company/templates/contact.html                                                               | PASS             | PASS        
company/templates/copyright\_statement.html                                                  | PASS             | PASS        
company/templates/faqs.html                                                                  | PASS             | PASS        
company/templates/health\_benefits.html                                                      | PASS             | PASS        
company/templates/our\_story.html                                                            | PASS             | FAIL        
company/templates/sustainability.html                                                        | PASS             | PASS        
company/templates/terms\_and\_conditions.html                                                | PASS             | PASS        
[https://the-coffee-collective.herokuapp.com/](https://the-coffee-collective.herokuapp.com/) | PASS             | PASS        
products/templates/products/add\_product.html                                                | PASS             | PASS        
products/templates/products/delete\_product\_page.html                                       | FAIL             | FAIL        
products/templates/products/edit\_product.html                                               | PASS             | PASS        
products/templates/products/product\_detail.html                                             | PASS             | PASS        
products/templates/products/products.html                                                    | PASS             | PASS        
profiles/templates/profiles/profile.html                                                     | PASS             | PASS        
templates/allauth/account/confirm-email.html                                                 | PASS             | PASS        
templates/allauth/account/login.html                                                         | PASS             | PASS        
templates/allauth/account/logout.html                                                        | PASS             | PASS        
templates/allauth/account/signup.html                                                        | PASS             | PASS        
templates/errors/403.html                                                                    | PASS             | PASS        
templates/errors/404.html                                                                    | PASS             | PASS        
templates/errors/405.html                                                                    | PASS             | PASS        
templates/errors/500.html                                                                    | PASS             | PASS        


<br>


## Responsiveness

To test the websites layout and content remains well structured and accessible across differing screen sizes, I used Chrome's Developer Tools to virtualise how the website and all it's pages look and feel. In consideration that I opted to use Bootstrap which provides standard media queries for screen sizes from XS through to XL, I selected the following screens to test on; iPhone 4, iPhone SE, Samsung Galaxy S8, iPad, iPad Pro, Laptop at 1366x768, Monitor at 1920x1080 and iMac 5K.

In summary of the results, very few bugs were identified; 
* Small changes to padding and margin sizes for the FAQ's section to ensure I was maximising the use of mobile screens.
* The homepage failed on mobile devices as the container for the nav-menu toggle button was too large and covering other navbar links. This was a simple resizing fix for the container.
* The homepage failed on tablets as elements from both the mobile and desktop navbar were showing at the same time. The fix involved readdressing the out of the box class names from Bootstrap to ensure only the right elements showed on the right screen widths.

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

Using Chrome's developer tool 'Lighthouse Testing' all pages were tested. At a high-level the tool tests performance in terms of loading speed, best-practice in regards to layout, SEO for how searchable the website and how accessible it is for visually impaired users who may also require a screen reader. 
The results below show mobile in the first 4 columns and desktop in the second 4 columns.
To try and achieve clear and consistent results I used an incognito version of Chrome.

In general the website scored highly across all tests against a desktop criteria. However for the same tests on a mobile, the following issues were identified.

* The tool considered the use of inbuilt Django forms for pages such as adding products and contacting the business, as an issue due to them not being supported by screen readers. However this was not raised as an issue for the desktop test.
* The homepage on mobiles was the most concerning aspect as the page was considered far too long in performing the initial load. Helpfully the tool advises different resolutions. To improve the loading time I tried to defer or synchronise some of the script loading however on test the relating features failed to load. When testing on devices I felt the page loading time on mobiles and tablets was within what I expect from websites. I will continue to look at resizing the main images to improve performance.

<br>

| File path                                                                                    | Performance | Accessibility | Best Practice | SEO | Performance | Accessibility | Best Practice | SEO |
| -------------------------------------------------------------------------------------------- | ----------- | ------------- | ------------- | --- | ----------- | ------------- | ------------- | --- |
| bag/templates/bag/bag.html                                                                   | 41          | 89            | 100           | 92  | 93          | 90            | 100           | 90  |
| checkout/templates/checkout/checkout\_success.html                                           | 36          | 100           | 100           | 100 | 95          | 100           | 100           | 100 |
| checkout/templates/checkout/checkout.html                                                    | 35          | 96            | 100           | 100 | 92          | 94            | 100           | 100 |
| company/templates/accessibility\_statement.html                                              | 72          | 100           | 100           | 100 | 92          | 100           | 100           | 100 |
| company/templates/contact.html                                                               | 77          | 100           | 100           | 100 | 96          | 100           | 100           | 100 |
| company/templates/copyright\_statement.html                                                  | 77          | 100           | 100           | 100 | 98          | 100           | 100           | 100 |
| company/templates/faqs.html                                                                  | 71          | 100           | 100           | 100 | 95          | 100           | 100           | 100 |
| company/templates/health\_benefits.html                                                      | 72          | 100           | 100           | 100 | 97          | 100           | 100           | 100 |
| company/templates/our\_story.html                                                            | 70          | 100           | 100           | 100 | 95          | 100           | 100           | 100 |
| company/templates/sustainability.html                                                        | 72          | 100           | 100           | 100 | 98          | 100           | 100           | 100 |
| company/templates/terms\_and\_conditions.html                                                | 55          | 100           | 100           | 100 | 95          | 100           | 100           | 100 |
| [https://the-coffee-collective.herokuapp.com/](https://the-coffee-collective.herokuapp.com/) | 36          | 98            | 100           | 100 | 75          | 98            | 100           | 100 |
| products/templates/products/add\_product.html                                                | 39          | 91            | 100           | 100 | 90          | 92            | 100           | 100 |
| products/templates/products/delete\_product\_page.html                                       | 60          | 98            | 92            | 100 | 87          | 100           | 100           | 100 |
| products/templates/products/edit\_product.html                                               | 55          | 81            | 83            | 92  | 92          | 84            | 100           | 90  |
| products/templates/products/product\_detail.html                                             | 68          | 89            | 92            | 92  | 95          | 89            | 100           | 90  |
| products/templates/products/products.html                                                    | 61          | 100           | 92            | 92  | 83          | 100           | 100           | 90  |
| profiles/templates/profiles/profile.html                                                     | 66          | 100           | 100           | 100 | 96          | 100           | 100           | 100 |
| templates/allauth/account/confirm-email.html                                                 | 80          | 100           | 100           | 100 | 96          | 100           | 100           | 100 |
| templates/allauth/account/login.html                                                         | 71          | 100           | 100           | 100 | 96          | 100           | 100           | 100 |
| templates/allauth/account/logout.html                                                        | 71          | 100           | 100           | 100 | 96          | 100           | 100           | 100 |
| templates/allauth/account/signup.html                                                        | 69          | 100           | 100           | 100 | 98          | 100           | 100           | 100 |
| templates/errors/403.html                                                                    | NP          | NP            | NP            | NP  | NP          | NP            | NP            | NP  |
| templates/errors/404.html                                                                    | NP          | NP            | NP            | NP  | NP          | NP            | NP            | NP  |
| templates/errors/405.html                                                                    | NP          | NP            | NP            | NP  | NP          | NP            | NP            | NP  |
| templates/errors/500.html                                                                    | NP          | NP            | NP            | NP  | NP          | NP            | NP            | NP  |


<br>


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
* profiles.js and stripe_elements.js - ES6 warning to use 'esversion:6'. I researched a fix and added JSHint ES6 to the settings.JSON file, however this did not clear the warning. As this was a warning and I could not identify any issues with functionality I chose to allow this exception for the MVP.

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

The following bugs were identified as part of the testing phase and will be investigated further to find a fix.

### Bugs that require a fix for MVP

B1. As a site admin performing a product delete from the front end, a 500 Internal Server Error was triggered after clicking submit on the final screen. This requires further investigation.<br>
B2. A link contained on the Our Story page to navigate users to sign-in/register is broken as it directs users to the homepage.<br>

### Bugs that require further investigation and potentially fixed for MVP

B3. Decouple the bag details from the toast success - so that a bag toast is only displayed when adding or removing items from the bag. This will improve the users experience through clearly feeding back on how they are interacting with the site.<br>
B4. Centralise the image of Luca and text from the homepage on mobile devices - so that it follows the format of the business location and opening times above.<br>
B5. Investigate why search results are not found when entering more than one descriptive word, or not returning results as expected.<br>
B6. To avoid user confusion, consider removing the product rating unless we can provide functionality for users to interact with the rating. Possibly change this to a 'like' system which would provide a method for leaving quick feedback.<br>
B7. The use of the 'Intensity' field as a method of sorting products works well if sorting coffee products. However it loses its value and is a little misleading for non-coffee products. To fix I will investigate whether we can limit the displaying of this field to only show on the coffee relating pages, otherwise it may be clearer to remove as a sorting options.<br>
B8. The homepage initial load on mobiles is scoring poorly on Chromes Developer Tools. Investigate whether resizing images will improve page loading times for mobiles.<br>


### Bugs that won't be fixed for MVP

B9. There was one isolated issue whereby the inherit styles for the Mailchimp element didn't load completely correct on my local machine when using Firefox. This also included the 'Subscribe' button not being functional. I tried to replicate this virtually using Firefox within the Lambda tool, however the feature loaded correctly and was functional.<br>
B10. env.py code error - E501 as line breached 79 characters, however when I tried to split the Database URL over two lines it not longer functioned. As a result I have chosen to allow this exception for the MVP.<br>
B11. profiles.js and stripe_elements.js code errors - ES6 warning to use 'esversion:6'. I researched a fix and added JSHint ES6 to the settings.JSON file, however this did not clear the warning. As this was a warning and I could not identify any issues with functionality I chose to allow this exception for the MVP.<br>