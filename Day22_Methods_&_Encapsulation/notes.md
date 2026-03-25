# 🔐 Day 22 — Methods & Encapsulation

## Overview

Welcome to **Day 22 of my 45-Day Python Learning Journey**.

Today I explored two important concepts in Object-Oriented Programming:

- **Methods** — defining behavior inside classes  
- **Encapsulation** — protecting and controlling access to data  

These concepts help make code more **secure, structured, and maintainable**, especially in real-world applications.

---

## 1️⃣ What are Methods?

**Methods** are functions defined inside a class that describe the behavior of objects.

They allow objects to perform actions.

### Example:

```python
class Person:
    def greet(self):
        print("Hello!")
````

Here, `greet()` is a method that belongs to the `Person` class.

---

## 2️⃣ Types of Methods

### Instance Methods

* Use `self` as the first parameter
* Work with data specific to an object
* Can access and modify instance variables

### Example:

```python
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello,", self.name)
```

---

## 3️⃣ What is Encapsulation?

**Encapsulation** is the concept of restricting direct access to certain variables and controlling how they are modified.

Instead of accessing data directly, we interact with it through methods.

---

## 4️⃣ Access Modifiers in Python

Python uses naming conventions to indicate access levels:

* `_variable` → **Protected** (by convention)
* `__variable` → **Private** (stronger restriction using name mangling)

---

## 5️⃣ Example of Encapsulation

```python
class Bank:
    def __init__(self, balance):
        self.__balance = balance   # private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance
```

### Usage:

```python
account = Bank(1000)
account.deposit(500)
print(account.get_balance())
```

⚠️ Direct access like `account.__balance` is not allowed.

---

## 6️⃣ Why Encapsulation Matters

Encapsulation plays a key role in building reliable systems:

* Protects data from accidental changes
* Prevents misuse of sensitive information
* Provides controlled access through methods
* Improves code security and structure
* Widely used in real-world applications (like banking systems)

---

## 📌 What I Learned Today

Today I learned:

* Methods define behavior inside classes
* Instance methods use `self` to access object data
* Encapsulation helps protect data
* Difference between protected and private variables
* How to use methods to safely access and modify data

---

## 💭 Reflection

Encapsulation changes how we think about handling data.

Instead of freely accessing variables, we **control interactions through methods**, making programs safer and more predictable.

This concept is essential for writing **robust and secure applications**, especially as projects grow in complexity.
