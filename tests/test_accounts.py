from datetime import date

from src.models import Account, Transaction, db


def test_account_rollover(app):
    with app.app_context():

        # Setup an account with an inital amount owed
        acc = Account(name="Credit Card", balance_owed=1000.00)
        db.session.add(acc)
        # Create a payment(Amount_paid)
        payment = Transaction(
            description="Payment",
            amount=400.00,
            category="Debt",
            date=date(2026, 1, 28),
            status="Cleared",
        )
        # Action: Apply the payment and rollover
        acc.apply_transaction(payment)
        acc.rollover_to_next_month()
        # Assert: Amount_owed(1000) - Amount_paid(400) = 600
        assert acc.balance_owed == 600.00
