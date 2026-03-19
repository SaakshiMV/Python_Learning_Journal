# 🔒 Day 11 — Tuples in Python

## Overview

Welcome to **Day 11 of my 45-Day Python Learning Journey**.

Today I learned about **tuples**, a data structure used to store **multiple values in a single variable**, similar to lists.

However, tuples come with an important property:

> 👉 **Tuples are immutable — once created, their values cannot be changed.**

This makes tuples especially useful when working with **fixed or constant data**.

---

# 1️⃣ Creating a Tuple

Tuples are created using **parentheses `()`**.

Example:

```python id="1t4z3c"
numbers = (1, 2, 3, 4)
```

Tuples can also store **different data types**:

```python id="1t4z3c"
data = ("xyz", 30, True)
```

This flexibility allows tuples to hold **related pieces of information together**.

---

# 2️⃣ Accessing Tuple Elements

Like lists, tuples use **indexing** to access elements.

Important rule:

* Indexing starts at **0**

Example:

```python id="w7g5nx"
fruits = ("apple", "banana", "mango")

print(fruits[0])
print(fruits[1])
```

Output:

```id="h3k2qp"
apple
banana
```

This allows us to **retrieve specific values** from the tuple.

---

# 3️⃣ Immutability

The key feature of tuples is that they are **immutable**.

This means once a tuple is created, its values **cannot be modified**.

Example:

```python id="p9x6rm"
numbers = (1, 2, 3)

# This will cause an error
numbers[0] = 10
```

Attempting to change a tuple will result in a **TypeError**.

This property makes tuples ideal for storing **constant or protected data**.

---

# 4️⃣ Tuple Length

We can find the number of elements in a tuple using the `len()` function.

Example:

```python id="z8d4lf"
numbers = (1, 2, 3, 4)
print(len(numbers))
```

Output:

```id="k2n8x1"
4
```

This is useful when working with **collections of fixed size**.

---

# 5️⃣ Looping Through Tuples

Tuples can be used with loops to iterate through each element.

Example:

```python id="b6t9vd"
fruits = ("apple", "banana", "mango")

for fruit in fruits:
    print(fruit)
```

Output:

```id="v4y1kc"
apple
banana
mango
```

This allows efficient processing of all elements in the tuple.

---

# 6️⃣ When to Use Tuples

Tuples are best used when:

* Data should **not change**
* Storing **fixed records**
* Protecting data from accidental modification
* Slight performance benefits over lists

---

# 🚀 Why Tuples Matter

Tuples help ensure **data integrity** by preventing accidental changes.

They are commonly used in:

* Database records
* Coordinates (e.g., `(x, y)`)
* Configuration settings
* Returning multiple values from functions

Because of their immutability, tuples make programs **more predictable and reliable**.

---

# 📌 What I Learned Today

Today I learned:

* How to create tuples in Python
* The difference between tuples and lists
* Why immutability is important
* How to access and loop through tuple elements
* When to use tuples in real-world programs

---

# 💭 Reflection

Tuples provide a **safe and structured way to store data that should remain constant**.

Understanding when to use tuples instead of lists helps in writing **more efficient, secure, and reliable programs**.
