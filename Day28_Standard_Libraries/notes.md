# ⚙️ Day 28 — Python Standard Libraries (Smart Expense Tracker)

## Overview

Welcome to **Day 28 of my 45-Day Python Learning Journey**.

Today I enhanced my **Expense Tracker** by using Python’s **standard libraries** to make it smarter and more practical.

I used:

- `datetime` → for adding timestamps  
- `os` → for better file handling  

These improvements make the project feel closer to a **real-world application**.

---

## 🚀 Features Added

- 🕒 Timestamp for every expense  
- 🏷️ Category support  
- 🧾 Cleaner output formatting  
- 📁 Automatic file handling  

---

## 🧾 Example Data

```json
[
  {
    "title": "Food",
    "amount": 200,
    "category": "Daily",
    "date": "2026-03-19 18:30"
  }
]
````

---

## 🧠 Using Python Standard Libraries

### 1️⃣ Using `datetime` for Timestamps

```python
from datetime import datetime

current_time = datetime.now().strftime("%Y-%m-%d %H:%M")
```

This helps track **when each expense was added**, making the data more meaningful.

---

### 2️⃣ Using `os` for File Handling

```python id="btxk8m"
import os

if not os.path.exists("data.json"):
    with open("data.json", "w") as file:
        file.write("[]")
```

This ensures the file exists before reading or writing, preventing errors.

---

## 📌 What I Learned

Today I learned:

* How to use `datetime` for real-world data tracking
* How to use `os` to safely handle files
* How to improve user experience with better data structure
* How to write cleaner and smarter code
* How small improvements can make a big difference

---

## 💭 Reflection

This version of the Expense Tracker feels much more refined.

By adding timestamps and categories, the data is no longer just numbers — it becomes **meaningful and useful**.

Using Python’s standard libraries made the application more **robust, user-friendly, and closer to a real product** 🚀
