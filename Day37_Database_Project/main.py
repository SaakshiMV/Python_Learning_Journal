from db import (
    create_table,
    add_expense,
    get_all_expenses,
    update_expense,
    delete_expense,
    get_by_category,
    get_total
)

from utils import display_expenses

create_table()

while True:
    print("\n1. Add Expense")
    print("2. View All")
    print("3. Update")
    print("4. Delete")
    print("5. Filter by Category")
    print("6. Total Expense")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        title = input("Title: ")
        category = input("Category: ")
        try:
            amount = float(input("Amount: "))
            add_expense(title, amount, category)
        except ValueError:
            print("Invalid amount!")

    elif choice == "2":
        data = get_all_expenses()
        display_expenses(data)

    elif choice == "3":
        data = get_all_expenses()
        display_expenses(data)

        try:
            eid = int(input("Enter ID: "))
            title = input("New title: ")
            category = input("New category: ")
            amount = float(input("New amount: "))
            update_expense(eid, title, amount, category)
        except ValueError:
            print("Invalid input!")

    elif choice == "4":
        data = get_all_expenses()
        display_expenses(data)

        try:
            eid = int(input("Enter ID: "))
            delete_expense(eid)
        except ValueError:
            print("Invalid input!")

    elif choice == "5":
        category = input("Enter category: ")
        data = get_by_category(category)
        display_expenses(data)

    elif choice == "6":
        print("Total:", get_total())

    elif choice == "7":
        print("Exiting...")
        break

    else:
        print("Invalid choice!")
