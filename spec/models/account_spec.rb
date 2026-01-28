require 'rails_helper'

# Defines the test suite for the Account model.
RSpec.describe Account, type: :model do
  # Groups our validation-specific tests together
  describe 'validations' do
    # Defines the "Happy Path" test case.
    it 'is valid with a name and account_type' do
      # Creates a new in-memory instance of an Account.
      account = Account.new(name: 'Checking', account_type: 'asset', balance: 0)
      # Asserts that the account meets all validation criteria.
      expect(account).to be_valid
    end
    # Defines a failure case to ensure names are mandatory.
    it 'is invalid without a name' do
      # Creates an account with a missing name.
      account = Account.new(name: nil)
      # Asserts that the validation correctly catches the error.
      expect(account).not_to be_valid
    end
  end
end
