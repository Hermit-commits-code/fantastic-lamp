class Entry < ApplicationRecord
  belongs_to :account
  belongs_to :ledger_transaction, class_name: "Transaction"
  after_save :update_account_balance
  private
  def update_account_balance
    # Explanation: Finds the parent account, sums up all its entries, and saves
    # the new total to the balance column.
    account.update!(balance: account.entries.sum(:amount))
  end
end