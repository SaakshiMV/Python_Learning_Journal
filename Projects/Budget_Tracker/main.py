expenses = []
amount = 0
total = 0
budget = float(input("Enter the budget: "))
print(f"The total budget is ${budget}")

while True:
    spent = input("\nEnter the amount or 'done'(for exiting) : ").lower()
    if spent == 'done':
        break
    else:
        amount = float(spent)
        expenses.append(amount)
        total = total + amount

        if total > budget:
            print(f"\nAlert u have over spent by ${total-budget}")
            undo = input("Would u like to cancel the previous expense (y/n): ")
            if(undo == 'y'):
                removed_expense = expenses.pop()
                total = total - removed_expense
                print(f"The {removed_expense} expense has been cancelled.")
                print(f"The new total expense is {total}")
            else:
                print("You chose not to cancel the expense.")
        else:
            print(f"You have spent {total} out of {budget}")

print(f"Final list of expenses: {expenses}")
print("=============Goodbye==========")
