# 📂 Day 18 — File Handling in Python

## Overview

Welcome to **Day 18 of my 45-Day Python Learning Journey**.

Today I learned about **file handling**, which allows Python programs to **read from and write to files**.

Until now, the programs I built worked only during execution.
With file handling, programs can now **store data permanently and retrieve it later**, making them far more practical and real-world ready.

---

# 1️⃣ Opening a File

Python uses the `open()` function to work with files.

Example:

```python id="h3k9tz"
file = open("example.txt", "r")
```

### File Modes

| Mode  | Description                |
| ----- | -------------------------- |
| `"r"` | Read (default mode)        |
| `"w"` | Write (overwrites file)    |
| `"a"` | Append (adds data to file) |

Choosing the correct mode is important depending on whether you want to **read, overwrite, or add data**.

---

# 2️⃣ Reading a File

We can read the contents of a file using the `read()` method.

Example:

```python id="k8p2zn"
file = open("example.txt", "r")

content = file.read()
print(content)

file.close()
```

### How it works:

* The file is opened in **read mode**
* The entire content is stored in `content`
* The file is then **closed manually**

---

# 3️⃣ Writing to a File

We can write data into a file using `"w"` mode.

Example:

```python id="p6x4rm"
file = open("example.txt", "w")

file.write("Hello, Python!")

file.close()
```

⚠️ Important:

* If the file already exists, `"w"` will **overwrite its content**

---

# 4️⃣ Appending to a File

To add new data without deleting existing content, we use `"a"` mode.

Example:

```python id="t9m3yc"
file = open("example.txt", "a")

file.write("\nNew line added")

file.close()
```

This adds content **at the end of the file**.

---

# 5️⃣ Using `with` (Best Practice)

The recommended way to work with files is using the `with` statement.

Example:

```python id="v2n7qx"
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
```

### Why use `with`?

* Automatically closes the file
* Prevents memory leaks
* Makes code cleaner and safer

---

# 🚀 Why File Handling Matters

File handling is essential for building **real-world applications**.

It is used in:

* Saving user data
* Creating logs and reports
* Storing application data
* Basic database-like operations
* Configuration files

Without file handling, programs cannot **persist data beyond runtime**.

---

# 📌 What I Learned Today

Today I learned:

* How to open files using `open()`
* Different file modes (`r`, `w`, `a`)
* How to read and write data
* How to append content to files
* Why using `with` is a best practice

---

# 💭 Reflection

File handling takes programming to the next level by enabling **data persistence**.

With this concept, programs are no longer temporary — they can now **store information, retrieve it later, and interact with real-world data**, making them far more powerful and useful.
