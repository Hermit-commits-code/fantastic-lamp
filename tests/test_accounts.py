from datetime import date

from src.models import Account, Transaction


def test_account_rollover():
    # Setup an account with an inital amount owed
    acc = Account(name="Credit Card", balance_owed=1000.00)
    # Create a payment(Amount_paid)
    payment = Transaction("Monthly Payment", 400.00, "Debt", date(2026, 1, 28))
    # Action: Apply the payment and rollover
    acc.apply_transaction(payment)
    acc.rollover_to_next_month()
    # Assert: Amount_owed(1000) - Amount_paid(400) = 600
    assert acc.balance_owed == 600.00
