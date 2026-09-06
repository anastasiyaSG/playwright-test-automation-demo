"""Short user flows composed from the portfolio page object."""

from pages.portfolio_page import PortfolioPage


class PortfolioActions:
    """Keep navigation flows readable in the test module."""

    def __init__(self, portfolio_page: PortfolioPage) -> None:
        self.portfolio_page = portfolio_page

    async def open_case_studies(self) -> None:
        """Navigate from the hero to the featured case studies."""
        await self.portfolio_page.open_case_studies()

    async def open_contact(self) -> None:
        """Navigate from the hero to the contact section."""
        await self.portfolio_page.open_contact()