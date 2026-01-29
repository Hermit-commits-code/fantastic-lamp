# Changelog

## [0.3.0] - 2026-01-28

### Added

- Forecasting method for Account model to project future balances.
- Fixed Transaction initialization to make 'status' optional.

## [0.2.0] - 2026-01-28

### Added

- Transaction model with description, amount, category, date, and status
- Account model with balance rollover logic ($Amount\_owed - Amount\_paid = New\ Owed$).
- Pytest configuration for automated test discovery.

## [0.1.0] - 2026-01-28

- Initialized project structure and environment.
