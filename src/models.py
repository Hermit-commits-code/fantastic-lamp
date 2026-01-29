from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# Purpose: db.Model makes this class a database table.
class Transaction(db.Model):
    # Purpose: Unique ID for every transaction (essential for CRUD).
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(100), nullable=False)
    date = db.Column(db.Date, default=datetime.utcnow)
    status = db.Column(db.String(50), default="Pending")
    account_id = db.Column(db.Integer, db.ForeignKey("account.id"))

    def __repr__(self):
        return f"<Transaction {self.description}: {self.amount}>"


class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    balance_owed = db.Column(db.Float, default=0.0)
    transactions = db.relationship("Transaction", backref="account", lazy=True)

    def apply_transaction(self, transaction):
        self.transactions.append(transaction)

    def rollover_to_next_month(self):
        total_paid = sum(
            t.amount for t in self.transactions if t.status in ["Cleared", "Pending"]
        )
        self.balance_owed -= total_paid

    def forecast_balance(self, monthly_payment, months):
        # Calculates the future balance based on a fixed monthly payment.
        projected_balance = self.balance_owed - (monthly_payment * months)
        # Returns the new balance, ensuring it doesn't drop below 0 (since you can't owe negative money on a loan).
        return max(0, projected_balance)
