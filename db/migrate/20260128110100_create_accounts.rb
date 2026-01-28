# Defines the migration using Rails 8.0 standards.
class CreateAccounts < ActiveRecord::Migration[8.0]
  # The standard method for applying database changes.
  def change
    # Explanation: Instructs SQLite to create our accounts table.
    create_table :accounts do |t|
      # Explanation: Creates a column for the account name (e.g., "Checking").
      t.string :name
      # Explanation: Creates a column for the category (e.g., "asset" or "liability").
      t.string :account_type
      # Explanation: Manually setting precision to 15 (total digits) and scale to
      # 2 (decimals) with a safe default of zero.
      t.decimal :balance, precision: 15, scale: 2, default:0.0
      # Explanation: Adds created_at and updated_at tracking.
      t.timestamps
    end
  end
end
