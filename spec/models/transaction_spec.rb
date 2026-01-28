require 'rails_helper'

RSpec.describe Transaction, type: :model do
  let(:asset) { Account.create!(name: 'Bank', account_type: 'asset') }
  let(:expense) { Account.create!(name: 'Groceries', account_type: 'expense') }
  it 'is invalid if entries do not balance to zero' do
    txn = Transaction.new(description: "Unbalanced", date: Date.today)
    txn.entries.build(account: asset, amount: -100.00) # Credit Bank
    txn.entries.build(account: expense, amount: 50.00) # Debit Groceries (Missing 50!)
    expect(txn).not_to be_valid
  end
  it 'is valid when entries balance' do
    txn = Transaction.new(description: "Balanced", date: Date.today)
    txn.entries.build(account: asset, amount: -100.00)
    txn.entries.build(account: expense, amount: 100.00)
    expect(txn).to be_valid
  end
end
