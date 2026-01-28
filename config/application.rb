require_relative "boot"

require "rails/all"

# Require the gems listed in Gemfile, including any gems
# you've limited to :test, :development, or :production.
Bundler.require(*Rails.groups)

module HermitLedger
  class Application < Rails::Application
    config.load_defaults 8.0 # Ensure this is 8.0 for 2026 standards

    config.autoload_lib(ignore: %w(assets tasks))

    # Asset Pipeline Shim for No-Sprockets builds
    config.assets = ActiveSupport::OrderedOptions.new
    config.assets.paths = []      # Fixes Importmap error
    config.assets.precompile = [] # Fixes Turbo/Tailwind error
  end
end