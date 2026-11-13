from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SearchPage(BasePage):

    SEARCH_BOX = (By.ID, "twotabsearchtextbox")
    SEARCH_BUTTON = (By.ID, "nav-search-submit-button")

    def search_product(self, product):

        self.send_keys(self.SEARCH_BOX, product)

        self.click(self.SEARCH_BUTTON)