# 📦 Day 26 — Advanced File Handling & JSON

## Overview

Welcome to **Day 26 of my 45-Day Python Learning Journey**.

Today I upgraded my **Expense Tracker** by switching from plain text files to **JSON (JavaScript Object Notation)** for data storage.

JSON is a widely used format in modern applications for storing and exchanging data.

It is commonly used in:

- APIs  
- Databases  
- Configuration files  

---

## 🤔 Why JSON?

Compared to plain text files, JSON offers several advantages:

- 📊 Structured and organized format  
- 📖 Easy to read and write  
- 🔁 Supports complex data (lists, dictionaries)  
- 🌍 Widely used in real-world applications  

---

## 🚀 Features Added

- 📦 JSON-based data storage  
- 🧾 Structured expense records  
- ⚡ Improved data handling  
- 🛡️ Safer file operations  

---

## 🧾 Example JSON Data

```json
[
  {"title": "Food", "amount": 200},
  {"title": "Travel", "amount": 500}
]
````

---

## 🧠 Working with JSON in Python

### 1️⃣ Writing JSON Data

```python
import json

data = [{"title": "Food", "amount": 200}]

with open("data.json", "w") as file:
    json.dump(data, file)
```

---

### 2️⃣ Reading JSON Data

```python
import json

with open("data.json", "r") as file:
    data = json.load(file)
```

---

### 3️⃣ Handling Missing Files Safely

```python
import json

try:
    with open("data.json", "r") as file:
        data = json.load(file)
except FileNotFoundError:
    data = []
```

---

## 📌 What I Learned

Today I learned:

* How to read data from JSON files
* How to write structured data into JSON
* How to convert Python objects ↔ JSON
* How to safely handle missing or empty files
* Why JSON is preferred in real-world applications

---

## 💭 Reflection

Switching to JSON made my project more structured and scalable.

It feels closer to how real-world applications manage data, especially when working with APIs and databases.

This upgrade improved both the **reliability** and **readability** of my project, making it a strong step toward building production-level applications 🚀
