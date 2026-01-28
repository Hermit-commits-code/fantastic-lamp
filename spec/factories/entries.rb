FactoryBot.define do
  factory :entry do
    account { nil }
    ledger_transaction { nil }
    amount { "9.99" }
  end
end
