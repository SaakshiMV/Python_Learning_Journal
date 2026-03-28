# 💻 Day 30 — CLI Expense Tracker

## Overview

Welcome to **Day 30 of my 45-Day Python Learning Journey**.

Today I transformed my Expense Tracker into a **Command Line Interface (CLI) tool**.

Instead of using menu-based input, the application now runs using **terminal commands**, making it faster and more practical.

---

## 🧠 What is CLI?

**CLI (Command Line Interface)** allows users to interact with programs using commands in the terminal.

### Example:

```bash
python main.py add Food 200 Daily
````

This makes applications more powerful and efficient, especially for developers.

---

## 🚀 Features

* ➕ Add expense via command
* 📋 View all expenses
* 💰 Show total expense
* 📦 JSON-based storage

---

## ⚙️ Commands

### 1️⃣ Add Expense

```bash
python main.py add <title> <amount> <category>
```

---

### 2️⃣ View Expenses

```bash id="1i4yvl"
python main.py view
```

---

### 3️⃣ Total Expense

```bash id="6j5h2c"
python main.py total
```

---

## 📌 Example Usage

```bash id="d7o4mf"
python main.py add Food 250 Daily
python main.py view
python main.py total
```

---

## 🧠 Core Concept Used

### Using `sys.argv`

```python id="fxnqz9"
import sys

command = sys.argv[1]
```

This allows the program to read command-line arguments and perform actions accordingly.

---

## 📌 What I Learned

Today I learned:

* How to use `sys.argv` for command-line arguments
* How to build CLI-based tools
* How to improve user interaction via commands
* How real-world tools are structured
* How to make applications faster and more efficient

---

## 💭 Reflection

This version of the Expense Tracker feels like a **real software tool**.

Running commands directly from the terminal makes it more powerful and user-friendly for developers.

It’s a big step toward building **professional-grade applications** 🚀
