from src.models import Account


def test_load_forecast():
    # Setup $5000.00 debt, paying $500/month
    acc = Account(name="Car Loan", balance_owed=5000.00)
    # Action: Forecast 3 months ahead
    forecast = acc.forecast_balance(monthly_payment=500.00, months=3)
    # Assert: 5000 - (500 * 3) = 3500
    assert forecast == 3500.00
