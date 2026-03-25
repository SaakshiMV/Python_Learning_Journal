# 🛠️ Day 27 — JSON CRUD Expense Tracker

## Overview

Welcome to **Day 27 of my 45-Day Python Learning Journey**.

Today I upgraded my Expense Tracker into a **full CRUD application** using JSON for data storage.

**CRUD** is a fundamental concept used in almost every real-world application.

It stands for:

- **Create** → Add expense  
- **Read** → View expenses  
- **Update** → Edit expense  
- **Delete** → Remove expense  

---

## 🚀 Features

- ➕ Add new expenses  
- 📋 View all expenses  
- ✏️ Update existing expenses  
- ❌ Delete expenses  
- 📦 JSON-based data storage  

---

## 🧠 Core Functionalities

### 1️⃣ Create (Add Expense)

```python
def add_expense(data, title, amount):
    data.append({"title": title, "amount": amount})
````

---

### 2️⃣ Read (View Expenses)

```python
def view_expenses(data):
    for i, exp in enumerate(data):
        print(i, exp["title"], exp["amount"])
```

---

### 3️⃣ Update (Edit Expense)

```python
def update_expense(data, index, title, amount):
    if 0 <= index < len(data):
        data[index] = {"title": title, "amount": amount}
```

---

### 4️⃣ Delete (Remove Expense)

```python
def delete_expense(data, index):
    if 0 <= index < len(data):
        data.pop(index)
```

---

## 📁 JSON File Handling

```python
import json

def load_data():
    try:
        with open("data.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data(data):
    with open("data.json", "w") as file:
        json.dump(data, file)
```

---

## 📌 What I Learned

Today I learned:

* How to implement full CRUD operations
* How to update JSON data dynamically
* How to safely delete records
* How to manage structured data efficiently
* How real-world applications handle user data

---

## 💭 Reflection

This project feels like a complete application now.

Instead of just storing data, I can fully **create, manage, update, and delete** it — just like real-world systems.

It gave me a strong understanding of how backend systems work with data and how important CRUD operations are in application development 🚀
