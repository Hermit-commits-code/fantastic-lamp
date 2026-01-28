class Account < ApplicationRecord
  validates :name, presence: true
  validates :account_type, presence: true, inclusion:{in: %w[asset liability equity income expense]}
end
