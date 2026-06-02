import pytest

from pages.BasePage import BasePage
from data.bestbuy_data import bestbuy_url


class Walmart(BasePage):
    def __init__(self, page):
        super().__init__(page)

    @pytest.mark.bestbuy
    def test_run_bestbuy_workflow(self):
        self.navigate_to_url(bestbuy_url)
        