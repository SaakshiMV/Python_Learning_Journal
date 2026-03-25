# Main Program
from tracker import ExpenseTracker

tracker = ExpenseTracker()

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        title = input("Enter expense title: ")
        try:
            amount = float(input("Enter amount: "))
            tracker.add_expense(title, amount)
        except ValueError:
            print("Invalid amount!")

    elif choice == "2":
        tracker.view_expenses()

    elif choice == "3":
        tracker.total_expense()

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid choice!")
