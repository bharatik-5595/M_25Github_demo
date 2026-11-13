from selenium.webdriver.support.ui import Select


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        self.driver.find_element(*locator).click()

    def send_keys(self, locator, value):
        self.driver.find_element(*locator).send_keys(value)

    def select_option(self, locator, value):
        dropdown = self.driver.find_element(*locator)
        select = Select(dropdown)
        select.select_by_visible_text(value)