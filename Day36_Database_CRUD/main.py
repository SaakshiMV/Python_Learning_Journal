from db import (
    create_table,
    add_expense,
    view_expenses,
    update_expense,
    delete_expense
)

create_table()

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
            add_expense(title, amount)
        except ValueError:
            print("Invalid amount!")

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        view_expenses()
        try:
            expense_id = int(input("Enter ID to update: "))
            title = input("Enter new title: ")
            amount = float(input("Enter new amount: "))
            update_expense(expense_id, title, amount)
        except ValueError:
            print("Invalid input!")

    elif choice == "4":
        view_expenses()
        try:
            expense_id = int(input("Enter ID to delete: "))
            delete_expense(expense_id)
        except ValueError:
            print("Invalid input!")

    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid choice!")
