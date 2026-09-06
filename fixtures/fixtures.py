"""Async browser and shared data fixtures."""

import pytest_asyncio
from playwright.async_api import Browser, BrowserContext, Page, async_playwright

from utils.config import DEFAULT_TIMEOUT_MS, HEADLESS
from utils.helpers import load_test_config


@pytest_asyncio.fixture(scope="session")
async def browser() -> Browser:
    """Start one headless browser for the test session."""
    async with async_playwright() as playwright:
        instance = await playwright.chromium.launch(headless=HEADLESS)
        yield instance
        await instance.close()


@pytest_asyncio.fixture
async def context(browser: Browser) -> BrowserContext:
    """Create an isolated context for each test."""
    test_context = await browser.new_context()
    yield test_context
    await test_context.close()


@pytest_asyncio.fixture
async def page(context: BrowserContext) -> Page:
    """Create a page with the suite timeout applied."""
    test_page = await context.new_page()
    test_page.set_default_timeout(DEFAULT_TIMEOUT_MS)
    yield test_page
    await test_page.close()


@pytest_asyncio.fixture(scope="session")
def test_config() -> dict[str, str]:
    """Provide the environment-driven portfolio URL."""
    return load_test_config()
