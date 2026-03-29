# 🌐 Day 38 — Introduction to Flask (Web Development)

## Overview

Welcome to **Day 38 of my 45-Day Python Learning Journey**.

Today I built my **first web application** using **Flask**.

Flask is a **lightweight Python web framework** that allows developers to quickly build web applications and APIs.

---

## 🚀 What I Built

A simple web application that:

- 🏠 Displays a homepage  
- 🖥️ Runs on a local server  
- 🎨 Renders HTML using Flask  

---

## 🧠 What is Flask?

Flask is a micro web framework that allows you to:

- 🌐 Create web servers  
- 🔗 Handle routes (URLs)  
- 🧾 Render HTML templates  
- 🔌 Build APIs  

---

## ⚙️ Basic Flask Example

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello, World!</h1>"

if __name__ == "__main__":
    app.run(debug=True)
````

---

## 🧠 Core Concepts Learned

### 1️⃣ Setting Up Flask

Install Flask using pip:

```bash
pip install flask
```

---

### 2️⃣ Creating Routes

Routes define what happens when a user visits a specific URL.

```python
@app.route("/")
def home():
    return "Welcome!"
```

---

### 3️⃣ Rendering Templates

```python id="o7y3hk"
from flask import render_template

@app.route("/")
def home():
    return render_template("index.html")
```

---

## ▶️ How to Run the App

```bash
pip install -r requirements.txt
python app.py
```

Open in browser:

```
http://127.0.0.1:5000/
```

---

## 📌 What I Learned

Today I learned:

* How to set up Flask
* How to create routes
* How to render HTML templates
* How frontend and backend connect
* How to run a local web server

---

## 💭 Reflection

This is my first step into **web development with Python**.

Seeing my code run in a browser instead of the terminal was exciting and rewarding.

It opens the door to building **full-stack applications** and real-world web products 🚀
