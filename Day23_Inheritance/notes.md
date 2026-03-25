# 🧬 Day 23 — Inheritance in Python

## Overview

Welcome to **Day 23 of my 45-Day Python Learning Journey**.

Today I learned about **Inheritance**, a fundamental concept in Object-Oriented Programming (OOP).

Inheritance allows a class to **reuse properties and methods** of another class, making code more efficient and structured.

---

## 1️⃣ What is Inheritance?

**Inheritance** means creating a new class (child) from an existing class (parent).

The child class automatically gets access to the parent class's attributes and methods.

### Syntax:

```python
class Child(Parent):
    pass
````

---

## 2️⃣ Basic Example

```python
class Animal:
    def speak(self):
        print("Animal makes sound")

class Dog(Animal):
    pass

d = Dog()
d.speak()
```

Here, `Dog` inherits the `speak()` method from `Animal`.

---

## 3️⃣ Adding New Behavior

A child class can also have its own additional methods.

```python
class Dog(Animal):
    def bark(self):
        print("Woof!")
```

Now, `Dog` has both:

* inherited method → `speak()`
* its own method → `bark()`

---

## 4️⃣ Method Overriding

The child class can **modify or override** methods from the parent class.

```python
class Dog(Animal):
    def speak(self):
        print("Dog barks")
```

Now, calling `speak()` will use the **child class version** instead of the parent’s.

---

## 5️⃣ Why Inheritance Matters

Inheritance is powerful for building scalable applications:

* Reduces code duplication
* Promotes code reusability
* Improves code organization
* Helps model real-world relationships
* Widely used in large systems and frameworks

---

## 📌 What I Learned Today

Today I learned:

* How to create child classes using inheritance
* How to reuse methods from a parent class
* How to extend functionality in child classes
* How to override existing methods

---

## 💭 Reflection

Inheritance makes it easier to build complex systems by reusing existing code.

Instead of writing everything from scratch, we can **build on top of existing classes**, making programs more efficient, scalable, and maintainable.

```
```
