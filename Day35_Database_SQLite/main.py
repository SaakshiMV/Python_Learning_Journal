from db import create_table, add_expense, view_expenses

create_table()

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        title = input("Enter title: ")
        try:
            amount = float(input("Enter amount: "))
            add_expense(title, amount)
        except ValueError:
            print("Invalid amount!")

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        print("Exiting...")
        break

    else:
        print("Invalid choice!")
