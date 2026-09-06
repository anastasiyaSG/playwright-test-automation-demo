"""Semantic locator factories for the portfolio page."""

from playwright.async_api import Page


class PortfolioLocators:
    """Stable, user-facing locators observed on the deployed portfolio."""

    @staticmethod
    def page_heading(page: Page):
        return page.get_by_role("heading", name="QA Engineer / SDET", level=1)

    @staticmethod
    def case_studies_link(page: Page):
        return page.get_by_role("link", name="View case studies")

    @staticmethod
    def contact_link(page: Page):
        return page.get_by_role("link", name="Get in touch")

    @staticmethod
    def black_friday_heading(page: Page):
        return page.get_by_role(
            "heading", name="Black Friday: capacity testing that prevented an incident"
        )

    @staticmethod
    def contact_heading(page: Page):
        return page.get_by_role("heading", name="Let's talk about quality at scale.")
