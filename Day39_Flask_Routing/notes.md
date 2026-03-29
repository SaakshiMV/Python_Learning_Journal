# 🌍 Day 39 — Flask Routing & Templates

## Overview

Welcome to **Day 39 of my 45-Day Python Learning Journey**.

Today I expanded my Flask application by adding **multiple routes** and **dynamic content**.

This made my app feel more like a **real website** instead of just a single page.

---

## 🚀 What I Built

A multi-page web application with:

- 🏠 Home page  
- ℹ️ About page  
- 🔄 Dynamic data passed from backend to frontend  

---

## 🧠 Key Concepts

- 🔗 Routing (handling multiple URLs)  
- 🎨 Dynamic templates  
- 🔁 Passing data using Flask  

---

## ⚙️ Routing in Flask

Routing connects URLs to Python functions.

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Home Page"

@app.route("/about")
def about():
    return "About Page"
````

---

## 🎨 Rendering Templates

```python id="4dx7mr"
from flask import render_template

@app.route("/")
def home():
    return render_template("index.html")
```

---

## 🔄 Passing Data to Templates

```python id="w6h3zb"
@app.route("/")
def home():
    name = "Saakshi"
    return render_template("index.html", name=name)
```

### In HTML (Jinja2):

```html id="b1pjzs"
<h1>Hello, {{ name }}!</h1>
```

---

## ▶️ How to Run the App

```bash id="0g1p9f"
pip install -r requirements.txt
python app.py
```

Open in browser:

```id="v5q3zn"
http://127.0.0.1:5000/
```

---

## 📌 What I Learned

Today I learned:

* How different URLs map to Python functions
* How to create multiple pages in a Flask app
* How to render different HTML templates
* How to pass variables from backend to frontend
* How dynamic content works in web apps

---

## 💭 Reflection

This upgrade made my application feel like a **real website**.

Adding multiple pages and dynamic content made it more interactive and user-friendly.

It’s a big step toward building **full-fledged web applications** 🚀
