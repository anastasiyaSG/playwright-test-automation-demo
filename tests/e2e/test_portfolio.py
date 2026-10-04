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
    await expect(page.certificate_pdf).to_be_visible()


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
async def test_ai_workflow_navigation_reaches_section(portfolio):
    """Verify the primary navigation reaches the compact AI workflow section."""
    page = PortfolioPage(portfolio)

    await page.ai_workflow_nav_link.click()

    assert portfolio.url.endswith("#ai-workflow")
    await expect(page.ai_workflow_region).to_be_visible()
    await expect(page.ai_workflow_intro).to_be_visible()
    await expect(page.ai_workflow_details_button).to_be_visible()


@pytest.mark.e2e
async def test_ai_workflow_dialog_covers_stages_and_review_practices(portfolio):
    """Verify the details dialog covers workflow stages, guardrails, and tools."""
    page = PortfolioPage(portfolio)

    await page.ai_workflow_details_button.click()

    await expect(page.ai_workflow_dialog).to_be_visible()
    for step_heading in page.ai_workflow_steps.values():
        await expect(step_heading).to_be_visible()
    await expect(page.ai_workflow_guardrails_heading).to_be_visible()
    await expect(page.ai_workflow_lessons_heading).to_be_visible()
    await expect(page.ai_workflow_day_to_day_heading).to_be_visible()
    for tool_tag in page.ai_workflow_tools.values():
        await expect(tool_tag).to_be_visible()
    await expect(page.ai_workflow_dialog.get_by_text("AI is an accelerator, not a source of truth.")).to_be_visible()


@pytest.mark.e2e
async def test_ai_workflow_dialog_can_be_dismissed_with_escape(portfolio):
    """Verify the workflow details dialog supports keyboard dismissal."""
    page = PortfolioPage(portfolio)

    await page.ai_workflow_details_button.click()
    await expect(page.ai_workflow_dialog).to_be_visible()
    await portfolio.keyboard.press("Escape")

    await expect(page.ai_workflow_dialog).to_have_count(0)


@pytest.mark.e2e
async def test_education_section_is_available_from_navigation(portfolio):
    logger.info("Arrange: create the portfolio page object")
    page = PortfolioPage(portfolio)

    logger.info("Act: navigate to the Education section")
    await page.education_nav_link.click()

    logger.info("Assert: education entries and engineering background are visible")
    assert portfolio.url.endswith("#education")
    await expect(page.education_region).to_be_visible()
    await expect(page.education_heading).to_be_visible()
    await expect(page.education_masters_heading).to_be_visible()
    await expect(page.education_bachelors_heading).to_be_visible()
    await expect(page.education_training_heading).to_be_visible()
    await expect(page.education_background).to_be_visible()
    await expect(page.education_region.get_by_text("6.00/6.00").first).to_be_visible()
    assert await page.education_entries.count() == 3
    education_periods = [
        (await entry.inner_text()).splitlines()[0]
        for entry in await page.education_entries.all()
    ]
    assert education_periods == ["2019 – 2020", "2013 – 2015", "2008 – 2012"]


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
async def test_mobile_navigation_has_menu_button(portfolio):
    """Verify the horizontal navigation reaches Education on mobile."""
    logger.info("Arrange: create the portfolio page object")
    page = PortfolioPage(portfolio)

    logger.info("Act: set a mobile viewport and activate Education navigation")
    await portfolio.set_viewport_size({"width": 390, "height": 844})
    await page.education_nav_link.click()

    logger.info("Assert: mobile navigation reaches Education")
    assert portfolio.url.endswith("#education")
    await expect(page.education_region).to_be_visible()


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
