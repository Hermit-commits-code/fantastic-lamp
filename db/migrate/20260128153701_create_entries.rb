class CreateEntries < ActiveRecord::Migration[8.0]
  def change
    create_table :entries do |t|
      t.references :account, null: false, foreign_key: true
      t.references :ledger_transaction, null: false, foreign_key: {to_table: :transactions}
      t.decimal :amount

      t.timestamps
    end
  end
end
