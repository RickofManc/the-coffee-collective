# the Coffee Collective

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
* [Credits](#Credit)

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

Following a 'design thinking' approach and using the knowledge and experience from the Nielsen Norman Group, the following key personas have been used to empathize with and understand their needs.

<details><summary><b>User Personas</b></summary>
    <p align="center">
        <img src="" alt="User Personas created from research"/>
    </p>
</details><br />

The output from this phase led to the creation of User Stories complete with Acceptance Criteria and high-level tasks for the Development Phase. The GitHub issues area has been used to store, update and track these User Stories through to completion. 

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
* New product listings, discounts and recommendations visible on the landing page.
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

Key to meeting delivering for the differing user personas is a landing page that can immediately meet their priority requirements whilst not over complicating the UI with too much information, and too many choices. The hierarchal structure will be supported by the Navbar that within a click can navigated users to the main product categories. Similarly the landing page will host a carousel with a hero image enticing users who want to either find sale items, or learn more about the products.

The landing page will also act as the main point of navigation to allow users to learn more about the business, the benefits of coffee and links to useful resources i.e. FAQ's.

Aesthetically the layout and content will be clean and clear to promote the products and different areas of the site.

In building the skeleton I used Wireframes to enable the client to feedback on how their site will look and interact ahead of development.

<br />

#### Keyword Research

Ahead of creating the Wireframes, I performed keyword research to understand what topics and categories users are searching for when they come to shop for fresh coffee and coffee related products online. First I brainstormed general coffee topics to ascertain some keywords, and followed this by researching these words using Amazon to understand potential short-tail and long-tail keywords. Using [wordtracker.com](https://www.wordtracker.com/) I evaluated which would be competitive, relevant, authoritative and trustworthy. 

The output highlighted below helped with the naming conventions and descriptions for the products and page URLs to improve site searchability.

**Short-tail Keywords**
* Coffee beans
* Fresh coffee
* Ground coffee
* Coffee machines
* Coffee mug
* Coffee cup
* Coffee grinder

**Long-tail Keywords**
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

As part of this phase wireframes for desktop and mobile devices have been produced using Balsamiq (see images below - the wireframe files are located with the project [GitHub Repo](https://github.com/RickofManc/the-coffee-collective)). I focused on mocking up the main layouts; the landing page, a page with multiple products and a detailed view of a product.

The website is responsive through differing screen widths being designed for mobile first to a max-width of 767px. Tablets are responsive from 768px through to 1023px, laptops from 1023-1440px, and desktops from 1440px upward.


<details>
    <summary><b>Landing Page Wireframe</b></summary>
    <p align="center">
        <img src="readme-images/the_coffee_collective_landing_page_wireframe.png" alt="Landing page wireframe for desktop and mobile devices" />
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

In consideration that accessibility is a key design criteria, the visual language offers contrast using a simple colour palette, readable font and clear layout. Throughout the website this language has been applied consistently to promote intuitive behaviour with the most important links and information easily recognised.


#### Colour

This palette has been carefully selected to bring high contrasting colours to improve accessibility to visually impaired users. As the primary aim of the site is to inform, Black text on a White background is adopted throughout. The Teal based accents will be used to highlight buttons, points of reference or navigation and other key pieces of user information.


<p align="center">
    <img src="readme-images/the_coffee_collective_colour_palette.png" alt="The Coffee Collective Colour Palette"/>
</p>

<br />

The mock-up's enabled me to work through differing layout styles, whilst using [Contrast Checker](https://coolors.co/contrast-checker) to test whether the combinations of colours would be highly accessible for visual impaired users.

<details>
    <summary><b>Colour Palette Contrast Checker</b></summary>
    <p align="center">
        <img src="readme-images/the_coffee_collective_contrast_checker.png" alt="Results of checking the colour palette for good contrast to support visually impaired users"/>
    </p>
</details>
<br />
