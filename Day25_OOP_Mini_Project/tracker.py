# Expense Tracker Logic
from expense import Expense

class ExpenseTracker:
    def __init__(self, file_name="data.txt"):
        self.file_name = file_name

    def add_expense(self, title, amount):
        expense = Expense(title, amount)

        try:
            with open(self.file_name, "a") as file:
                file.write(str(expense) + "\n")
            print("Expense added successfully!")
        except Exception as e:
            print("Error saving expense:", e)

    def view_expenses(self):
        try:
            with open(self.file_name, "r") as file:
                print("\nExpenses:")
                for line in file:
                    title, amount = line.strip().split(",")
                    print(f"{title} - ₹{amount}")
        except FileNotFoundError:
            print("No expenses found.")

    def total_expense(self):
        total = 0
        try:
            with open(self.file_name, "r") as file:
                for line in file:
                    _, amount = line.strip().split(",")
                    total += float(amount)
            print(f"\nTotal Expense: ₹{total}")
        except FileNotFoundError:
            print("No data available.")
