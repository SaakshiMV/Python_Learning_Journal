# 🧱 Day 20 — Object-Oriented Programming (OOP) Basics

## Overview

Welcome to **Day 20 of my 45-Day Python Learning Journey**.

Today I learned about **Object-Oriented Programming (OOP)** — a programming paradigm that allows us to structure code using **classes and objects**.

Instead of writing code as a sequence of instructions, OOP helps in modeling **real-world entities** and organizing code in a more structured and reusable way.

---

## 1️⃣ What is a Class?

A **class** is a blueprint used to create objects.

It defines the structure and behavior that the objects created from it will have.

### Example:

```python
class Student:
    pass
```
Here, Student is a class with **no attributes or methods** yet.

---

## 2️⃣ What is an Object?

An object is an instance of a class.

It represents a real-world entity created using the class blueprint.

Example:
```python
s1 = Student()
```
Here, s1 is an **object of the Student class**.

---

## 3️⃣ The __init__ Method (Constructor)

The __init__ method is a special method used to initialize object data when an object is created.

Example:
```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```
How it works:
- Automatically called when an object is created
- Used to assign values to instance variables
- self refers to the current object
---

## 4️⃣ Instance Variables

Instance variables are variables that belong to an object.

Each object can have its own unique values.

Example:
```python
s1 = Student("John", 20)
print(s1.name)
```
Here, name and age are **instance variables** specific to s1.

---

## 5️⃣ Methods (Functions Inside a Class)

Methods are functions defined inside a class that describe the behavior of objects.

Example:
```python
class Student:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello, my name is", self.name)
```
Usage:
```
s1 = Student("Alice")
s1.greet()
```
---

## 6️⃣ Creating Multiple Objects

We can create multiple objects from the same class, each having its own data.

Example:
```python
s1 = Student("Alice")
s2 = Student("Bob")
```

Each object is **independent and stores its own values**.

## 🚀 Why OOP Matters

Object-Oriented Programming is essential for building scalable and maintainable applications.

It helps to:
- Organize large programs efficiently
- Promote code reusability
- Model real-world systems effectively
- Improve code readability
- Make applications easier to scale and maintain

## 📌 What I Learned Today

Today I learned:

- What classes and objects are
- How to use the `__init__` constructor
- What instance variables are
- How to define and use methods
- How to create multiple objects from a class
- 
## 💭 Reflection

OOP makes programming feel more like designing real-world systems rather than just writing step-by-step instructions.

It introduces a structured way of thinking that is essential for building complex and scalable applications.

This shift in mindset is a major step toward becoming a better developer.
