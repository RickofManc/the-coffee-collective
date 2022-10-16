# The Coffee Collective

[Insert Website Mockup]

[Insert Link to Live Website]

[GitHub Repo](https://github.com/RickofManc/the-coffee-collective)


***


## Background

<br />

The Coffee Collective is a small family run cart serving fresh coffee to city workers in Manchester. The family migrated from Italy in the 1970's and established a business that would allow them to use their knowledge and skills to help their new home. A cart was created and peddled to the city each morning to sell coffee to Mancunians. In the days before takeaway cups, customers stood and socialised whilst sipping their morning espressos and so became known to passers-by and onlookers as "the coffee collective".

***
<br />

## Index - Table of Contents

* [User Experience R&D](#user-experience-research-and-design)
    * [Strategy](#strategy)
    * [Scope](#Scope)
    * [Structure](#Structure)
    * [Skeleton](#Skeleton)
    * [Surface](#Surface)
* [Data Model](#Data-Model) 
* [Features](#Features)
* [Testing](#Testing)
* [Deployment](#Deployment)
* [Credit & Attributes](#Credit&Attributes)

<br />

***
<br />

## User Experience Research and Design

<br />

### Problem Statement

During the last forty years the family has diversified and setup a popular shop in the city where patrons still stand and socialise. The shop has become so popular that many coffee roasters provide bags of coffee for sale as some customers like to enjoy fresh coffee in work or at home. The COVID pandemic reduced the footfall considerably and whilst the cart was used for supplying coffee outside and socially distanced, the family know an e-commerce site would greatly help their financial stability. Furthermore, due to their popularity, the local coffee roasters would welcome the opportunity to sell their products through another channel.

<br />

### Objective

Understand the user requirements to enable development of a B2C web application that allows The Coffee Collective's customers to purchase coffee online with delivery to their chosen address. The e-commerce site will also allow the family to promote new stock lines such as coffee cups, coffee making equipment and clothing. Customers will have an option to create a user account to ease future transactions through saved details, view order history etc. All site visitors will have the opportunity to sign-up for latest news and promotions delivered monthly by email.

<br />

### Design Thinking

Following a design thinking approach and using the knowledge and experience of the Nielsen Norman Group, the following key personas have been used to empathize with and understand their needs.

<details><summary><b>User Personas</b></summary>
    <p align="center">
        <img src="readme-images/the_coffee_collective_user_personas.png" alt="User Personas highlighting the needs of the differing types of users"/>
    </p>
</details><br />

The output from this phase supported the ideation of potential features and also the creation of User Stories complete with Acceptance Criteria and high-level tasks for the Development Phase. The GitHub Projects Kanban Board has been used to prioritise, update and track all User Stories through to completion. Note this Kanban Board was also used for bug fixing and issue resolution, please see the Testing section of this document for further information.

The table below provide an overview of how the features are driving the epics, that in turn have been used to develop the user stories required to deliver the features.


<details><summary><b>Epics and User Stories Overview</b></summary>
    <p align="center">
        <img src="readme-images/the_coffee_collective_epics_and_user_stories.png" alt="Table highlighting the Epics, Features and User Stories"/>
    </p>
</details><br />

<br />

#### Strategic Opportunities

A list of features has been established from the User Stories. These features have been assessed using the MoSCoW method to understand which features are essential for the MVP and which could be re-prioritised for a future release. Following this assessment I looked at how feasible each of these features is to develop within the time frame. The chart below highlights the output from this evaluation. Overall this critical stage of analysis ensures the features that are available and will provide immediate user benefit, and in turn value for the business will be developed first.


<details><summary><b>MoSCoW Features Assessment</b></summary>
    <p align="center">
        <img src="readme-images/the_coffee_collective_MoSCoW_assessment.png" alt="Table highlighting each features assessment of Must do, Should do, Could do and Won't do (for the MVP)"/>
    </p>
</details><br />


<details><summary><b>Importance versus Feasibility Assessment</b></summary>
    <p align="center">
        <img src="readme-images/the_coffee_collective_importance_versus_feasibility_assessment.png" alt="Table highlighting each features assessment of importance versus feasibility for the MVP"/>
    </p>
</details><br />


<p align="center">
    <img src="readme-images/the_coffee_collective_features_roadmap.png" alt="Chart highlighting each features assessment for importance against feasibility for the MVP"/>
</p>

<br />

### Scope

An agile approach of keeping the features simple and aligned to the strategy for the MVP will be adopted. This will allow the business to understand which are driving benefit, and therefore should be developed further. Below is a list of the leading features for this project.


#### In Scope Features
* Responsive Navbar complete with product search, category menus, user account access.
* A streamlined checkout that is easy-to-edit and retains products between visits.
* New product listings, discounts and recommendations visible on the homepage.
* Optional user accounts with editable profile data, order history and the storing of shipping details
* Registered users will be able to leave product reviews to help build trust in the products for new customers.
* A 10% discount code provided to those users signing up for the monthly newsletter.
* Free shipping on orders over £45.
* Business pages to inform of the company, and their position towards Accessibility, Copyright etc.
* Clear Terms & Conditions.
* All site visitors should have an option to share a product listing via social media.
* FAQ's to help the users navigation and experience of the site and service


#### Out of Scope Features - for future release
* Site visitors being able to compare products side by side.
* Realtime stock inventory updating the site when a product is out of stock.
* Single Sign-on to user accounts with social media logins.
* The status of a placed order with the users account area.
* Sale of e-vouchers to buy as gifts to be redeemed in the store.
* Country/Language switching for global shopping convenience.

<br />


### Structure

This website will be built with the following design considerations. The final structure for the MVP may differ slightly as development progresses from user feedback and testing.

* A hierarchal structure where the homepage will act as a landing pad with key links and useful information.
* The Navbar will provide menu buttons to the differing product categories.
* Each product category page will have the ability to filter the results. Clicking on a product will reveal further information about the product and provide the ability to add to bag.
* All of the above, and the user account, checkout, and business pages will be no more than 3 clicks away.
* The Navbar menu will be simple in design and layout, collapsing for mobile and tablet devices.
* Breadcrumbs will be added to the top of desktop pages allowing visitors to quickly navigate back to a previous section.
* A sitemap (available from the Footer) will display all the important categories and pages in a single page so users can find easily what they want.


<br />

### Skeleton

Key to meeting delivering for the differing user personas is a homepage that can immediately meet their priority requirements whilst not over complicating the UI with too much information, and too many choices. The hierarchal structure will be supported by the Navbar that within a click can navigated users to the main product categories. Similarly the homepage will host a carousel with a hero image enticing users who want to either find sale items, or learn more about the products.

The homepage will also act as the main point of navigation to allow users to learn more about the business, the benefits of coffee and links to useful resources i.e. FAQ's.

Aesthetically the layout and content will be clean and clear to promote the products and different areas of the site.

In building the skeleton I used Wireframes to enable the client to feedback on how their site will look and interact ahead of development.

<br />

**Keyword Research**

Ahead of creating the Wireframes, I performed keyword research to understand what topics and categories users are searching for when they come to shop for fresh coffee and coffee related products online. First I brainstormed general coffee topics to ascertain some keywords, and followed this by researching these words using Amazon to understand potential short-tail and long-tail keywords. Using [wordtracker.com](https://www.wordtracker.com/) I evaluated which would be competitive, relevant, authoritative and trustworthy. 

The output highlighted below helped with the naming conventions and descriptions for the products and page URLs to improve site searchability.

**_Short-tail Keywords_**
* Coffee beans
* Fresh coffee
* Ground coffee
* Coffee machines
* Coffee mug
* Coffee cup
* Coffee grinder

**_Long-tail Keywords_**
* Fresh coffee beans 1kg
* Fresh coffee beans
* Fresh coffee ground
* Fresh coffee maker
* Fresh coffee machine
* Coffee clothing for men
* Coffee lover clothing
* Coffee barista apron
* Café aprons for women coffee bean design
* Waist apron coffee shop
* Cafetiere 8 cup
* Cafetiere 2 cup
* Cafetiere coffee ground
* Fresh coffee beans near me
* How to make fresh coffee
* Buy coffee beans online
* Locally roasted coffee near me

<br />

#### Wireframes

As part of this phase wireframes for desktop and mobile devices have been produced using Balsamiq (see images below - the wireframe files are located with the project [GitHub Repo](https://github.com/RickofManc/the-coffee-collective)). I focused on mocking up the main layouts; the homepage, a page with multiple products and a detailed view of a product.

The website is responsive through differing screen widths being designed for mobile first to a max-width of 767px. Tablets are responsive from 768px through to 1023px, laptops from 1023-1440px, and desktops from 1440px upward.


<details>
    <summary><b>Homepage Wireframe</b></summary>
    <p align="center">
        <img src="readme-images/the_coffee_collective_homepage_wireframe.png" alt="Homepage wireframe for desktop and mobile devices" />
    </p>
</details><br />

<details>
    <summary><b>Products Page Wireframe</b></summary>
    <p align="center">
        <img src="readme-images/the_coffee_collective_all_products_page_wireframe.png" alt="Products page wireframe for desktop and mobile devices" />
    </p>
</details><br />

<details>
    <summary><b>Product in Detail Page Wireframe</b></summary>
    <p align="center">
        <img src="readme-images/the_coffee_collective_product_in_detail_page_wireframe.png" alt="Product in detail page wireframe for desktop and mobile devices" />
    </p>
</details><br />

<br />

### Surface

In consideration that accessibility is a key design criteria, the visual language offers contrast using a simple colour palette, readable font and clear layout. Throughout the website this language has been applied consistently to promote intuitive behaviour with the most important links and information easily recognised. The differing aspects of the Surface are described below.


#### Colour

This palette has been carefully selected to bring high contrasting colours to improve accessibility to visually impaired users. As the primary aim of the site is to inform and in turn promote, Black text on a White background is adopted throughout. Purple has been chosen as conventionally this represents luxury and glamour within e-commerce. As the products being sold are aimed at users who can afford fresh coffee at home, or potentially as a gift, Purple should help to being a special feel to their experience.

Purple has been offset with some softer Grey tones to ensure where necessary information within Purple sections stands out and entices users.

<p align="center">
    <img src="readme-images/the_coffee_collective_colour_palette.png" alt="The Coffee Collective Colour Palette"/>
</p>

<br />

The mock-up's enabled me to work through differing layout styles with this colour palette in mind, whilst using [Contrast Checker](https://coolors.co/contrast-checker) to test whether the combinations of colours would be accessible for visual impaired users. The main Purple tone was evaluated as 'Super' whilst the slightly lighter shade will be used for larger text areas as guided.

<details>
    <summary><b>Colour Palette Contrast Checker</b></summary>
    <p align="center">
        <img src="readme-images/the_coffee_collective_contrast_checker.png" alt="Results of checking the colour palette for good contrast to support visually impaired users"/>
    </p>
</details>
<br />


#### Logo




#### Fonts

Google Fonts has been used to provide free fonts for commercial use. The fonts selected have been chosen for differing reasons whilst still complementing each other. 
Firstly, a strong bold font has been selected in 'Bebas Neue' for titles and subtitles to be impactful for a few words. Whereas 'Open Sans' will be used for body text at a conventional 16px as by design the font is clear and accessible for paragraphs as well as being legible for numbers and symbols.


<p align="center">
    <img src="readme-images/the_coffee_collective_fonts.png" alt="Image showing the two font choices Bebas Neue and Open Sans"/>
</p>

<br />

***

<br />

## Data Model

As part of the project planning phase a high-level design of the site [structure](#Structure) has been created to understand the main entities, and the relationship between these entities set within a Hierarchical structure.
This led to understanding the next level down through mapping out the tables, columns and attributes required for the database. The initial draft in Excel has been mapped into a data schema below using [draw.io](https://www.draw.io/index.html) to help understand how the entities and data will relate across the site.

In consideration of the a requirement for the data to be searchable, and in time understand patterns and trends in user behaviour, an Object-Relational Database using MVT architecture has been selected. I've opted for a PostgreSQL DBMS (Database Management System) as it can support the aforementioned requirements, PostgreSQL can also support multiple programming languages and libraries that which will be used to build the application.

The diagram below shows the entity relationships between categories, products, product reviews, users, and an order. The Product Model is used by the Review Model to ensure the right product is being reviewed. The diagram also highlights that one product can have many reviews. 

The key component in this relationship is the user. I have used the default Django User Model with customisations for simplicity. Both the user and product models are used by Order and Order Line Item models (as users have an option to checkout as a user or as guest).

With this architecture a user can add many products to one order, and leave many product reviews. 

There are currently seven categories created within Category table. These are used to group the products and can be accessed from the navigation menu. They can managed through the Django admin panel, along with user data, products, reviews and orders. 

<br />

The diagram highlights the following relationships:
* One product can have many reviews
* One product can have one category
* One category can have many products
* One order can have many products
* One user can have one order
* One user can add a review to many products
* One user can add many reviews to one product


The Contact Model (within the Company App) does not have a relationship with the other apps, however I have included for awareness towards future development.

 
<p align="center">
    <img src="readme-images/the_coffee_collective_erd.png" alt="Entity relationship diagram for this website"/>
</p>

<br />


### Data Security

Specific steps have been taken to ensure the security of users data and the websites integrity. These are as follows;
* The use of an env.py file to store key variables for accessing secure environments i.e. Postgres Database.
* A gitignore file has been incorporated to ensure the env.py file is never committed to production. Therefore retaining the security of these key variables.
* Additionally, these variables are stored within the Config Variables in Heroku to ensure GitPod and Heroku can synchronise securely.
* Cross Site Request Forgery (CSRF) tokens have been applied to all HTML Forms. Their application provides protection from malicious attacks where users maybe performing certain actions or sending data when logged-in.
* Django's inbuilt User Authentication has been applied to several key areas to ensure only authenticated users can add reviews. A further layer of security has been applied to ensure the ability to manage products (Create, Update, Delete) in the front end can only be performed by users with 'Admin' status.


### Meta data

Meta data is included within the HTML head element to increase the traffic to the website. Additionally, site pages are titled appropriately as another method of informing users of their location.


***

<br />

## Technologies


### Languages

* HTML5
* CSS3
* Python
* JavaScript


### Frameworks & Libraries

* [Django 3.2](https://docs.djangoproject.com/en/4.0/releases/3.2/) has been adopted as more preferable over the newest beta Django 4 to rapidly and securely develop this application.
* [dj_database_url](https://pypi.org/project/dj-database-url/) library used to allow Database urls to connect to the Postgres database.
* [Psycopg2](https://pypi.org/project/psycopg2/) supports the connection to the Postgres database.
* [Gunicorn](https://gunicorn.org/) was used as the Web Server to run Django on Heroku.
* [Django-allauth](https://django-allauth.readthedocs.io/en/latest/) used for addressing user authentication, registration and account management.
* [Bootstrap4](https://getbootstrap.com/docs/4.6/getting-started/introduction/) was used to build responsive web pages.
* [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) is simplifying rendering on several forms.
* [Font Awesome](https://fontawesome.com/icons) source of all site icons.
* [Bulma](https://bulma.io/extensions/) used to support the line height of Font Awesome icons.
* [Pillow](https://pillow.readthedocs.io/en/stable/) to support image processing capabilities.




### Software & Web Applications

* [Balsamiq](https://balsamiq.com/) to build wireframes for the Skelton phase.
* [Figma](https://www.figma.com/) for the high-level site structure.
* [draw.io](https://www.draw.io/index.html) to diagram data schema/model.
* [Photopea](https://www.photopea.com/) to create the clothing product images and brand logo.
* [CovertCSV](https://www.convertcsv.com/csv-to-json.htm) used to convert the csv files with products and categories to json for importing to the repo.
* [GitPod](https://gitpod.io/) used for the IDE and [GitHub](https://github.com/) as a hosting repository.
* [Google Developer Tools](https://developers.google.com/web/tools/chrome-devtools) Used as the primary method for developing the sites responsiveness and identifying bugs.
* [GitHub Kanban board](https://github.com/users/RickofManc/projects/5/views/1) adopted for managing and tracking the user stories using the kanban agile methodology.
* [Heroku](https://dashboard.heroku.com/) to host the live website, including database.
* [Kaffeine](https://kaffeine.herokuapp.com/) used to ping the Heroku every 30 minutes to ensure the website doesn't go to sleep, ensuring fastest load times.
* [AWS](https://aws.amazon.com/) used to store media files.
* [Wave](https://wave.webaim.org/) - Accessibility Testing to ensure content is readable for all users.
* [HTML Validator](https://validator.w3.org/) validates HMTL code.
* [W3 CSS Validator](https://jigsaw.w3.org/css-validator/validator) validates CSS code.
* [PEP8 Validator](http://pep8online.com/)  validates Python code.
* [JSHint](https://jshint.com/) validates JavaScript code.
* [Code Beautify](https://codebeautify.org/) validates the code formatting for browser reading.
* [IE NetREnderer](https://netrenderer.com/index.php) for cross browser testing, specifically Microsoft IE versions 11 and Edge.
* [LambdaTest](https://www.lambdatest.com/) for cross browser testing, specifically macOS Safari and Opera.





















***

<br />

## Credit & Attributes


### Credit

* Mentor Brian Macharia for continuing to guide and feedback throughout the projects lifecycle, especially on how to improve UX and my code.


### Attributes

Support with how to develop ideas into code also came from various online resources, as well as using open source code and free images. All these are documented below.

* In general the coding and testing has relied on the Code Institutes walkthrough project "Boutique Ado", with customisations to bring in information about the business and how to contact TCC. Additionally, users can add product reviews, as well as the products containing some differing attributes from the walkthrough project.
* [W3schools](https://www.w3schools.com/) as a source of 'How to...' information throughout the build, and specifically on adapting the Bootsrap NavBar to have a [burger menu icon](https://www.w3schools.com/howto/howto_css_menu_icon.asp) for mobile devices
* [Django Project Docs](https://docs.djangoproject.com/en/4.0/ref/models/fields/) were referenced many times, especially in how to reference fields correctly across differing python files.
* [Ordinary Coders](https://ordinarycoders.com/blog/article/add-a-custom-favicon-to-your-django-web-app) guided me on how to create and add a customised favicon.
* [Monica Wheeler](https://codepen.io/frogmcw/pen/deqRwa) for the code to build the FAQs feature, Union Roasted Coffee provided inspiration for some of the typical questions users may ask.
* [RocketLawyer](http://rocketlawyer.com/) for free creation of a basic Terms & Conditions document.

#### Images

* Photo of Lorenzo Ferodo by Andrea Piacquadio on [Pexels](https://www.pexels.com/)
* Photo of Luca Ferodo by Apunto Group Agencia on [Pexels](https://www.pexels.com/)
* Photo of Coffee Shop interior by Dmitry Zvolskiy on [Pexels](https://www.pexels.com/)
* Favicon from Vecteezy by [icon0.com](https://www.vecteezy.com/free-png/coffee-bean)
* HTML Background sourced from Pexels by [Engin Akyurt](https://www.pexels.com/photo/photo-of-a-black-mug-on-top-of-brown-coffee-beans-9899791/)
* Image of Barista Aprons from [Zazzle](https://www.zazzle.co.uk/barista+aprons)
* Images of Moka Pots from [Bialetti](https://www.bialetti.com/it_en/)
* Images of Cafetieres from [Olympia](https://www.nisbets.co.uk/olympia-contemporary-cafetiere-black-8-cup/cw951)
* Images and descriptions of Coffee Cups from [Gimoka](https://cafazzini.co.uk/collections/all/italian-coffee-cups)
* Inspiration on coffee sizing and prices from [Cafazzini](https://www.gimokacoffee.com/)
* Adobe Stock was used for clothing images under licence.




