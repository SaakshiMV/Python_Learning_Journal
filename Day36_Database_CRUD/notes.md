# 🛠️ Day 36 — Database CRUD (SQLite)

## Overview

Welcome to **Day 36 of my 45-Day Python Learning Journey**.

Today I upgraded my **database-based Expense Tracker** to support full **CRUD operations** using SQLite.

CRUD is a core concept in application development and stands for:

- **Create** → Add expense  
- **Read** → View expenses  
- **Update** → Modify expense  
- **Delete** → Remove expense  

---

## 🚀 Features

- ➕ Add new expenses  
- 📋 View all expenses  
- ✏️ Update existing entries  
- ❌ Delete entries  
- 🗄️ SQLite database storage  

---

## 🧠 SQL Operations Used

### 1️⃣ Create (Insert Data)

```sql
INSERT INTO expenses (title, amount)
VALUES ('Food', 200);
````

---

### 2️⃣ Read (Fetch Data)

```sql id="y84zkl"
SELECT * FROM expenses;
```

---

### 3️⃣ Update (Modify Data)

```sql id="7px2re"
UPDATE expenses
SET title = 'Travel', amount = 500
WHERE id = 1;
```

---

### 4️⃣ Delete (Remove Data)

```sql id="q2h8vn"
DELETE FROM expenses
WHERE id = 1;
```

---

## ⚙️ Using SQLite in Python

```python id="v5s1rq"
import sqlite3

conn = sqlite3.connect("expenses.db")
cursor = conn.cursor()

# Example: Fetch data
cursor.execute("SELECT * FROM expenses")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.commit()
conn.close()
```

---

## 📌 What I Learned

Today I learned:

* How to use SQL `UPDATE` queries
* How to use SQL `DELETE` queries
* How to work with unique IDs in databases
* How to manage records efficiently
* How CRUD operations apply to real-world systems

---

## 💭 Reflection

This version of the project feels like a **complete application**.

Users can now fully control their data — adding, viewing, updating, and deleting records.

It gave me a deeper understanding of how databases power real-world applications and how important CRUD operations are in backend development 🚀
