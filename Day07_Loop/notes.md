# 🔁 Day 7 — Loops in Python

## Overview

Welcome to **Day 7 of my 45-Day Python Learning Journey**.

Today I learned about **loops**, one of the most powerful concepts in programming. Loops allow a program to **repeat a block of code multiple times**, which is extremely useful when performing repetitive tasks.

Instead of writing the same code again and again, loops make programs **shorter, cleaner, and more efficient**.

Common tasks where loops are useful include:

* Processing collections of data
* Printing patterns or sequences
* Running repeated calculations
* Building interactive or menu-based programs

Python provides two main types of loops:

* `for` loops
* `while` loops

---

# 1️⃣ The `for` Loop

A **`for` loop** is used to iterate over a sequence of values.

Example:

```python
for i in range(5):
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

* `range(5)` generates numbers from **0 to 4**
* The loop variable `i` takes each value in the sequence
* The loop runs once for every value in the range

`for` loops are commonly used when **the number of iterations is known beforehand**.

---

# 2️⃣ The `range()` Function

The `range()` function generates a **sequence of numbers**, which is often used with `for` loops.

Common patterns:

```
range(5)      → 0,1,2,3,4
range(1,6)    → 1,2,3,4,5
range(2,10,2) → 2,4,6,8
```

Example program:

```python
for i in range(1,6):
    print(i)
```

Output:

```
1
2
3
4
5
```

The third parameter in `range(start, stop, step)` controls **how much the number increases each time**.

---

# 3️⃣ The `while` Loop

A **`while` loop** repeats a block of code **as long as a condition remains true**.

Example:

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

Output:

```
1
2
3
4
5
```

### How it works

1. Python checks the condition `count <= 5`
2. If the condition is **True**, the loop runs
3. The variable `count` increases by 1
4. When the condition becomes **False**, the loop stops

`while` loops are useful when the **number of iterations is not known in advance**.

---

# 4️⃣ Difference Between `for` and `while`

| Loop    | Best Used When                    |
| ------- | --------------------------------- |
| `for`   | The number of iterations is known |
| `while` | The loop depends on a condition   |

Example comparison:

```python
# for loop
for i in range(5):
    print(i)

# while loop
i = 0
while i < 5:
    print(i)
    i += 1
```

Both loops produce the **same result**, but they are used in different situations depending on the program logic.

---

# 5️⃣ Common Use Cases of Loops

Loops are widely used in real-world programming tasks such as:

* Iterating through datasets
* Processing files
* Automation scripts
* Game loops
* Menu-driven programs
* Repeated calculations

Without loops, programs would require **a large amount of repetitive code**.

---

# 📌 What I Learned Today

Today I learned:

* How `for` loops iterate through sequences
* How the `range()` function generates numbers
* How `while` loops execute based on conditions
* The difference between `for` and `while` loops
* Practical scenarios where loops are useful

---

# 💭 Reflection

Loops are a fundamental programming concept that make it possible to **automate repetitive tasks and process large amounts of data efficiently**.

Understanding loops is essential for writing scalable programs, and they will play a major role in future topics like **data processing, algorithms, and building interactive applications**.
