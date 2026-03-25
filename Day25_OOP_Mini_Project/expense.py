# Expense class
class Expense:
    def __init__(self, title, amount):
        self.title = title
        self.amount = amount

    def __str__(self):
        return f"{self.title},{self.amount}"
