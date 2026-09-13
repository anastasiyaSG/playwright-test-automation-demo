# Portfolio Playwright Demo

[![Portfolio smoke tests](https://github.com/anastasiyaSG/playwright-test-automation-demo/actions/workflows/daily-tests.yml/badge.svg)](https://github.com/anastasiyaSG/playwright-test-automation-demo/actions/workflows/daily-tests.yml)

A deliberately small async Playwright + pytest project that tests my deployed QA Engineer / SDET portfolio. It demonstrates a readable Page Object Model, semantic locators, a thin actions layer, isolated browser fixtures, and a CI-generated HTML report.

Target: <https://anastasiyasg.github.io/portfolio/>

## What it tests

- The homepage title and H1 clearly identify the QA Engineer / SDET positioning.
- The “View case studies” hero link reaches the featured Black Friday case study.
- The “Get in touch” hero link reaches the contact section.
- The contact email, LinkedIn, and GitHub links are visible and have destinations.
- The profile photo is visible.
- Six detail dialogs open with the expected content.

These are intentionally smoke-level checks for a portfolio, not a large synthetic test suite.

## Structure

```text
pages/       PortfolioPage element references only
elements/    Centralized semantic locator factories
actions/     Browser, context, page, and environment fixtures
tests/e2e/   Basic portfolio smoke and interaction tests
```

Tests use `get_by_role` and visible text. There are no XPath selectors and no hardcoded CSS selectors.

## Run locally

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m playwright install chromium
pytest
```

The self-contained HTML report is written to `playwright-report/index.html`.

To test another deployment:

```powershell
$env:BASE_URL = "http://localhost:5173/portfolio/"
pytest
```

## Publish the report

See [REPORT_PUBLISHING.md](REPORT_PUBLISHING.md) for the repository and GitHub Pages setup steps.

## Add it to the portfolio

See [PORTFOLIO_DEMO_PROMPT.md](PORTFOLIO_DEMO_PROMPT.md) for a ready-to-use implementation brief for the portfolio repository.
