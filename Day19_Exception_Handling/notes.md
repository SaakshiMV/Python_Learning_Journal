# ⚠️ Day 19 — Exception Handling in Python

## Overview

Welcome to **Day 19 of my 45-Day Python Learning Journey**.

Today I learned about **exception handling**, a crucial concept that allows programs to **handle errors gracefully without crashing**.

In real-world applications, errors are inevitable. Exception handling ensures that programs can **respond to errors intelligently and continue execution when possible**.

---

# 1️⃣ What is an Exception?

An **exception** is an error that occurs during the execution of a program.

Example:

```python id="k2m8zp"
num = int("abc")  # This will cause an error
```

Here, Python raises a **ValueError** because `"abc"` cannot be converted into an integer.

Without exception handling, such errors would **stop the program abruptly**.
---

# 2️⃣ Types of Exceptions
## 🛠️ Common Built-in Exceptions
These are the most frequently encountered errors during standard data processing:

- **`ZeroDivisionError`**  
  Raised when attempting to divide a number by zero.

- **`ValueError`**  
  Occurs when a function receives the correct type but an inappropriate value.  
  Example: `int("abc")`

- **`TypeError`**  
  Raised when an operation is applied to an object of inappropriate type.  
  Example: `len(5)`

- **`IndexError`**  
  Occurs when trying to access an index that is out of range in a list.

- **`KeyError`**  
  Raised when accessing a dictionary key that does not exist.

- **`NameError`**  
  Occurs when a variable or function is used before being defined.

- **`FileNotFoundError`**  
  Raised when trying to open a file that does not exist.

- **`ImportError`**  
  Occurs when an import statement fails to locate a module.

---

## 🏗️ Structural & System Exceptions
These errors are related to code structure or system-level interruptions:

- **`SyntaxError`**  
  Raised when Python code is written incorrectly.  
  Example: missing colon `:`

- **`IndentationError`**  
  Occurs due to improper indentation in code blocks.

- **`KeyboardInterrupt`**  
  Triggered when the user manually stops the program (e.g., `Ctrl + C`).

- **`StopIteration`**  
  Raised by iterators when there are no more items to return.

---

## 📂 The Exception Hierarchy
Python organizes exceptions in a hierarchical structure:

- **`BaseException`**  
  The root of all exceptions.  
  ⚠️ Avoid catching this directly.

- **`Exception`**  
  The base class for most runtime errors.  
  ✅ Recommended for general exception handling.

---

## 👤 User-Defined Exceptions
You can create custom exceptions to handle specific business logic by inhering from the `Exception` class.

### Example:

```python
class InsufficientFundsError(Exception):
    """Raised when a bank withdrawal exceeds the balance."""
    pass
```
---
# 3️⃣ Using `try` and `except`

The `try` and `except` blocks allow us to **catch and handle errors**.

Example:

```python id="x7p4rn"
try:
    num = int(input("Enter a number: "))
except:
    print("Invalid input!")
```

### How it works:

* Code inside `try` is executed
* If an error occurs, Python jumps to `except`
* The program continues instead of crashing

---

# 4️⃣ Handling Specific Exceptions

It is better to handle **specific exceptions** rather than using a general `except`.

Example:

```python id="v9z3kt"
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Please enter a valid number")
```

This improves clarity and ensures that **only expected errors are handled**.

---

# 5️⃣ Using `finally`

The `finally` block runs **no matter what happens**, whether an exception occurs or not.

Example:

```python id="p6x8df"
try:
    file = open("data.txt", "r")
except FileNotFoundError:
    print("File not found")
finally:
    print("Execution complete")
```

This is useful for tasks like:

* Closing files
* Releasing resources
* Cleaning up operations

---

# 6️⃣ Using `else`

The `else` block runs **only if no exception occurs**.

Example:

```python id="n3q7zb"
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Invalid input")
else:
    print("You entered:", num)
```

This helps separate **error-handling logic from successful execution logic**.

---

# 🚀 Why Exception Handling Matters

Exception handling is essential for building **robust and user-friendly programs**.

It helps to:

* Prevent program crashes
* Handle invalid user input
* Manage unexpected situations
* Improve user experience
* Build reliable applications

Without exception handling, even small errors could **break entire programs**.

---

# 📌 What I Learned Today

Today I learned:

* What exceptions are
* How to use `try` and `except`
* How to handle specific exceptions like `ValueError`
* How to use `else` and `finally` blocks
* How exception handling improves program stability

---

# 💭 Reflection

Exception handling makes programs **more stable, reliable, and professional**.

By anticipating possible errors and handling them properly, programs can **continue running smoothly even in unexpected situations**, which is essential for real-world applications.
