# This line will **fail** because src.models does not exist yet. This is the "RED" phase of TDD.
from datetime import date

from src.models import Transaction


# Defines a function to test the creation of a ledger entry
def test_new_transaction():
    today = date(2026, 1, 28)
    # Transaction class that takes a description, amount, and category.
    transaction = Transaction(
        description="Rent",
        amount=1200.00,
        category="Housing",
        date=today,
        status="Pending",
    )
    assert transaction.date == today
    # Verifies the object shows status
    assert transaction.status == "Pending"
    # Verifies the object stores data correctly.
    assert transaction.description == "Rent"
    # Verifies the numerical value is accurate.
    assert transaction.amount == 1200.00
