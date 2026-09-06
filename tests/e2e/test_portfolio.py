"""Small smoke and navigation checks for the deployed portfolio."""

import pytest
import pytest_asyncio
from playwright.async_api import expect

from actions.portfolio_actions import PortfolioActions
from pages.portfolio_page import PortfolioPage


@pytest_asyncio.fixture
async def portfolio(page, test_config):
    """Open the portfolio and return its page object."""
    portfolio_page = PortfolioPage(page, test_config["base_url"])
    await portfolio_page.open()
    return portfolio_page


@pytest.mark.e2e
async def test_homepage_has_clear_qa_positioning(portfolio):
    """The first screen identifies the portfolio owner as a QA Engineer/SDET."""
    await portfolio.expect_loaded()
    await expect(portfolio.page).to_have_title("Anastasiya Georgieva — QA Engineer / SDET")


@pytest.mark.e2e
async def test_case_studies_link_reaches_featured_work(portfolio):
    """The primary hero CTA reaches the featured case-study content."""
    actions = PortfolioActions(portfolio)
    await actions.open_case_studies()
    await expect(portfolio.page).to_have_url("**/#projects")
    await expect(portfolio.black_friday_heading).to_be_visible()


@pytest.mark.e2e
async def test_contact_link_reaches_contact_section(portfolio):
    """The contact CTA reaches the visible contact heading."""
    actions = PortfolioActions(portfolio)
    await actions.open_contact()
    await expect(portfolio.page).to_have_url("**/#contact")
    await expect(portfolio.contact_heading).to_be_visible()
