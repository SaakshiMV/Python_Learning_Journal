# 📝 Day 40 — Flask Forms & User Input

## Overview

Welcome to **Day 40 of my 45-Day Python Learning Journey**.

Today I made my Flask application **interactive** by handling **user input through forms**.

This is a major step toward building real web applications where users can **send and receive data**.

---

## 🚀 What I Built

A web application where:

- 👤 User enters their name  
- 📤 Form sends data to the backend  
- ⚙️ Backend processes the input  
- 📄 Result is displayed on a new page  

---

## 🧠 Key Concepts

- 📝 HTML Forms  
- 🔄 GET vs POST methods  
- 📥 Request handling in Flask  
- 🔁 Passing user data to templates  

---

## ⚙️ Handling Forms in Flask

### 1️⃣ HTML Form

```html
<form method="POST">
    <input type="text" name="username" placeholder="Enter your name">
    <button type="submit">Submit</button>
</form>
````

---

### 2️⃣ Flask Backend

```python id="y7l3kp"
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form["username"]
        return render_template("result.html", name=name)
    return render_template("index.html")
```

---

## 🔄 GET vs POST

* **GET** → Used to retrieve data (data visible in URL)
* **POST** → Used to send data securely to the server

---

## ▶️ How to Run the App

```bash id="9h2kxm"
pip install -r requirements.txt
python app.py
```

Open in browser:

```id="xk7n2q"
http://127.0.0.1:5000/
```

---

## 📌 What I Learned

Today I learned:

* How to collect user input using HTML forms
* How Flask processes form data using `request`
* Difference between GET and POST methods
* How to pass user input to templates
* How to display dynamic results

---

## 💭 Reflection

This made my application truly interactive.

Instead of just displaying content, it can now **accept input and respond dynamically**, just like real-world web apps.

This is a big step toward building **fully functional web applications** 🚀
