import json
from expense import Expense

class ExpenseTracker:
    def __init__(self, file_name="data.json"):
        self.file_name = file_name

    def load_data(self):
        try:
            with open(self.file_name, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_data(self, data):
        with open(self.file_name, "w") as file:
            json.dump(data, file, indent=4)

    def add_expense(self, title, amount):
        data = self.load_data()
        expense = Expense(title, amount)
        data.append(expense.to_dict())
        self.save_data(data)
        print("Expense added!")

    def view_expenses(self):
        data = self.load_data()
        if not data:
            print("No expenses found.")
            return

        print("\nExpenses:")
        for i, exp in enumerate(data):
            print(f"{i}: {exp['title']} - ₹{exp['amount']}")

    def update_expense(self, index, new_title, new_amount):
        data = self.load_data()

        if 0 <= index < len(data):
            data[index]["title"] = new_title
            data[index]["amount"] = new_amount
            self.save_data(data)
            print("Expense updated!")
        else:
            print("Invalid index!")

    def delete_expense(self, index):
        data = self.load_data()

        if 0 <= index < len(data):
            removed = data.pop(index)
            self.save_data(data)
            print(f"Deleted: {removed['title']}")
        else:
            print("Invalid index!")
