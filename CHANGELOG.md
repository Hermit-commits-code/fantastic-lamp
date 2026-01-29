# Changelog

## [0.5.2] - 2026-01-28

### Fixed

- Corrected Flask factory invocation syntax in execution command.

## [0.5.0] - 2026-01-28

### Added

- Initial Flask Application factory setup.

- Modernized Transaction model to use UTC timezone-aware dates.

### Changed

- Refactored tests to use Session.get() (SQLAlchemy 2.0 standard).

- Automated database table creation on app startup.

## [0.4.1] - 2026-01-28

### Fixed

- Corrected fixture discovery by adding tests/**init**.py.

- Fixed import errors in test suite regarding app context.

- Successfully integrated SQLAlchemy models with existing rollover and forecasting logic.

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
