from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate_to_url(self,url):
        self.page.goto(url)