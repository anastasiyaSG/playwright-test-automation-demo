"""Resume download checks for the deployed portfolio."""

import pytest
from playwright.async_api import expect

from pages.portfolio_page import PortfolioPage


@pytest.mark.e2e
async def test_resume_download_link_has_pdf_destination(portfolio):
	"""Verify the resume link exposes the expected downloadable PDF."""
	page = PortfolioPage(portfolio)

	await expect(page.resume_download_link).to_be_visible()
	assert (await page.resume_download_link.get_attribute("href")).endswith(
		"anastasiya-georgieva-resume.pdf"
	)
	assert await page.resume_download_link.get_attribute("download") is not None


@pytest.mark.e2e
async def test_resume_download_produces_expected_file(portfolio):
	"""Verify clicking the resume link starts a download with the expected name."""
	page = PortfolioPage(portfolio)

	async with portfolio.expect_download() as download_info:
		await page.resume_download_link.click()

	download = await download_info.value

	assert download.suggested_filename == "anastasiya-georgieva-resume.pdf"
	assert await download.path() is not None
