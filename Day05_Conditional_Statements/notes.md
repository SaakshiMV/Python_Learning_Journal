# 🔀 Day 5 — Conditional Statements in Python

## Overview

Welcome to **Day 5 of my 45-Day Python Learning Journey**.

Today I explored **conditional statements**, which allow programs to **make decisions based on conditions**.

Instead of executing code in a fixed sequence, conditionals let programs **choose different paths depending on the data or user input**.

This concept is fundamental because it introduces **control flow**, allowing programs to behave intelligently.

---

# 1️⃣ The `if` Statement

The `if` statement runs a block of code **only if a specified condition is true**.

Example:

```python
age = 20

if age >= 18:
    print("You are eligible to vote.")
```

How it works:

* Python checks the condition `age >= 18`
* If the condition evaluates to **True**, the indented code block runs
* If it is **False**, the program skips the block

Indentation is important in Python because it defines the **code block belonging to the condition**.

---

# 2️⃣ The `if-else` Statement

The `else` statement provides an **alternative block of code** when the condition is false.

Example:

```python
number = 10

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")
```

Explanation:

* If the number is divisible by 2 → it prints **Even number**
* Otherwise → it prints **Odd number**

This allows programs to **choose between two possible outcomes**.

---

# 3️⃣ The `elif` Statement

When multiple conditions need to be checked, Python provides the **`elif` (else-if) statement**.

Example:

```python
score = 75

if score >= 90:
    print("Grade A")
elif score >= 70:
    print("Grade B")
else:
    print("Grade C")
```

Evaluation flow:

1. Python checks the first condition
2. If false, it checks the `elif`
3. If none match, the `else` block runs

This structure helps build **multi-branch decision logic**.

---

# 4️⃣ Nested Conditions

Conditions can also be placed **inside other conditions**, which is called **nested conditional logic**.

Example:

```python
age = 22
has_id = True

if age >= 18:
    if has_id:
        print("Access granted")
```

In this case:

* The second condition is checked **only if the first condition is true**

Nested conditions allow programs to perform **more detailed decision-making**.

---

# 5️⃣ Logical Operators in Conditions

Logical operators help combine **multiple conditions into a single expression**.

Example:

```python
age = 20
citizen = True

if age >= 18 and citizen:
    print("Eligible to vote")
```

Common logical operators:

| Operator | Meaning                             |
| -------- | ----------------------------------- |
| `and`    | Both conditions must be true        |
| `or`     | At least one condition must be true |
| `not`    | Reverses the condition              |

These operators make it possible to create **complex logical rules in programs**.

---

# 🚀 Why Conditional Statements Matter

Conditional statements allow programs to:

* Make **decisions based on data**
* Respond to **user input**
* Control **program behavior**
* Build **interactive and dynamic applications**

Almost every real-world program uses conditional logic to determine **what should happen next**.

---

# 📌 What I Learned Today

Today I learned:

* How `if` statements evaluate conditions
* How to use `if-else` for two possible outcomes
* How to use `elif` to check multiple conditions
* How nested conditional statements work
* How logical operators combine conditions

---

# 💭 Reflection

Conditional statements introduce the ability for programs to **think and react based on information**.

Instead of following a rigid sequence of instructions, programs can now **adapt their behavior depending on input, data, or specific rules**.

This concept is essential for building **intelligent, interactive, and real-world applications**.
