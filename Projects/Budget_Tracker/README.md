# 💰 Budget Tracker (Python CLI)

A simple **command-line Budget Tracker built using Python** that helps users monitor their spending against a fixed budget.

This program allows users to enter expenses, keeps track of total spending, and alerts the user if they exceed their budget. It also provides an option to **undo the most recent expense** if the budget limit is crossed.

---

# 🚀 Features

- ✅ Set a total budget
- ✅ Add multiple expenses
- ✅ Track total spending in real-time
- ✅ Receive alerts when the budget is exceeded
- ✅ Option to cancel the most recent expense
- ✅ View the final list of expenses

---

# 🧠 Python Concepts Used

This project demonstrates several beginner Python concepts:

* Variables
* Lists
* Loops (`while`)
* Conditional statements (`if/else`)
* User input handling
* List methods (`append()`, `pop()`)
* Basic arithmetic operations

---

# ⚙️ How the Program Works

1. The user enters a **total budget**.
2. The program continuously asks the user to enter an **expense amount**.
3. Each expense is:

   * converted to a `float`
   * stored inside a list
   * added to the running total.
4. If the **total exceeds the budget**, the program:

   * displays an alert
   * asks if the user wants to **undo the last expense**.
5. The program continues until the user types **`done`**.
6. Finally, the program prints the **complete list of expenses**.

---

# 🖥️ Example Output

```
Enter the budget: 100
The total budget is $100

Enter the amount or 'done'(for exiting) : 30
You have spent 30 out of 100

Enter the amount or 'done'(for exiting) : 80
Alert u have over spent by $10
Would u like to cancel the previous expense (y/n): y
The 80 expense has been cancelled.
The new total expense is 30

Enter the amount or 'done'(for exiting) : done

Final list of expenses: [30.0]
=============Goodbye==========
```

---

# 📂 Project Structure

```
budget-tracker
│
├── main.py
└── README.md
```

---

# 🔧 Possible Improvements

Future enhancements for this project could include:

* Adding **expense categories**
* Showing **remaining budget**
* Saving expenses to a **file or database**
* Creating a **monthly spending summary**
* Adding **error handling for invalid input**

---

# 🎯 Learning Outcome

Through this project, I practiced:

* Writing interactive Python programs
* Working with lists and loops
* Implementing logical conditions
* Handling user input effectively

---

# 📌 Author

Created as part of a **Python learning journey** to practice programming fundamentals and build small practical projects.
