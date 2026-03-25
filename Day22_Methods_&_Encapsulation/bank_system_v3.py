# Bank System with Encapsulation
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance   # private variable

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}")
        else:
            print("Invalid amount")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance")
        elif amount <= 0:
            print("Invalid amount")
        else:
            self.__balance -= amount
            print(f"Withdrawn {amount}")

    def get_balance(self):
        return self.__balance


# Main program
name = input("Enter name: ")

try:
    balance = float(input("Enter initial balance: "))
except ValueError:
    balance = 0

account = BankAccount(name, balance)

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        amount = float(input("Enter amount: "))
        account.deposit(amount)

    elif choice == "2":
        amount = float(input("Enter amount: "))
        account.withdraw(amount)

    elif choice == "3":
        print("Balance:", account.get_balance())

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid choice!")
