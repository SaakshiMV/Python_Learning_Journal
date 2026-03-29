def display_expenses(expenses):
    if not expenses:
        print("No expenses found.")
        return

    print("\nExpenses:")
    print("-" * 50)

    for exp in expenses:
        print(f"ID: {exp[0]} | {exp[1]} | ₹{exp[2]} | {exp[3]}")
