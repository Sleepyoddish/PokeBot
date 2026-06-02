from pages.BasePage import BasePage


class WalmartPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def login(self, username, password):
        self.page.get_by_role("button", name="Sign In").click()
        self.page.get_by_role("button", name="Sign in or create account").click()

