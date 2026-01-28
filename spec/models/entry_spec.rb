# Explanation: Loads the testing environment and Rails configuration.
require 'rails_helper'
# Explanation: Starts the test suite for the Entry (line-item) model.
RSpec.describe Entry, type: :model do
  # Explanation: Describes the specific behavior we are testing (the automated callback).
  it 'updates the account balance after saving' do
    # Explanation: Creates a starting account with a zero balance.
    account = Account.create!(name: 'Cash', account_type: 'asset', balance: 0)
    # Explanation: Creates the parent transaction container for our entry.
    txn = Transaction.create!(description: 'Initial Deposit', date: Date.today)
    # Explanation: Creates an entry of $500. This is the action that should
    # trigger the balance update.
    Entry.create!(account: account, ledger_transaction: txn, amount: 500.00)
    # Explanation: Refreshes the account data from the database and checks if
    # the balance is now 500.
    expect(account.reload.balance).to eq(500.00)
  end
end