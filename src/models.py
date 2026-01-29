# Defines the blueprint for our ledger entries
class Transaction:
    # The constructor method that initializes a new transaction object.
    def __init__(self, description, amount, category, date, status):
        # Assigns the description string to an object.
        self.description = description
        # Assigns numerical amount to the object
        self.amount = amount
        # Assigns the category (e.g. "Savings","Debt") to the object
        self.category = category
        # Stores the transaction date
        self.date = date
        # Stores the status (defaults to "Pending" if not provided)
        self.status = status
