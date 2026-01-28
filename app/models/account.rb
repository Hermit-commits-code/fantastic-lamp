class Account < ApplicationRecord
  has_many :entries, dependent: :destroy
  validates :name, presence: true
  validates :account_type, presence: true, inclusion:{in: %w[asset liability equity income expense]}
  validates :balance, numericality: true
end
