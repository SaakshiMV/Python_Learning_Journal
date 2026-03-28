import sys
from tracker import ExpenseTracker

tracker = ExpenseTracker()

def show_help():
    print("""
Usage:
python main.py add <title> <amount> <category>
python main.py view
python main.py total
""")

if len(sys.argv) < 2:
    show_help()
else:
    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) != 5:
            print("Invalid usage!")
            show_help()
        else:
            title = sys.argv[2]
            try:
                amount = float(sys.argv[3])
                category = sys.argv[4]
                tracker.add_expense(title, amount, category)
            except ValueError:
                print("Amount must be a number!")

    elif command == "view":
        tracker.view_expenses()

    elif command == "total":
        tracker.total_expense()

    else:
        print("Unknown command!")
        show_help()
