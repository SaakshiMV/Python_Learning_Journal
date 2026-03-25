# Example 1: Method
class Dog:
    def bark(self):
        print("Woof!")

d = Dog()
d.bark()


# Example 2: Encapsulation
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def show_balance(self):
        print(self.__balance)

acc = BankAccount(1000)
acc.deposit(500)
acc.show_balance()


# Example 3: Prevent direct access
# print(acc.__balance)  ❌ will give error
