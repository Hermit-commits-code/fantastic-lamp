# Defines where to download gems from
source "https://rubygems.org"
# Specifies the exact Ruby version to use
ruby "3.3.10"
# The core Rails framework
gem "rails", "~> 7.1.0"
# The database engine for local development
gem "sqlite3", "~> 1.4"
# The web server to handle requests
gem "puma", "~> 6.0"

# Gems only used during coding or testing
group :development, :test do
  # Debugging tool for stepping through code
  gem "debug", platforms: %i[ mri mingw x64_mingw ]
  # Testing framework we will use for TDD
  gem "rspec-rails"
  # Linter to ensure clean, standard code
  gem "rubocop-rails", require: false
  # End of development/test group
end