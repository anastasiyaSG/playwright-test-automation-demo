"""Shared Playwright fixtures for the portfolio tests."""

from collections.abc import AsyncGenerator
from pathlib import Path

import pytest_asyncio
from pytest import FixtureRequest
from playwright.async_api import Browser, BrowserContext, Page, async_playwright

from utils.config import DEFAULT_TIMEOUT_MS, HEADLESS
from utils.helpers import load_test_config


@pytest_asyncio.fixture
async def browser() -> AsyncGenerator[Browser, None]:
    """Start an isolated browser for each test and close it reliably."""
    playwright = await async_playwright().start()
    instance = await playwright.chromium.launch(headless=HEADLESS)
    try:
        yield instance
    finally:
        await instance.close()
        await playwright.stop()


@pytest_asyncio.fixture
async def context(
    browser: Browser, request: FixtureRequest
) -> AsyncGenerator[BrowserContext, None]:
    """Create an isolated browser context for each test."""
    test_context = await browser.new_context()
    test_results = Path("test-results")
    test_results.mkdir(exist_ok=True)
    test_name = request.node.name.replace("/", "_").replace("\\", "_")
    trace_path = test_results / f"{test_name}.zip"
    await test_context.tracing.start(screenshots=True, snapshots=True, sources=True)
    try:
        yield test_context
    finally:
        await test_context.tracing.stop(path=str(trace_path))
        await test_context.close()


@pytest_asyncio.fixture
async def page(
    context: BrowserContext, request: FixtureRequest
) -> AsyncGenerator[Page, None]:
    """Create a page with the configured timeout."""
    test_page = await context.new_page()
    test_page.set_default_timeout(DEFAULT_TIMEOUT_MS)
    test_results = Path("test-results")
    test_results.mkdir(exist_ok=True)
    test_name = request.node.name.replace("/", "_").replace("\\", "_")
    screenshot_path = test_results / f"{test_name}.png"
    try:
        yield test_page
    finally:
        await test_page.screenshot(path=str(screenshot_path), full_page=True)
        await test_page.close()


@pytest_asyncio.fixture(scope="session")
def test_config() -> dict[str, str]:
    """Load the deployed portfolio URL and local overrides."""
    return load_test_config()


@pytest_asyncio.fixture
async def portfolio(page: Page, test_config: dict[str, str]) -> Page:
    """Open the portfolio before each test and return the browser page."""
    await page.goto(test_config["base_url"], wait_until="domcontentloaded", timeout=30000)
    await page.wait_for_load_state("domcontentloaded")
    return page
