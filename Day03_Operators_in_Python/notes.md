# ⚙️ Day 3 — Operators in Python

## Overview

Welcome to **Day 3 of my 45-Day Python Learning Journey**.

Today I explored **operators**, which are fundamental tools used to perform operations on variables and values. Operators allow programs to **calculate results, compare values, and make logical decisions**.

Without operators, programs could store data but would not be able to **process or evaluate it**.

---

# 🧮1. Arithmetic Operators

Arithmetic operators perform **mathematical calculations**.

| Operator | Meaning             | Example   | Result |
| -------- | ------------------- | --------- | ------ |
| `+`      | Addition            | `5 + 3`   | `8`    |
| `-`      | Subtraction         | `5 - 3`   | `2`    |
| `*`      | Multiplication      | `5 * 3`   | `15`   |
| `/`      | Division            | `10 / 2`  | `5.0`  |
| `%`      | Modulus (remainder) | `10 % 3`  | `1`    |
| `**`     | Exponent            | `2 ** 3`  | `8`    |
| `//`     | Floor Division      | `10 // 3` | `3`    |

### Example

```python
a = 10
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
```

---

# ⚖️2. Comparison Operators

Comparison operators compare two values and return a **Boolean value (`True` or `False`)**.

| Operator | Meaning                  |
| -------- | ------------------------ |
| `==`     | Equal to                 |
| `!=`     | Not equal to             |
| `>`      | Greater than             |
| `<`      | Less than                |
| `>=`     | Greater than or equal to |
| `<=`     | Less than or equal to    |

### Example

```python
x = 10
y = 5

print("x > y:", x > y)
print("x == y:", x == y)
print("x != y:", x != y)
```

These operators are commonly used in **conditions and decision-making** within programs.

---

# 🧩3. Logical Operators

Logical operators allow us to **combine multiple conditions**.

| Operator | Meaning                             |
| -------- | ----------------------------------- |
| `and`    | Both conditions must be true        |
| `or`     | At least one condition must be true |
| `not`    | Reverses the condition              |

### Example

```python
age = 20
has_id = True

print(age > 18 and has_id)
```

In this case, the result will be **True** because both conditions are satisfied.

---

# = 4. Assignment Operators

Assignment operators are used to **store and update values in variables**.

Basic assignment:

```python
x = 10
```

Compound assignment operators make updates shorter and cleaner.

```python
x = 10

x += 5
x -= 2
x *= 3
x /= 2
```

These operators modify the variable using its **existing value**.

---

# 🔝 5. Operator Precedence

Python follows the **standard mathematical order of operations** when evaluating expressions.

Example:

```python
result = 10 + 5 * 2
print(result)
```

Output:

```
20
```

Multiplication is performed **before addition**, which is why the result is `20` instead of `30`.

---

# Why Operators Matter

Operators allow programs to:

* Perform calculations
* Compare values
* Create logical conditions
* Control how programs behave

Almost every program relies heavily on operators to **process data and make decisions**.

---

# What I Learned Today

Today I learned about:

* Arithmetic operators
* Comparison operators
* Logical operators
* Assignment operators
* Operator precedence

---

# Reflection

Operators transform simple variables into **powerful tools for computation and decision-making**.

Understanding how operators work is essential because they form the **foundation of program logic**, which will be used extensively when working with **conditions, loops, and more complex algorithms** later in this journey.
