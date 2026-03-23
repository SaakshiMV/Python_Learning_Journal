# 📘 Day 21 — Constructors & Instance Variables

## Overview

Welcome to **Day 21 of my 45-Day Python Learning Journey**.

Today I learned how objects are initialized using **constructors** and how data is stored using **instance variables**.

This makes classes capable of holding real, meaningful data.

---

## 1️⃣ What is a Constructor?

A **constructor** is a special method that runs automatically when an object is created.

In Python, it is written as:

```python
def __init__(self):
    pass
````

---

## 2️⃣ Using `__init__`

```python
class Student:
    def __init__(self, name):
        self.name = name
```

### When an object is created:

```python
s1 = Student("Alice")
```

👉 The `__init__` method runs automatically.

---

## 3️⃣ What is `self`?

`self` refers to the **current object**.

```python
self.name = name
```

This means:

👉 Store `name` inside this specific object.

---

## 4️⃣ Instance Variables

Variables created using `self` are called **instance variables**.

Each object has its own copy of these variables.

### Example:

```python
s1 = Student("Alice")
s2 = Student("Bob")

print(s1.name)  # Alice
print(s2.name)  # Bob
```

---

## 5️⃣ Multiple Instance Variables

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

Now each object stores both `name` and `age`.

---

## 6️⃣ Default Values in Constructor

```python
class Student:
    def __init__(self, name, age=18):
        self.name = name
        self.age = age
```

If `age` is not provided, it defaults to `18`.

---

## 🚀 Why This Matters

Constructors and instance variables allow us to:

* Store object-specific data
* Create flexible and dynamic classes
* Build real-world models in code

---

## 📌 What I Learned Today

Today I learned:

* What constructors are
* How the `__init__` method works
* The role of `self`
* What instance variables are
* How to assign default values

---

## 💭 Reflection

Now classes can actually **hold meaningful data**, not just define structure.

This makes programming more practical and closer to modeling real-world systems.
