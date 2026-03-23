# Bank Account System using Constructors
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def display(self):
        print(f"Owner: {self.owner}, Balance: {self.balance}")


accounts = []

while True:
    print("\n1. Create Account")
    print("2. View Accounts")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        try:
            balance = int(input("Enter initial balance: "))
            acc = BankAccount(name, balance)
            accounts.append(acc)
            print("Account created!")
        except ValueError:
            print("Invalid amount!")

    elif choice == "2":
        if not accounts:
            print("No accounts found.")
        else:
            for acc in accounts:
                acc.display()

    elif choice == "3":
        print("Exiting...")
        break

    else:
        print("Invalid choice!")
