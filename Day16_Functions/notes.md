# 🧩 Day 16 — Functions in Python

## Overview

Welcome to **Day 16 of my 45-Day Python Learning Journey**.

Today I learned about **functions**, one of the most important concepts in programming.

Functions allow us to **organize code into reusable blocks**, making programs cleaner, more structured, and easier to manage.

Instead of repeating the same code multiple times, we can write it once inside a function and reuse it whenever needed.

---

# 1️⃣ Defining a Function

A function is defined using the `def` keyword.

Example:

```python id="f2k8zp"
def greet():
    print("Hello, welcome!")
```

This defines a function named `greet`, but it will not run until it is called.

---

# 2️⃣ Calling a Function

To execute a function, we **call it by its name**.

```python id="x9v4mt"
greet()
```

Output:

```id="q7w2ns"
Hello, welcome!
```

This allows us to **reuse the same block of code multiple times**.

---

# 3️⃣ Functions with Parameters

Functions can accept input values called **parameters**.

Example:

```python id="m5z8kq"
def greet(name):
    print(f"Hello, {name}!")
```

Calling the function:

```python id="v8n3pd"
greet("xyz")
```

Output:

```id="k1t9xz"
Hello, xyz!
```

Parameters make functions more **flexible and dynamic**.

---

# 4️⃣ Functions with Return Values

Functions can return results using the `return` keyword.

Example:

```python id="z4p6yc"
def add(a, b):
    return a + b

result = add(5, 3)
print(result)
```

Output:

```id="n6q2ra"
8
```

The `return` statement sends the result back to the caller, allowing further use of the value.

---

# 5️⃣ Default Parameters

Functions can have **default values** for parameters.

Example:

```python id="w3r8nk"
def greet(name="Guest"):
    print(f"Hello, {name}")
```

Calling:

```python id="j9k2mv"
greet()
greet("xyz")
```

Output:

```id="t5x7pl"
Hello, Guest
Hello, xyz
```

Default parameters make functions easier to use when **optional values are involved**.

---

# 🚀 Why Functions Matter

Functions are essential for writing **clean and scalable programs**.

They help in:

* Reducing code repetition
* Breaking down complex problems
* Improving readability
* Reusing logic across programs
* Building modular and maintainable systems

Almost every large application is built using **multiple functions working together**.

---

# 📌 What I Learned Today

Today I learned:

* How to define and call functions
* How to use parameters to pass data
* How to return values from functions
* How to use default parameters
* How functions improve program structure

---

# 💭 Reflection

Functions are the foundation of **structured programming**.

They make it possible to build **organized, reusable, and scalable code**, which is essential for developing real-world applications.

Mastering functions is a key step toward writing **efficient and professional Python programs**.
