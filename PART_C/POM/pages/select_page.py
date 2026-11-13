from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SelectPage(BasePage):

    SORT_DROPDOWN = (By.ID, "s-result-sort-select")

    def select_sort_option(self, option):

        self.select_option(self.SORT_DROPDOWN, option)