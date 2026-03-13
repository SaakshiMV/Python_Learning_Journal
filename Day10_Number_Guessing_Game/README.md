# 🎮 Day 10 — Mini Project: Number Guessing Game

## Overview

Welcome to **Day 10 of my 45-Day Python Learning Journey**.

To apply everything I learned in the first few days, I built a small interactive project: a **Number Guessing Game**.

The idea is simple — the computer randomly selects a number, and the player must **guess the correct number** within the game loop. After every guess, the program gives feedback to guide the player.

This project helped combine several Python fundamentals into a **single working program**.

---

# 🧠 How the Game Works

The game follows a simple flow:

1. The computer randomly selects a number within a given range.
2. The player is prompted to **enter a guess**.
3. The program checks the guess and gives feedback:

   * 📉 Too low
   * 📈 Too high
4. The player continues guessing until the **correct number is found**.

This creates a simple but engaging **interactive loop between the user and the program**.

---

# ⚙️ Python Concepts Used

This mini project combines multiple concepts learned in the first 9 days:

* Variables for storing game data
* `while` loops to keep the game running
* Conditional statements (`if / elif / else`) for decision making
* User input using `input()`
* Type conversion using `int()`
* Random number generation using Python's `random` module

Building projects like this is important because it shows how **multiple programming concepts work together in real programs**.

---

# 🧩 Example Gameplay

```
Guess the number between 1 and 10

Enter your guess: 4
Too low!

Enter your guess: 8
Too high!

Enter your guess: 7
Correct! You guessed the number.
```

The game continues until the player guesses the **correct number**.

---

# 🧪 Sample Implementation

```python id="g7pdfr"
import random

number = random.randint(1, 10)

guess = None

print("Guess the number between 1 and 10")

while guess != number:
    guess = int(input("Enter your guess: "))

    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print("Correct! You guessed the number.")
```

---

# 📌 What I Learned

Through this mini project, I practiced and reinforced:

* Writing interactive programs
* Using loops to control program flow
* Applying conditional logic to evaluate user input
* Generating random values in Python
* Combining multiple concepts to build a working application

---

# 💭 Reflection

This was my **first small Python project**, and it demonstrated how foundational concepts can be combined to build something interactive.

Projects like this make learning programming much more practical because they move beyond theory and show **how real programs are structured and executed**.

As the journey continues, I plan to build **larger and more complex projects** using the concepts learned each day.
