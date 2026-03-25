import json
import os
from expense import Expense

class ExpenseTracker:
    def __init__(self, file_name="data.json"):
        self.file_name = file_name

    def load_data(self):
        if not os.path.exists(self.file_name):
            return []

        try:
            with open(self.file_name, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return []

    def save_data(self, data):
        with open(self.file_name, "w") as file:
            json.dump(data, file, indent=4)

    def add_expense(self, title, amount, category):
        data = self.load_data()
        expense = Expense(title, amount, category)
        data.append(expense.to_dict())
        self.save_data(data)
        print("Expense added!")

    def view_expenses(self):
        data = self.load_data()

        if not data:
            print("No expenses found.")
            return

        print("\nExpenses:")
        print("-" * 40)

        for i, exp in enumerate(data):
            print(f"{i}: {exp['title']} | ₹{exp['amount']} | {exp['category']} | {exp['date']}")

    def total_expense(self):
        data = self.load_data()
        total = sum(exp["amount"] for exp in data)
        print(f"\nTotal Expense: ₹{total}")
