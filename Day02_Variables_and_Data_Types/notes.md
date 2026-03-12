# Day 2 — Variables and Data Types in Python

## Overview

Today I learned about **variables and basic data types in Python**.
Variables allow us to store information that a program can use and manipulate.

Understanding variables is essential because **almost every program relies on storing and processing data**.

---

# 1️⃣ Variables in Python

A **variable** is a name that refers to a value stored in memory.

Example:

```python
name = "xyz"
age = 30
```

Here:

* `name` stores a string value
* `age` stores an integer

Python automatically determines the type of variable.

---

# 2️⃣ Variable Naming Rules

Good variable names make code easier to read.

Rules:

* Must start with a letter or `_`
* Cannot start with a number
* Cannot use Python keywords
* Should describe the data stored

Good examples:

```python
user_name
total_score
price
```

Bad examples:

```python
1name
class
$price
```

---

# 3️⃣ Basic Data Types

Python has several built-in data types.

## Integer

Whole numbers.

```python
age = 21
year = 2026
```

---

## Float

Numbers with decimals.

```python
temperature = 36.6
price = 19.99
```

---

## String

Text values enclosed in quotes.

```python
name = "xyz"
message = "Learning Python"
```

---

## Boolean

Represents True or False.

```python
is_student = True
is_logged_in = False
```

---

# 4️⃣ Checking Data Types

Python provides the `type()` function.

Example:

```python
age = 30
print(type(age))
```

Output:

```
<class 'int'>
```

---

# 5️⃣ Multiple Variables

You can assign multiple variables in one line.

```python
x, y, z = 10, 20, 30
```

---

# 6️⃣ Dynamic Typing

Python is **dynamically typed**, meaning the type of a variable can change.

Example:

```python
value = 10
value = "ten"
```

The variable `value` first stores an integer and later a string.

---

# Why This Matters

Variables are used everywhere in programming:

* storing user input
* tracking scores in games
* storing data in applications
* processing calculations

Understanding variables is the **foundation of programming logic**.

---

# What I Learned Today

* How variables store values
* Rules for naming variables
* Common Python data types
* How to check data types using `type()`
* Python’s dynamic typing

---

# Reflection

Today’s concepts introduced the basic building blocks for storing and managing data in Python programs.
