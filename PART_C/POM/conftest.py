import pytest
from selenium import webdriver


def pytest_addoption(parser):

    parser.addoption(
        "--browser",
        action="store",
        default="chrome"
    )


@pytest.fixture
def setup(request):

    browser = request.config.getoption("--browser")

    if browser == "chrome":
        driver = webdriver.Chrome()

    elif browser == "edge":
        driver = webdriver.Edge()

    elif browser == "firefox":
        driver = webdriver.Firefox()

    else:
        raise ValueError("Browser not supported")

    driver.maximize_window()

    driver.get("https://www.amazon.in/")

    yield driver

    driver.quit()