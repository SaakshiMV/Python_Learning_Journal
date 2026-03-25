from tracker import ExpenseTracker

tracker = ExpenseTracker()

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Update Expense")
    print("4. Delete Expense")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        title = input("Enter title: ")
        try:
            amount = float(input("Enter amount: "))
            tracker.add_expense(title, amount)
        except ValueError:
            print("Invalid amount!")

    elif choice == "2":
        tracker.view_expenses()

    elif choice == "3":
        tracker.view_expenses()
        try:
            index = int(input("Enter index to update: "))
            title = input("Enter new title: ")
            amount = float(input("Enter new amount: "))
            tracker.update_expense(index, title, amount)
        except ValueError:
            print("Invalid input!")

    elif choice == "4":
        tracker.view_expenses()
        try:
            index = int(input("Enter index to delete: "))
            tracker.delete_expense(index)
        except ValueError:
            print("Invalid input!")

    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid choice!")
