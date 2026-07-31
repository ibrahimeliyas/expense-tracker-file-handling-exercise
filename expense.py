class Expense:
    def __init__(self, amount, category, description):
        self.amount = amount
        self.category = category
        self.description = description

    def display(self):
        print(f"Amount: {self.amount}")
        print(f"Category: {self.category}")
        print(f"Description: {self.description}")
        print("------------------------")

    def to_dict(self):
        return {
            "amount": self.amount,
            "category": self.category,
            "description": self.description
        }