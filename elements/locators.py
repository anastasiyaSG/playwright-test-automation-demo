"""Centralized semantic locator factories for the portfolio page."""

from playwright.async_api import Page


class PortfolioLocators:
    """Build page locators without embedding selectors in tests."""

    @staticmethod
    def page_heading(page: Page):
        return page.get_by_role("heading", name="QA Engineer / SDET", level=1)

    @staticmethod
    def profile_photo(page: Page):
        return page.get_by_role("img", name="Anastasiya Georgieva")

    @staticmethod
    def case_studies_link(page: Page):
        return page.get_by_role("link", name="View case studies")

    @staticmethod
    def contact_cta(page: Page):
        return page.get_by_role("link", name="Get in touch")

    @staticmethod
    def mobile_navigation_menu_button(page: Page):
        return page.get_by_role("button", name="Open navigation")

    @staticmethod
    def case_study_heading(page: Page):
        return page.get_by_role(
            "heading", name="Black Friday: capacity testing that prevented an incident"
        )

    @staticmethod
    def contact_heading(page: Page):
        return page.get_by_role("heading", name="Let's talk about quality at scale.")

    @staticmethod
    def contact_email(page: Page):
        return page.get_by_role("link", name="anastassiya.georgieva@gmail.com")

    @staticmethod
    def contact_linkedin(page: Page):
        return page.get_by_role("link", name="linkedin.com/in/anastasiya-georgieva")

    @staticmethod
    def contact_github(page: Page):
        return page.get_by_role("link", name="github.com/anastasiyaSG")

    @staticmethod
    def resume_download_link(page: Page):
        return page.get_by_role("link", name="Download résumé (PDF) →")

    @staticmethod
    def certificate_button(page: Page):
        return page.get_by_role("button", name="Certified ISTQB Test Automation Engineer")

    @staticmethod
    def philosophy_button(page: Page):
        return page.get_by_role("button", name="View QA philosophy and outcomes →")

    @staticmethod
    def experience_button(page: Page):
        return page.get_by_role("button", name="View experience details →")

    @staticmethod
    def toolset_button(page: Page):
        return page.get_by_role("button", name="View complete toolset →")

    @staticmethod
    def cv_project_button(page: Page):
        return page.get_by_role("button", name="Evolved CV Builder View project details →")

    @staticmethod
    def car_watcher_project_button(page: Page):
        return page.get_by_role("button", name="car-watcher View project details →")

    @staticmethod
    def dialog(page: Page):
        return page.get_by_role("dialog")

    @staticmethod
    def certificate_dialog_heading(page: Page):
        return page.get_by_role(
            "heading",
            name="ISTQB Certified Tester, Specialist Level Test Automation Engineer",
        )

    @staticmethod
    def philosophy_dialog_heading(page: Page):
        return page.get_by_role("heading", name="Quality work starts before testing")

    @staticmethod
    def experience_dialog_heading(page: Page):
        return page.get_by_role("heading", name="Career log details")

    @staticmethod
    def experience_role(page: Page):
        return page.get_by_role(
            "heading", name="Senior QA Engineer (Automation & Quality Strategy)"
        ).last

    @staticmethod
    def toolset_dialog_heading(page: Page):
        return page.get_by_role("heading", name="Complete toolset")

    @staticmethod
    def toolset_automation_heading(page: Page):
        return page.get_by_role("heading", name="Automation & Testing").last

    @staticmethod
    def project_dialog(page: Page):
        return page.get_by_role("dialog")

    @staticmethod
    def project_dialog_close(page: Page):
        return page.get_by_role("button", name="Close")

    @staticmethod
    def philosophy_outcome(page: Page):
        return page.get_by_text("Approximately 120 non-escaped defects were identified")

    @staticmethod
    def cv_project_dialog_heading(page: Page):
        return page.get_by_role("heading", name="Evolved CV Builder").last

    @staticmethod
    def cv_project_github_link(page: Page):
        return page.get_by_role("link", name="Open project on GitHub →")

    @staticmethod
    def car_watcher_dialog_heading(page: Page):
        return page.get_by_role("heading", name="car-watcher").last
