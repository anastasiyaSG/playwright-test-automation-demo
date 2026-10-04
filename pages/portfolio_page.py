"""Portfolio page elements used by the test suite."""

from playwright.async_api import Page

from elements.locators import PortfolioLocators


class PortfolioPage:
    """Page object containing elements only, following the project convention."""

    def __init__(self, page: Page) -> None:
        self.page = page
        self.page_heading = PortfolioLocators.page_heading(page)
        self.profile_photo = PortfolioLocators.profile_photo(page)
        self.case_studies_link = PortfolioLocators.case_studies_link(page)
        self.contact_cta = PortfolioLocators.contact_cta(page)
        self.ai_workflow_nav_link = PortfolioLocators.ai_workflow_nav_link(page)
        self.education_nav_link = PortfolioLocators.education_nav_link(page)
        self.mobile_navigation_menu_button = PortfolioLocators.mobile_navigation_menu_button(page)
        self.case_study_heading = PortfolioLocators.case_study_heading(page)
        self.contact_heading = PortfolioLocators.contact_heading(page)
        self.contact_email = PortfolioLocators.contact_email(page)
        self.contact_linkedin = PortfolioLocators.contact_linkedin(page)
        self.contact_github = PortfolioLocators.contact_github(page)
        self.resume_download_link = PortfolioLocators.resume_download_link(page)
        self.certificate_button = PortfolioLocators.certificate_button(page)
        self.philosophy_button = PortfolioLocators.philosophy_button(page)
        self.experience_button = PortfolioLocators.experience_button(page)
        self.toolset_button = PortfolioLocators.toolset_button(page)
        self.cv_project_button = PortfolioLocators.cv_project_button(page)
        self.car_watcher_project_button = PortfolioLocators.car_watcher_project_button(page)
        self.dialog = PortfolioLocators.dialog(page)
        self.certificate_dialog_heading = PortfolioLocators.certificate_dialog_heading(page)
        self.certificate_pdf = PortfolioLocators.certificate_pdf(page)
        self.philosophy_dialog_heading = PortfolioLocators.philosophy_dialog_heading(page)
        self.experience_dialog_heading = PortfolioLocators.experience_dialog_heading(page)
        self.experience_role = PortfolioLocators.experience_role(page)
        self.toolset_dialog_heading = PortfolioLocators.toolset_dialog_heading(page)
        self.toolset_automation_heading = PortfolioLocators.toolset_automation_heading(page)
        self.ai_workflow_region = PortfolioLocators.ai_workflow_region(page)
        self.ai_workflow_intro = PortfolioLocators.ai_workflow_intro(page)
        self.ai_workflow_details_button = PortfolioLocators.ai_workflow_details_button(page)
        self.ai_workflow_dialog = PortfolioLocators.ai_workflow_dialog(page)
        self.ai_workflow_steps = {
            name: PortfolioLocators.ai_workflow_step_heading(page, name)
            for name in (
                "Requirements refinement",
                "Test case design",
                "Documentation",
                "Automation",
                "Test data",
                "Continuous improvement",
            )
        }
        self.ai_workflow_guardrails_heading = PortfolioLocators.ai_workflow_subsection_heading(
            page, "Guardrails and responsible use"
        )
        self.ai_workflow_lessons_heading = PortfolioLocators.ai_workflow_subsection_heading(
            page, "Lessons learned"
        )
        self.ai_workflow_day_to_day_heading = PortfolioLocators.ai_workflow_subsection_heading(
            page, "Day-to-day"
        )
        self.ai_workflow_tools = {
            name: PortfolioLocators.ai_workflow_tool(page, name)
            for name in ("Claude Code", "Confluence", "Playwright", "Synthetic test data")
        }
        self.education_region = PortfolioLocators.education_region(page)
        self.education_entries = PortfolioLocators.education_entries(page)
        self.education_heading = PortfolioLocators.education_heading(page)
        self.education_training_heading = self.education_region.get_by_role(
            "heading", name="QA Automation training", exact=True
        )
        self.education_masters_heading = self.education_region.get_by_role(
            "heading", name="MSc, Logistics Engineering", exact=True
        )
        self.education_bachelors_heading = self.education_region.get_by_role(
            "heading", name="BSc, Aviation Engineering", exact=True
        )
        self.education_background = page.get_by_text(
            "Engineering background in safety-critical, process-driven fields, "
            "which shaped my risk-based approach to quality."
        )
        self.project_dialog = PortfolioLocators.project_dialog(page)
        self.project_dialog_close = PortfolioLocators.project_dialog_close(page)
        self.philosophy_outcome = PortfolioLocators.philosophy_outcome(page)
        self.cv_project_dialog_heading = PortfolioLocators.cv_project_dialog_heading(page)
        self.cv_project_github_link = PortfolioLocators.cv_project_github_link(page)
        self.car_watcher_dialog_heading = PortfolioLocators.car_watcher_dialog_heading(page)
