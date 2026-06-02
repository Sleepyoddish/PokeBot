import os

import pytest
from playwright.sync_api import sync_playwright


HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"
SLOWMO = int(os.getenv("SLOWMO", "0"))


@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="session")
def browser(playwright_instance):
    print(f"Launching browser with headless={HEADLESS}, slow_mo={SLOWMO}")
    browser = playwright_instance.chromium.launch(
        headless=HEADLESS,
        slow_mo=SLOWMO
    )
    yield browser
    browser.close()

@pytest.fixture
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()


