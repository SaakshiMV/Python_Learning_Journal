# Bank System with Inheritance
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance   # protected

    def deposit(self, amount):
        self._balance += amount
        print(f"Deposited {amount}")

    def withdraw(self, amount):
        if amount > self._balance:
            print("Insufficient balance")
        else:
            self._balance -= amount
            print(f"Withdrawn {amount}")

    def show_balance(self):
        print(f"Balance: {self._balance}")


# Savings Account
class SavingsAccount(BankAccount):
    def add_interest(self):
        interest = self._balance * 0.05
        self._balance += interest
        print(f"Interest added: {interest}")


# Current Account
class CurrentAccount(BankAccount):
    def withdraw(self, amount):
        # Allow overdraft up to -500
        if self._balance - amount < -500:
            print("Overdraft limit reached!")
        else:
            self._balance -= amount
            print(f"Withdrawn {amount}")


# Main Program
name = input("Enter name: ")
acc_type = input("Account type (savings/current): ").lower()

balance = float(input("Enter initial balance: "))

if acc_type == "savings":
    account = SavingsAccount(name, balance)
else:
    account = CurrentAccount(name, balance)


while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Balance")
    print("4. Extra Feature")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        amount = float(input("Enter amount: "))
        account.deposit(amount)

    elif choice == "2":
        amount = float(input("Enter amount: "))
        account.withdraw(amount)

    elif choice == "3":
        account.show_balance()

    elif choice == "4":
        if isinstance(account, SavingsAccount):
            account.add_interest()
        else:
            print("No extra feature for this account")

    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid choice!")
