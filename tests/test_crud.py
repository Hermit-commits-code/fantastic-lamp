from src.models import Account, Transaction, db


def test_create_and_read_account(app):
    with app.app_context():
        # Create
        new_acc = Account(name="Savings", balance_owed=0.0)
        db.session.add(new_acc)
        db.session.commit()
        # Read
        fetched_acc = Account.query.filter_by(name="Savings").first()
        assert fetched_acc.id is not None
        assert fetched_acc.name == "Savings"


def test_update_transaction_status(app):
    with app.app_context():
        t = Transaction(
            description="Gas", amount=50.0, category="Transport", status="Pending"
        )
        db.session.add(t)
        db.session.commit()
        # Update
        t.status = "Cleared"
        db.session.commit()
        updated_t = db.session.get(Transaction, t.id)
        assert updated_t.status == "Cleared"


def test_delete_account(app):
    with app.app_context():
        acc = Account(name="Temp", balance_owed=10.0)
        db.session.add(acc)
        db.session.commit()
        # Delete
        db.session.delete(acc)
        db.session.commit()
        deleted_acc = db.session.get(Account, acc.id)
        assert deleted_acc is None
