# 📦 Day 2 — Variables and Data Types in Python

## Overview

Welcome to **Day 2 of my 45-Day Python Learning Journey**.

Today I learned about **variables and basic data types**, which are the building blocks used to store and manage information inside a program.

Almost every piece of software from simple scripts to complex applications relies on variables to **store data, update values, and perform operations**.

Understanding how variables work is one of the **first major steps toward writing meaningful programs**.

---

# 1️⃣ Variables in Python

A **variable** is a name that refers to a value stored in memory.

Think of a variable as a **labeled container** that holds data which the program can use later.

Example:

```python
name = "xyz"
age = 30
```

Here:

* `name` stores a **string**
* `age` stores an **integer**

One important feature of Python is that **you don’t need to declare the type explicitly**.
Python automatically determines the type based on the assigned value.

---

# 2️⃣ Variable Naming Rules

Choosing clear and meaningful variable names helps make code **more readable and maintainable**.

### Basic Rules

* Must start with a **letter** or `_`
* Cannot start with a **number**
* Cannot use **Python reserved keywords**
* Should clearly describe the stored data

### Good Examples

```python
user_name
total_score
price
```

### Bad Examples

```python
1name
class
$price
```

Good naming practices make code **easier for others (and your future self) to understand**.

---

# 3️⃣ Basic Data Types

Python provides several built-in data types for storing different kinds of values.

---

## 🔢 Integer (`int`)

Integers represent **whole numbers**.

```python
age = 21
year = 2026
```

Examples include counts, IDs, or numeric values without decimals.

---

## 🔢 Float (`float`)

Floats represent **numbers with decimal points**.

```python
temperature = 36.6
price = 19.99
```

These are commonly used for **measurements, percentages, or monetary values**.

---

## 📝 String (`str`)

Strings represent **text data** and are enclosed in quotes.

```python
name = "xyz"
message = "Learning Python"
```

Strings are used for storing **names, messages, and textual information**.

---

## ✔ Boolean (`bool`)

Booleans represent **True or False values**.

```python
is_student = True
is_logged_in = False
```

Booleans are commonly used in **conditions and decision-making logic**.

---

# 4️⃣ Checking Data Types

Python provides the built-in `type()` function to check the data type of a variable.

Example:

```python
age = 30
print(type(age))
```

Output:

```
<class 'int'>
```

This function is very useful for **debugging and understanding how Python interprets values**.

---

# 5️⃣ Multiple Variables

Python allows assigning multiple variables in a single line.

Example:

```python
x, y, z = 10, 20, 30
```

This is a concise way to **initialize several variables at once**.

---

# 6️⃣ Dynamic Typing

Python is a **dynamically typed language**, which means the type of a variable can change during execution.

Example:

```python
value = 10
value = "ten"
```

Here:

* `value` initially stores an **integer**
* Later it stores a **string**

Python automatically adjusts the variable type based on the assigned value.

---

# 🚀 Why This Matters

Variables are used everywhere in programming, including:

* Storing **user input**
* Tracking **scores in games**
* Managing **application data**
* Performing **calculations and analysis**

Understanding variables is essential because they form the **foundation of how programs store and process information**.

---

# 📌 What I Learned Today

Today I learned:

* How variables store values in Python
* Rules for naming variables properly
* The most common Python data types
* How to check variable types using `type()`
* How Python supports **dynamic typing**

---

# 💭 Reflection

Today’s concepts introduced the **core building blocks for managing data in Python**.

By understanding variables and data types, I now have the tools needed to start writing programs that **store information, manipulate values, and make decisions based on data**.

These fundamentals will become even more important as the journey continues into **conditions, loops, and more complex program logic**.
