import pytest


@pytest.fixture()
def open_page(playwright):
    browser = playwright.chromium.launch(headless=False, args=["--start-maximized"])
    context = browser.new_context(viewport={'width': 1920, 'height': 1080})
    page = context.new_page()
    page.goto("https://www.kiwi.com")
    page.wait_for_load_state()
    return page
