# Hermit Ledger

A high-precision accounting ledger application built with Ruby 3.4.1 and Rails 8.0.4.

## Objectives

- Precise transaction tracking and amount calculation.
- Automated monthly rollover logic.
- Loan and payment forecasting.

## Prerequisites

- Ruby 3.4.1

- SQLite 3.x

## Setup Instructions

1. Clone the repository.
2. Run `bundle install` to install dependencies.
3. Run `bin/rails db:prepare` to initialize the database.

## Testing Strategy

This project follows strict Test-Driven Development (TDD) using RSpec.

- **Unit Tests:** Models and core accounting logic (calculations/rollovers) require 100% coverage.

- **System Tests:** Critical user flows (adding transactions, viewing forecasts) are tested via Capybara.

## Core Logic Specifications

- **Double-Entry Principles:** Every transaction must maintain a balanced state across accounts.
- **Rollover:** Monthly transitions will carry over balances and outstanding debts automatically.
