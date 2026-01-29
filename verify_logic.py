from datetime import date

from src.models import Account, Transaction


def run_simulation():
    # 1. Initialize Account
    my_loan = Account(name="Personal Loan", balance_owed=1000.00)
    print(f"Starting Balance: {my_loan.balance_owed}")
    # 2. Add Transactions
    p1 = Transaction("Payment 1", 200.00, "Debt", date(2026, 1, 15))
    my_loan.apply_transaction(p1)
    # 3. Perform Rollover
    my_loan.rollover_to_next_month()
    print(f"Balance after rollover: {my_loan.balance_owed}")
    # 4. Forecast
    future = my_loan.forecast_balance(monthly_payment=200.00, months=2)
    print(f"Projected balance in 2 months: {future}")


if __name__ == "__main__":
    run_simulation()
