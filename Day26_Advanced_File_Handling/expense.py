# Expense class
class Expense:
    def __init__(self, title, amount):
        self.title = title
        self.amount = amount

    def to_dict(self):
        return {
            "title": self.title,
            "amount": self.amount
        }
