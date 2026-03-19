# 📖 Day 13 — Dictionaries in Python

## Overview

Welcome to **Day 13 of my 45-Day Python Learning Journey**.

Today I explored **dictionaries**, one of the most powerful and widely used data structures in Python.

Dictionaries store data in **key-value pairs**, allowing us to access values using meaningful labels (keys) instead of numeric indexes.

This makes dictionaries ideal for handling **structured and real-world data**.

---

# 1️⃣ Creating a Dictionary

Dictionaries are created using **curly braces `{}`** with key-value pairs.

Example:

```python id="d1k9z4"
student = {
    "name": "xyz",
    "age": 30,
    "course": "Python"
}
```

Here:

* `"name"`, `"age"`, `"course"` are **keys**
* `"xyz"`, `30`, `"Python"` are **values**

---

# 2️⃣ Accessing Values

Values in a dictionary are accessed using their **keys**.

Example:

```python id="k8x2np"
print(student["name"])
print(student["age"])
```

Output:

```id="p4v7yt"
xyz
30
```

This makes data access more **intuitive and readable** compared to index-based structures.

---

# 3️⃣ Adding and Updating Values

Dictionaries are **mutable**, meaning we can add or update values easily.

Example:

```python id="x7r3mc"
student["grade"] = "A"   # Adding a new key-value pair
student["age"] = 22      # Updating an existing value
```

This flexibility allows dictionaries to **grow and change dynamically**.

---

# 4️⃣ Removing Items

We can remove items using the `pop()` method.

Example:

```python id="m2q8ld"
student.pop("course")
```

This removes the key `"course"` and its associated value.

---

# 5️⃣ Looping Through a Dictionary

Dictionaries can be looped through using the `items()` method.

Example:

```python id="z5c1rf"
for key, value in student.items():
    print(key, ":", value)
```

Output:

```id="u8n3xs"
name : xyz
age : 30
grade : A
```

This allows us to **process both keys and values together**.

---

# 6️⃣ Useful Dictionary Methods

Some commonly used methods include:

| Method     | Description             |
| ---------- | ----------------------- |
| `keys()`   | Returns all keys        |
| `values()` | Returns all values      |
| `items()`  | Returns key-value pairs |

Example:

```python id="q9p6bn"
print(student.keys())
print(student.values())
```

---

# ⭐ Real-World Example — Student Record

Dictionaries are perfect for representing structured data like a student record.

Example:

```python id="t4y8jw"
student = {
    "name": "qwe",
    "marks": 85,
    "passed": True
}

print(f"{student['name']} scored {student['marks']}")
```

Output:

```id="n7v2kc"
Rahul scored 85
```

This is similar to how real-world systems store and process data.

---

# 🚀 Why Dictionaries Matter

Dictionaries are extremely important because they allow us to **organize and access data efficiently**.

They are widely used in:

* APIs (JSON data structures)
* Databases
* Configuration files
* Real-world applications

Almost every modern application relies on dictionaries or dictionary-like structures.

---

# 📌 What I Learned Today

Today I learned:

* How to create dictionaries
* How to access values using keys
* How to add, update, and remove items
* How to loop through dictionaries
* Useful dictionary methods like `keys()`, `values()`, and `items()`

---

# 💭 Reflection

Dictionaries provide a powerful way to **store structured data with meaningful relationships between keys and values**.

They make programs more **organized, readable, and closer to real-world data representation**, making them one of the most essential tools in Python.
