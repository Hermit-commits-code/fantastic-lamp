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


class Account:
    def __init__(self, name, balance_owed):
        self.name = name
        self.balance_owed = balance_owed
        self.transactions = []

    def apply_transaction(self, transaction):
        # Adds a transaction to this specific account's history
        self.transactions.append(transaction)

    def rollover_to_next_month(self):
        total_paid = sum(
            t.amount
            for t in self.transactions
            if t.status == "Cleared" or t.status == "Pending"
        )
        self.balance_owed -= total_paid
        self.transactions = []
