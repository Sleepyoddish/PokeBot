import pytest

from pages.BasePage import BasePage
from data.walmart_data import walmart_url


class Walmart(BasePage):
    def __init__(self, page):
        super().__init__(page)

        
    @pytest.mark.walmart
    def test_run_walmart_workflow(self):
        self.navigate_to_url(walmart_url)
        self.page.get_by_role("button", name="Sign In").click()
        self.page.get_by_role("button", name="Sign in or create account").click()
        # Add more steps for the Walmart workflow here, such as logging in, searching for products, etc.
    