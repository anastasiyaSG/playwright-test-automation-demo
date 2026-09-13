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
        self.philosophy_dialog_heading = PortfolioLocators.philosophy_dialog_heading(page)
        self.experience_dialog_heading = PortfolioLocators.experience_dialog_heading(page)
        self.experience_role = PortfolioLocators.experience_role(page)
        self.toolset_dialog_heading = PortfolioLocators.toolset_dialog_heading(page)
        self.toolset_automation_heading = PortfolioLocators.toolset_automation_heading(page)
        self.project_dialog = PortfolioLocators.project_dialog(page)
        self.project_dialog_close = PortfolioLocators.project_dialog_close(page)
        self.philosophy_outcome = PortfolioLocators.philosophy_outcome(page)
        self.cv_project_dialog_heading = PortfolioLocators.cv_project_dialog_heading(page)
        self.cv_project_github_link = PortfolioLocators.cv_project_github_link(page)
        self.car_watcher_dialog_heading = PortfolioLocators.car_watcher_dialog_heading(page)
