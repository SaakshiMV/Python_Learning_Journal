# 💸 Day 25 — Expense Tracker (OOP Mini Project)

## Overview

Welcome to **Day 25 of my 45-Day Python Learning Journey**.

Today I built a **mini project — Expense Tracker** using Python and Object-Oriented Programming (OOP).

This project combines multiple concepts like **classes, file handling, and error handling** into a practical, real-world application.

It allows users to:

- Add expenses  
- View all expenses  
- Calculate total spending  
- Store and retrieve data from a file  

---

## 🚀 Features

- 🧱 **Object-Oriented Design**  
- 📁 **File Storage (Persistent Data)**  
- ⚠️ **Error Handling for User Input**  
- 🧩 **Modular Code Structure (Multiple Files)**  

---

## 🗂️ Project Structure

```

expense-tracker/
│
├── expense.py   # Defines the Expense class
├── tracker.py   # Handles expense operations
├── main.py      # User interface / CLI logic
└── data.txt     # Stores expense data

````

---

## 🧠 Core Concepts Used

### 1️⃣ Expense Class

Represents a single expense entry.

```python
class Expense:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount
````

---

### 2️⃣ Tracker Logic

Handles adding, viewing, and calculating expenses.

```python
class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def total_expense(self):
        return sum(exp.amount for exp in self.expenses)
```

---

### 3️⃣ File Handling

Used to store and load expense data.

```python
with open("data.txt", "a") as file:
    file.write(f"{expense.name},{expense.amount}\n")
```

---

## 📌 What I Learned

Today I learned:

* How to apply OOP concepts in a real project
* How to store data using files for persistence
* How to handle invalid user inputs safely
* How to structure a project across multiple files
* How to build a simple CLI-based application

---

## 💭 Reflection

This project helped me connect different Python concepts into one complete application.

Instead of just learning theory, I implemented:

* OOP (classes & objects)
* File handling
* Error handling

It gave me a better understanding of how real-world applications are structured and built.

This is a strong step toward building **larger and more practical software projects** 🚀
