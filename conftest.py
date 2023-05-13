import pytest


@pytest.fixture()
def open_page(playwright):
    browser = playwright.chromium.launch(headless=False, args=["--start-maximized", '--headless=chrome'])
    context = browser.new_context(viewport={'width': 1920, 'height': 1080})
    page = context.new_page()
    page.set_extra_http_headers({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                                               'AppleWebKit/537.36 (KHTML, like Gecko) '
                                               'Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299'})
    page.goto("https://www.kiwi.com")
    page.wait_for_load_state()
    return page
