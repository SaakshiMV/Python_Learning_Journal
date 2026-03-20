# ⚡ Day 15 — List Comprehensions in Python

## Overview

Welcome to **Day 15 of my 45-Day Python Learning Journey**.

Today I learned about **list comprehensions**, a powerful Python feature that allows us to create lists in a **concise and elegant way**.

Instead of writing multiple lines using loops, list comprehensions let us **build lists in a single line of code**, making programs more **readable and efficient**.

---

# 1️⃣ Basic Syntax

A list comprehension combines **an expression and a loop** into one line.

```python
[expression for item in iterable]
```

Example:

```python id="k3p9xz"
numbers = [1, 2, 3, 4, 5]

squares = [x**2 for x in numbers]
print(squares)
```

Output:

```id="r8m2yt"
[1, 4, 9, 16, 25]
```

This creates a new list where each number is **squared**.

---

# 2️⃣ Using Conditions

We can add conditions using `if` to filter elements.

Example:

```python id="w5z8qn"
numbers = [1, 2, 3, 4, 5, 6]

even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)
```

Output:

```id="v9d1kp"
[2, 4, 6]
```

This filters only the **even numbers** from the list.

---

# 3️⃣ Traditional vs List Comprehension

### Traditional Approach

```python id="j2f7mc"
squares = []

for x in range(5):
    squares.append(x**2)
```

### List Comprehension Approach

```python id="t8n4vd"
squares = [x**2 for x in range(5)]
```

List comprehensions:

* Reduce the number of lines
* Improve readability
* Make code more **Pythonic**

---

# 4️⃣ String Transformation

List comprehensions are also useful for **working with strings**.

Example:

```python id="y6k3rt"
words = ["python", "java", "c++"]

upper_words = [word.upper() for word in words]
print(upper_words)
```

Output:

```id="m4v7zx"
['PYTHON', 'JAVA', 'C++']
```

This transforms each word into **uppercase**.

---

# ⭐ Real-World Example — Data Filtering

List comprehensions are commonly used for **filtering data**.

Example:

```python id="p9w2qb"
marks = [45, 78, 82, 30, 90]

passed = [m for m in marks if m >= 50]
print(passed)
```

Output:

```id="z1x8vc"
[78, 82, 90]
```

This extracts only the **passing marks** from the dataset.

---

# 🚀 Why List Comprehensions Matter

List comprehensions are widely used in:

* Data processing
* Filtering datasets
* Transforming data
* Writing clean and efficient Python code

They are a key part of writing **concise and readable Python programs**.

---

# 📌 What I Learned Today

Today I learned:

* The syntax of list comprehensions
* How to include conditions using `if`
* The difference between traditional loops and comprehensions
* How to transform and filter data efficiently

---

# 💭 Reflection

List comprehensions make Python code **shorter, cleaner, and more expressive**.

They reflect one of Python’s core philosophies:

> *Write code that is simple, readable, and elegant.*

Mastering list comprehensions is an important step toward writing **professional and efficient Python code**.
