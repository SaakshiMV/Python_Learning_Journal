# 🪜 Day 6 — Nested Conditions in Python

## Overview

Welcome to **Day 6 of my 45-Day Python Learning Journey**.

Today I learned about **nested conditional statements**, a technique used when programs need to make **multiple levels of decisions**.

A nested condition occurs when one `if` statement is placed **inside another conditional block**. This allows programs to check additional conditions **only after an earlier condition has been satisfied**.

Nested conditions are commonly used in real-world programming scenarios where decisions depend on **several rules being evaluated step by step**.

---

# 1️⃣ What Are Nested Conditions?

A **nested condition** occurs when an `if` statement is placed inside another `if` block.

Example:

```python
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Access granted")
```

### How It Works

1. Python first checks the condition `age >= 18`
2. If it is **True**, the program moves inside the first block
3. Then the second condition `has_id` is evaluated
4. If both conditions are satisfied, the message is printed

This structure ensures that **the second condition is evaluated only when the first one passes**.

---

# 2️⃣ Why Nested Conditions Are Useful

Nested conditions are useful when a program needs to **evaluate multiple rules in sequence**.

Common situations where nested logic is used include:

* 🔐 Login or authentication systems
* 🎟 Eligibility verification
* 🚪 Access control mechanisms
* 📋 Menu-driven applications
* 🎮 Game rule checks

These scenarios often require **step-by-step decision-making** rather than a single condition.

---

# 3️⃣ Example — Movie Ticket Eligibility

Consider a situation where movie access depends on **age and parental supervision**.

```python
age = 16
with_parent = True

if age >= 18:
    print("You can watch the movie")
else:
    if with_parent:
        print("You can watch with parental guidance")
    else:
        print("Access denied")
```

### Logic Breakdown

* If the user is **18 or older**, they can watch the movie
* If under 18 but **with a parent**, they are allowed with supervision
* Otherwise, access is denied

This example demonstrates how nested conditions can handle **multiple decision paths**.

---

# 4️⃣ Simplifying Nested Conditions

In some cases, nested conditions can be simplified using **logical operators**.

Example:

```python
age = 20
citizen = True

if age >= 18 and citizen:
    print("Eligible to vote")
```

Here the `and` operator combines two conditions into a **single readable statement**, making the code shorter and easier to maintain.

---

# 5️⃣ Best Practices for Nested Conditions

When writing nested conditions, it's important to keep the code **clear and maintainable**.

Best practices include:

* ✔ Keep the logic **simple and readable**
* ✔ Avoid **deeply nested structures**
* ✔ Use **logical operators** when possible
* ✔ Maintain **consistent indentation**
* ✔ Break complex logic into smaller checks if needed

Clean structure makes programs **easier to debug and understand**.

---

# 📌 What I Learned Today

Today I learned:

* How nested `if` statements work
* When nested conditions are useful
* How to structure multi-level decision logic
* How logical operators can simplify nested checks

---

# 💭 Reflection

Nested conditions allow programs to perform **layered decision-making**, where each step depends on the result of the previous one.

By combining nested logic with logical operators, programs can implement **complex rules while keeping the code organized and readable**.

These concepts are important for building **real-world applications that require multiple validations and checks**.
