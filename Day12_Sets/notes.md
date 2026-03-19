# 🔢 Day 12 — Sets in Python

## Overview

Welcome to **Day 12 of my 45-Day Python Learning Journey**.

Today I explored **sets**, a powerful built-in Python data structure used to store **unique elements**.

Unlike lists and tuples, sets have some special properties:

* ❌ No duplicate values allowed
* 🔀 Unordered (no indexing)
* ⚡ Optimized for fast membership checks
* ➗ Support mathematical operations

Sets are especially useful when working with **data that must remain unique**.

---

# 1️⃣ Creating a Set

Sets are created using **curly braces `{}`**.

Example:

```python id="7c9k2d"
numbers = {1, 2, 3, 4}
```

If duplicate values are included, Python automatically removes them:

```python id="k8x1pq"
numbers = {1, 2, 2, 3}
print(numbers)
```

Output:

```id="v3n7az"
{1, 2, 3}
```

This makes sets ideal for handling **duplicate data efficiently**.

---

# 2️⃣ Adding Elements

We can add elements to a set using the `add()` method.

Example:

```python id="m4t9zx"
numbers = {1, 2, 3}
numbers.add(4)

print(numbers)
```

Output:

```id="b6k2yr"
{1, 2, 3, 4}
```

---

# 3️⃣ Removing Elements

Elements can be removed using the `remove()` method.

Example:

```python id="p2w8df"
numbers = {1, 2, 3}
numbers.remove(2)

print(numbers)
```

Output:

```id="r9x3js"
{1, 3}
```

⚠️ Note: If the element does not exist, `remove()` will raise an error.

---

# 4️⃣ Looping Through Sets

Even though sets are unordered, we can still loop through them.

Example:

```python id="z5q7lm"
fruits = {"apple", "banana", "mango"}

for fruit in fruits:
    print(fruit)
```

The output order may vary because sets **do not maintain order**.

---

# 5️⃣ Set Operations

One of the most powerful features of sets is their support for **mathematical operations**.

---

## ➕ Union (Combine Elements)

```python id="d8y4kc"
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)
```

Output:

```id="h2n9vx"
{1, 2, 3, 4, 5}
```

---

## 🔁 Intersection (Common Elements)

```python id="c7p3lt"
print(a & b)
```

Output:

```id="u4k8er"
{3}
```

---

## ➖ Difference (Unique Elements)

```python id="x9m2qb"
print(a - b)
```

Output:

```id="s6d1wp"
{1, 2}
```

---

# ⭐ Real-World Example : Removing Duplicates

A very common use of sets is **removing duplicate values from a list**.

Example:

```python id="f3k8zy"
numbers = [1, 2, 2, 3, 4, 4, 5]

unique_numbers = set(numbers)

print(unique_numbers)
```

Output:

```id="w8v6nt"
{1, 2, 3, 4, 5}
```

This technique is widely used in:

* Data cleaning
* Preprocessing datasets
* Filtering repeated entries

---

# 🚀 Why Sets Matter

Sets are extremely useful when working with **unique and unordered data**.

They are commonly used for:

* Removing duplicates
* Membership testing (`in` keyword)
* Mathematical operations
* Data filtering and validation

Their efficiency makes them important in **real-world data processing tasks**.

---

# 📌 What I Learned Today

Today I learned:

* How to create and use sets
* How duplicates are automatically removed
* How to add and remove elements
* How to loop through sets
* How to perform union, intersection, and difference operations

---

# 💭 Reflection

Sets provide a **clean and efficient way to handle unique data**.

They simplify tasks like removing duplicates and performing comparisons, making them highly useful for **data processing and real-world applications**.
