# 🗄️ Day 35 — Introduction to Databases (SQLite)

## Overview

Welcome to **Day 35 of my 45-Day Python Learning Journey**.

Today I upgraded my Expense Tracker by replacing JSON storage with a **SQLite database**.

SQLite is a **lightweight, file-based database** that comes built into Python, making it perfect for small to medium applications.

---

## 🤔 Why Databases?

Compared to JSON files, databases offer:

- ⚡ Faster data querying  
- 🧱 Structured storage using tables  
- 📈 Better scalability  
- 🌍 Used in real-world applications  

---

## 🚀 What I Built

- 🗄️ Created a SQLite database  
- 📋 Stored expenses in a table  
- ➕ Inserted data into the database  
- 🔍 Retrieved and displayed stored data  

---

## 🧠 SQL Basics Used

### 1️⃣ Create Table

```sql
CREATE TABLE expenses (
    id INTEGER PRIMARY KEY,
    title TEXT,
    amount REAL
);
````

---

### 2️⃣ Insert Data

```sql
INSERT INTO expenses (title, amount)
VALUES ('Food', 200);
```

---

### 3️⃣ Retrieve Data

```sql
SELECT * FROM expenses;
```

---

## ⚙️ Using `sqlite3` in Python

```python
import sqlite3

conn = sqlite3.connect("expenses.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM expenses")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
```

---

## 🧾 Example Table

```
id    title    amount
1     Food     200
```

---

## 📌 What I Learned

Today I learned:

* Basics of SQL (`CREATE`, `INSERT`, `SELECT`)
* How to use the `sqlite3` module in Python
* How to connect to a database
* How to execute queries and fetch data
* Why databases are preferred in real-world applications

---

## 💭 Reflection

Switching to a database made my project feel much more **professional and scalable**.

Instead of just storing data, I am now managing it in a structured way — just like real applications do.

This is a major step toward building **production-ready systems** 🚀
