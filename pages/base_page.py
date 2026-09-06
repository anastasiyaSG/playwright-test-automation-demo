"""Shared browser-page behavior."""

from playwright.async_api import Page, expect


class BasePage:
    """Base class for pages that share navigation and readiness helpers."""

    def __init__(self, page: Page, base_url: str) -> None:
        self.page = page
        self.base_url = base_url.rstrip("/")

    async def open(self, path: str = "/") -> None:
        """Navigate to a relative path and wait for the DOM to be ready."""
        await self.page.goto(f"{self.base_url.rstrip('/')}/{path.lstrip('/')}")
        await self.page.wait_for_load_state("domcontentloaded")

    async def expect_url(self, url_fragment: str) -> None:
        """Assert that the current URL contains the expected route fragment."""
        await expect(self.page).to_have_url(f"**{url_fragment}**")
