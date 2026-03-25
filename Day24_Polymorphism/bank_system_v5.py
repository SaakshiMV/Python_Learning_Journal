# Bank System with Polymorphism
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount
        print(f"Deposited {amount}")

    def withdraw(self, amount):
        raise NotImplementedError("This method should be overridden")

    def show_balance(self):
        print(f"Balance: {self._balance}")


# Savings Account
class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        if amount > self._balance:
            print("Insufficient balance")
        else:
            self._balance -= amount
            print(f"Withdrawn {amount}")

    def extra_feature(self):
        interest = self._balance * 0.05
        self._balance += interest
        print(f"Interest added: {interest}")


# Current Account
class CurrentAccount(BankAccount):
    def withdraw(self, amount):
        if self._balance - amount < -500:
            print("Overdraft limit reached")
        else:
            self._balance -= amount
            print(f"Withdrawn {amount}")

    def extra_feature(self):
        print("No extra feature available")


# Main Program
accounts = []

while True:
    print("\n1. Create Account")
    print("2. Perform Actions")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        acc_type = input("Type (savings/current): ").lower()
        balance = float(input("Enter balance: "))

        if acc_type == "savings":
            acc = SavingsAccount(name, balance)
        else:
            acc = CurrentAccount(name, balance)

        accounts.append(acc)
        print("Account created!")

    elif choice == "2":
        if not accounts:
            print("No accounts available")
            continue

        for i, acc in enumerate(accounts):
            print(f"{i}: {acc.owner}")

        idx = int(input("Select account: "))
        acc = accounts[idx]

        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. Balance")
        print("4. Extra Feature")

        action = input("Choose action: ")

        if action == "1":
            amt = float(input("Amount: "))
            acc.deposit(amt)

        elif action == "2":
            amt = float(input("Amount: "))
            acc.withdraw(amt)

        elif action == "3":
            acc.show_balance()

        elif action == "4":
            acc.extra_feature()   # polymorphism in action

    elif choice == "3":
        print("Exiting...")
        break

    else:
        print("Invalid choice!")
