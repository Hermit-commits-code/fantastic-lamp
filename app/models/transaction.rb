class Transaction < ApplicationRecord
  has_many :entries, foreign_key: :ledger_transaction_id, inverse_of: :ledger_transaction, dependent: :destroy
  accepts_nested_attributes_for :entries
  validate :must_balance
  private
  def must_balance
    total = entries.map(&:amount).compact.sum
    errors.add(:base, "Transaction does not balance") unless total.zero?
  end
end
