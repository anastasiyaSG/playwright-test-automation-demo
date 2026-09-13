"""Make action-layer fixtures available to every test."""

from actions.portfolio_fixtures import browser, context, page, portfolio, test_config

__all__ = ["browser", "context", "page", "portfolio", "test_config"]
