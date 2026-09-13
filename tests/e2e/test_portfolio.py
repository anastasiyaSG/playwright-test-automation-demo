"""Basic UI checks for the deployed portfolio."""

import pytest
from playwright.async_api import expect

from pages.portfolio_page import PortfolioPage


@pytest.mark.e2e
async def test_homepage_is_visible(portfolio):
    # Arrange
    page = PortfolioPage(portfolio)

    # Act
    heading = page.page_heading

    # Assert
    await expect(heading).to_be_visible()


@pytest.mark.e2e
async def test_certificate_popup_contains_certificate_title(portfolio):
    # Arrange
    page = PortfolioPage(portfolio)

    # Act
    await page.certificate_button.click()

    # Assert
    await expect(page.certificate_dialog_heading).to_be_visible()


@pytest.mark.e2e
async def test_philosophy_popup_contains_outcome(portfolio):
    # Arrange
    page = PortfolioPage(portfolio)

    # Act
    await page.philosophy_button.click()

    # Assert
    await expect(page.philosophy_dialog_heading).to_be_visible()
    await expect(page.philosophy_outcome).to_be_visible()


@pytest.mark.e2e
async def test_experience_popup_contains_current_role(portfolio):
    # Arrange
    page = PortfolioPage(portfolio)

    # Act
    await page.experience_button.click()

    # Assert
    await expect(page.experience_dialog_heading).to_be_visible()
    await expect(page.experience_role).to_be_visible()


@pytest.mark.e2e
async def test_toolset_popup_contains_automation_section(portfolio):
    # Arrange
    page = PortfolioPage(portfolio)

    # Act
    await page.toolset_button.click()

    # Assert
    await expect(page.toolset_dialog_heading).to_be_visible()
    await expect(page.toolset_automation_heading).to_be_visible()


@pytest.mark.e2e
async def test_cv_builder_popup_contains_project_link(portfolio):
    # Arrange
    page = PortfolioPage(portfolio)

    # Act
    await page.cv_project_button.click()

    # Assert
    await expect(page.cv_project_dialog_heading).to_be_visible()
    await expect(page.cv_project_github_link).to_be_visible()


@pytest.mark.e2e
async def test_car_watcher_popup_contains_project_title(portfolio):
    # Arrange
    page = PortfolioPage(portfolio)

    # Act
    await page.car_watcher_project_button.click()

    # Assert
    await expect(page.car_watcher_dialog_heading).to_be_visible()


@pytest.mark.e2e
async def test_case_study_navigation_reaches_projects(portfolio):
    # Arrange
    page = PortfolioPage(portfolio)

    # Act
    await page.case_studies_link.click()

    # Assert
    assert portfolio.url.endswith("#projects")
    await expect(page.case_study_heading).to_be_visible()


@pytest.mark.e2e
async def test_contact_cta_navigates_to_contact(portfolio):
    # Arrange
    page = PortfolioPage(portfolio)

    # Act
    await page.contact_cta.click()

    # Assert
    assert portfolio.url.endswith("#contact")
    await expect(page.contact_heading).to_be_visible()


@pytest.mark.e2e
async def test_contact_links_are_available(portfolio):
    # Arrange
    page = PortfolioPage(portfolio)

    # Act
    contact_links = [page.contact_email, page.contact_linkedin, page.contact_github]

    # Assert
    for contact_link in contact_links:
        await expect(contact_link).to_be_visible()
        assert await contact_link.get_attribute("href")


@pytest.mark.e2e
async def test_profile_photo_is_visible(portfolio):
    # Arrange
    page = PortfolioPage(portfolio)

    # Act
    photo = page.profile_photo

    # Assert
    await expect(photo).to_be_visible()
