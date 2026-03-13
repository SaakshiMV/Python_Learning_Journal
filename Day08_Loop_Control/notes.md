# 🎛️ Day 8 — Loop Control Statements in Python

## Overview

Welcome to **Day 8 of my 45-Day Python Learning Journey**.

Today I learned about **loop control statements**, which allow us to **modify the normal behavior of loops**.

Sometimes we don't want a loop to simply run from start to finish. Instead, we may want to:

* Stop the loop early
* Skip certain iterations
* Leave placeholders while writing code

Python provides three important loop control statements:

* `break`
* `continue`
* `pass`

These statements make loops **more flexible and responsive to conditions inside the loop**.

---

# 1️⃣ The `break` Statement

The `break` statement **immediately terminates a loop**, even if the loop condition is still true.

Example:

```python
for i in range(10):
    if i == 5:
        break
    print(i)
```

Output:

```
0
1
2
3
4
```

### How it works

* The loop starts printing numbers from `0`
* When `i` becomes `5`, the `break` statement runs
* The loop **stops instantly**, and the remaining iterations are skipped

`break` is useful when the program **finds what it was looking for and no longer needs to continue looping**.

---

# 2️⃣ The `continue` Statement

The `continue` statement **skips the current iteration and moves to the next one**.

Example:

```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```

Output:

```
0
1
3
4
```

### How it works

* The loop runs normally
* When `i == 2`, the `continue` statement is triggered
* Python skips the `print()` statement for that iteration
* The loop proceeds to the next value

This is useful when we want to **ignore specific cases while continuing the loop**.

---

# 3️⃣ The `pass` Statement

The `pass` statement does **nothing**. It simply acts as a **placeholder**.

Example:

```python
for i in range(5):
    if i == 2:
        pass
    print(i)
```

Output:

```
0
1
2
3
4
```

### Why `pass` exists

Sometimes when writing code, a block is required syntactically but we **haven’t implemented the logic yet**.

`pass` allows the program to run without errors while leaving a placeholder for future code.

---

# 4️⃣ Practical Use Cases

Loop control statements are frequently used in real-world programming.

Examples include:

* Exiting a **game loop** when a player quits
* Skipping **invalid data entries**
* Breaking a loop when a **target value is found**
* Handling **menu-driven programs**

Example: Searching for a specific number in a list.

```python
numbers = [3, 8, 2, 7, 5]

for num in numbers:
    if num == 7:
        print("Number found")
        break
```

Once the number `7` is found, the loop **stops immediately**, avoiding unnecessary iterations.

---

# 📌 What I Learned Today

Today I learned:

* How the `break` statement stops a loop immediately
* How `continue` skips specific iterations
* How `pass` works as a placeholder
* How loop control statements improve the flexibility of loops

---

# 💭 Reflection

Loop control statements make loops **much more powerful and adaptable**.

Instead of simply running from start to finish, loops can now **react dynamically to conditions inside the loop**, making programs more efficient and intelligent.
