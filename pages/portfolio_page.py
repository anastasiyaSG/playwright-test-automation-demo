"""Page object for the deployed portfolio homepage."""

from playwright.async_api import expect

from elements.locators import PortfolioLocators
from pages.base_page import BasePage


class PortfolioPage(BasePage):
    """Expose the small set of portfolio flows used by the demo tests."""

    def __init__(self, page, base_url: str) -> None:
        super().__init__(page, base_url)
        self.page_heading = PortfolioLocators.page_heading(page)
        self.case_studies_link = PortfolioLocators.case_studies_link(page)
        self.contact_link = PortfolioLocators.contact_link(page)
        self.black_friday_heading = PortfolioLocators.black_friday_heading(page)
        self.contact_heading = PortfolioLocators.contact_heading(page)

    async def expect_loaded(self) -> None:
        """Verify the primary portfolio positioning is visible."""
        await expect(self.page_heading).to_be_visible()

    async def open_case_studies(self) -> None:
        """Follow the hero link to the case-study section."""
        await self.case_studies_link.click()

    async def open_contact(self) -> None:
        """Follow the hero link to the contact section."""
        await self.contact_link.click()
