-# Ex.07 Restaurant Website
# Date:20/12/2025
# AIM:
To develop a static Restaurant website to display the food items and services provided by them.

# DESIGN STEPS:
## Step 1:
Requirement collection.

## Step 2:
Creating the layout using HTML and CSS.

## Step 3:
Updating the sample content.

## Step 4:
Choose the appropriate style and color scheme.

## Step 5:
Validate the layout in various browsers.

## Step 6:
Validate the HTML code.

## Step 7:
Publish the website in the given URL.

# PROGRAM:
```
index.html
{% load static %}
<!DOCTYPE html>
<html>
<head>
    <title>Delicious Bites</title>
    <link rel="stylesheet" href="{% static 'res_app/style.css' %}">  
</head>
<body>

<header>
  

    <h1>Delicious Bites</h1>
    <p>Fresh • Tasty • Hygienic</p>
</header>

<nav>
    <a href="{% url 'home' %}">Home</a>
    <a href="{% url 'menu' %}">Menu</a>
    <a href="{% url 'about' %}">About</a>
    <a href="{% url 'contact' %}">Contact</a>
</nav>

<div class="container">

    <!-- Intro Section -->
    <div class="card">
        <h2>Experience the Taste of Authentic Food</h2>
        <p>
            Welcome to <strong>Delicious Bites</strong>, where flavor meets comfort.
            We prepare every dish using fresh ingredients and traditional recipes
            to give you an unforgettable dining experience.
        </p>
        <a href="menu.html">
            <button>View Our Menu</button>
        </a>
    </div>

    <!-- Today's Highlights -->
    <div class="card">
    	<h2>Today’s Highlights</h2>
    	<p>• Freshly prepared meals available all day</p>
    	<p>• Special lunch combos from 12:00 PM – 3:00 PM</p>
   	<p>• Evening snacks served from 4:30 PM</p>
    	<p>• Home delivery available</p>
    </div>

    <!-- Services -->
    <div class="card">
   	<h2>Our Services</h2>
    	<p>• Dine-in facility</p>
    	<p>• Takeaway orders</p>
    	<p>• Online food ordering</p>
    	<p>• Catering for small events</p>
    </div>

    <!-- Timings -->
    <div class="card">
        <h2>Opening Hours</h2>
        <p>
            Monday – Sunday <br>
            10:00 AM – 10:30 PM
        </p>
        <p>Chennai, India</p>
    </div>

</div>

<footer>
    <p>Delicious Bites Restaurant</p>
</footer>

</body>
</html>

menu.html
{% load static %}
<!DOCTYPE html>
<html>
<head>
    <title>Menu | Delicious Bites</title>
    <link rel="stylesheet" href="{% static 'res_app/style.css' %}">   
</head>
<body>

<header>
    <h1>Our Menu</h1>
    <p>Delicious food for every mood</p>
</header>

<nav>
   <a href="{% url 'home' %}">Home</a>
   <a href="{% url 'menu' %}">Menu</a>
   <a href="{% url 'about' %}">About</a>
   <a href="{% url 'contact' %}">Contact</a>   
</nav>

<div class="container">

    <!-- Starters -->
    <div class="card">
        <h2>Starters</h2>
        <p>Veg Spring Rolls – ₹120</p>
        <p>Paneer Tikka – ₹180</p>
        <p>Chicken 65 – ₹200</p>
        <p>Gobi Manchurian – ₹150</p>
    </div>

    <!-- Main Course -->
    <div class="card">
        <h2>Main Course</h2>
        <p>Veg Biryani – ₹180</p>
        <p>Chicken Biryani – ₹250</p>
        <p>Mutton Biryani – ₹320</p>
        <p>Paneer Butter Masala – ₹220</p>
        <p>Butter Naan – ₹40</p>
    </div>

    <!-- South Indian -->
    <div class="card">
        <h2>South Indian</h2>
        <p>Masala Dosa – ₹90</p>
        <p>Plain Dosa – ₹70</p>
        <p>Idli (2 pcs) – ₹50</p>
        <p>Vada – ₹50</p>
    </div>

    <!-- Beverages -->
    <div class="card">
        <h2>Beverages</h2>
        <p>Fresh Lime Juice – ₹60</p>
        <p>Cold Coffee – ₹90</p>
        <p>Tea / Coffee – ₹30</p>
        <p>Soft Drinks – ₹40</p>
    </div>

    <!-- Desserts -->
    <div class="card">
        <h2>Desserts</h2>
        <p>Gulab Jamun – ₹70</p>
        <p>Ice Cream (Vanilla/Chocolate) – ₹80</p>
        <p>Brownie with Ice Cream – ₹120</p>
    </div>

</div>

<footer>
    <p>Thank you for dining with us</p>
</footer>

</body>
</html>

about.html
{% load static %}
<!DOCTYPE html>
<html>
<head>
    <title>About Us | Delicious Bites</title>
    <link rel="stylesheet" href="{% static 'res_app/style.css' %}">	    
</head>
<body>

<header>
    <h1>About Delicious Bites</h1>
    <p>Quality food • Clean environment • Friendly service</p>
</header>

<nav>
   <a href="{% url 'home' %}">Home</a>
   <a href="{% url 'menu' %}">Menu</a>
   <a href="{% url 'about' %}">About</a>
   <a href="{% url 'contact' %}">Contact</a>    
</nav>

<div class="container">

    <div class="card">
        <h2>Who We Are</h2>
        <p>
            Delicious Bites is a family-friendly restaurant established in 2020.
            We serve a variety of Indian dishes prepared using fresh ingredients
            and traditional cooking methods. Our focus is on quality, hygiene,
            and customer comfort.
        </p>
    </div>

    <div class="card">
        <h2>What We Offer</h2>
        <p>
            Our restaurant offers a wide range of vegetarian and non-vegetarian
            dishes, including South Indian, North Indian, and popular fast food
            items. We provide dine-in and takeaway services.
        </p>
    </div>

    <div class="card">
        <h2>Our Values</h2>
        <ul>
            <li>Fresh and quality ingredients</li>
            <li>Clean and hygienic preparation</li>
            <li>Friendly and respectful service</li>
            <li>Consistent taste and presentation</li>
        </ul>
    </div>

</div>

<footer>
    <p>Serving delicious food since 2020</p>
</footer>

</body>
</html>

contact.html
{% load static %}
<!DOCTYPE html>
<html>
<head>
    <title>Contact Us | Delicious Bites</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>

<header>
    <h1>Contact Us</h1>
    <p>Get in touch with Delicious Bites</p>
</header>

<nav>
  <a href="{% url 'home' %}">Home</a>
  <a href="{% url 'menu' %}">Menu</a>
  <a href="{% url 'about' %}">About</a>
  <a href="{% url 'contact' %}">Contact</a>   
</nav>

<div class="container">

    <div class="card">
        <h2>Contact Information</h2>
        <p><strong>Address:</strong> Chennai, India</p>
        <p><strong>Phone:</strong> +91 98765 43210</p>
        <p><strong>Email:</strong> deliciousbites@gmail.com</p>
    </div>

    <div class="card">
        <h2>Reach Us</h2>
        <p>You can contact us by phone or email for any enquiries.</p>
        <p>We look forward to serving you.</p>
    </div>

</div>

<footer>
    <p>Delicious Restaurant</p>
</footer>

</body>
</html>

style.css

body {
    margin: 0;
    font-family: Arial, sans-serif;
    background-color: #f5f5f5;
}

header {
    background-image: url("background.jpeg");
    background-size: cover;
    background-position: center;
    height: 200px;

    color: white;
    text-align: center;

    display: flex;
    flex-direction: column;
    justify-content: center;

    text-shadow: 2px 2px 5px black;
}
nav {
    background-color: #222;
    padding: 12px;
    text-align: center;
}

nav a {
    color: white;
    margin: 15px;
    text-decoration: none;
    font-size: 18px;
}

nav a:hover {
    color: #ffcccb;
}

.container {
    padding: 30px;
}

.card {
    background: white;
    padding: 20px;
    margin: 15px 0;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0,0,0,0.1);
}


footer {
    background-color: #222;
    color: white;
    text-align: center;
    padding: 10px;
    margin-top: 30px;
}
ul {
    padding-left: 20px;
}

ul li {
    margin: 8px 0;
    font-size: 16px;
}
.card h2 {
    border-bottom: 2px solid #8B0000;
    padding-bottom: 5px;
}

.card p {
    font-size: 16px;
    margin: 8px 0;
    line-height: 1.6;	
}

.container {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 20px;
}

input, textarea {
    width: 100%;
    padding: 8px;
    margin-top: 5px;
    border-radius: 4px;
    border: 1px solid #ccc;
}

```             
       
# OUTPUT:

![alt text](<Screenshot (64).png>) 
![alt text](<Screenshot (68).png>) 
![alt text](<Screenshot (67).png>) 
![alt text](<Screenshot (66).png>) 
![alt text](<Screenshot (65).png>)

# RESULT:
The program for designing software company website using HTML and CSS is completed successfully.
