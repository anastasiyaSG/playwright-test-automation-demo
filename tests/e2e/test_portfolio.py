"""Basic UI checks for the deployed portfolio."""

import logging

import pytest
from playwright.async_api import expect

from pages.portfolio_page import PortfolioPage


logger = logging.getLogger(__name__)


@pytest.mark.e2e
async def test_homepage_is_visible(portfolio):
    logger.info("Arrange: create the portfolio page object")
    page = PortfolioPage(portfolio)

    logger.info("Act: locate the homepage heading")
    heading = page.page_heading

    logger.info("Assert: homepage heading is visible")
    await expect(heading).to_be_visible()


@pytest.mark.e2e
async def test_certificate_popup_contains_certificate_title(portfolio):
    logger.info("Arrange: create the portfolio page object")
    page = PortfolioPage(portfolio)

    logger.info("Act: open the certificate dialog")
    await page.certificate_button.click()

    logger.info("Assert: certificate dialog heading is visible")
    await expect(page.certificate_dialog_heading).to_be_visible()


@pytest.mark.e2e
async def test_philosophy_popup_contains_outcome(portfolio):
    logger.info("Arrange: create the portfolio page object")
    page = PortfolioPage(portfolio)

    logger.info("Act: open the philosophy dialog")
    await page.philosophy_button.click()

    logger.info("Assert: philosophy dialog heading and outcome are visible")
    await expect(page.philosophy_dialog_heading).to_be_visible()
    await expect(page.philosophy_outcome).to_be_visible()


@pytest.mark.e2e
async def test_experience_popup_contains_current_role(portfolio):
    logger.info("Arrange: create the portfolio page object")
    page = PortfolioPage(portfolio)

    logger.info("Act: open the experience dialog")
    await page.experience_button.click()

    logger.info("Assert: experience dialog heading and role are visible")
    await expect(page.experience_dialog_heading).to_be_visible()
    await expect(page.experience_role).to_be_visible()


@pytest.mark.e2e
async def test_toolset_popup_contains_automation_section(portfolio):
    logger.info("Arrange: create the portfolio page object")
    page = PortfolioPage(portfolio)

    logger.info("Act: open the toolset dialog")
    await page.toolset_button.click()

    logger.info("Assert: toolset dialog and automation section are visible")
    await expect(page.toolset_dialog_heading).to_be_visible()
    await expect(page.toolset_automation_heading).to_be_visible()


@pytest.mark.e2e
async def test_cv_builder_popup_contains_project_link(portfolio):
    logger.info("Arrange: create the portfolio page object")
    page = PortfolioPage(portfolio)

    logger.info("Act: open the CV builder project dialog")
    await page.cv_project_button.click()

    logger.info("Assert: project dialog heading and GitHub link are visible")
    await expect(page.cv_project_dialog_heading).to_be_visible()
    await expect(page.cv_project_github_link).to_be_visible()


@pytest.mark.e2e
async def test_car_watcher_popup_contains_project_title(portfolio):
    logger.info("Arrange: create the portfolio page object")
    page = PortfolioPage(portfolio)

    logger.info("Act: open the car watcher project dialog")
    await page.car_watcher_project_button.click()

    logger.info("Assert: car watcher dialog heading is visible")
    await expect(page.car_watcher_dialog_heading).to_be_visible()


@pytest.mark.e2e
async def test_case_study_navigation_reaches_projects(portfolio):
    logger.info("Arrange: create the portfolio page object")
    page = PortfolioPage(portfolio)

    logger.info("Act: navigate to case studies")
    await page.case_studies_link.click()

    logger.info("Assert: projects section is selected and visible")
    assert portfolio.url.endswith("#projects")
    await expect(page.case_study_heading).to_be_visible()


@pytest.mark.e2e
async def test_contact_cta_navigates_to_contact(portfolio):
    logger.info("Arrange: create the portfolio page object")
    page = PortfolioPage(portfolio)

    logger.info("Act: navigate to contact")
    await page.contact_cta.click()

    logger.info("Assert: contact section is selected and visible")
    assert portfolio.url.endswith("#contact")
    await expect(page.contact_heading).to_be_visible()


@pytest.mark.e2e
async def test_contact_links_are_available(portfolio):
    logger.info("Arrange: create the portfolio page object")
    page = PortfolioPage(portfolio)

    logger.info("Act: collect contact links")
    contact_links = [page.contact_email, page.contact_linkedin, page.contact_github]

    logger.info("Assert: contact links are visible and have destinations")
    for contact_link in contact_links:
        await expect(contact_link).to_be_visible()
        assert await contact_link.get_attribute("href")


@pytest.mark.e2e
async def test_profile_photo_is_visible(portfolio):
    logger.info("Arrange: create the portfolio page object")
    page = PortfolioPage(portfolio)

    logger.info("Act: locate the profile photo")
    photo = page.profile_photo

    logger.info("Assert: profile photo is visible")
    await expect(photo).to_be_visible()
