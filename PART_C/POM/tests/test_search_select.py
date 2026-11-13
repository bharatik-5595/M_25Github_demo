import pytest

from pages.search_page import SearchPage
from pages.select_page import SelectPage
from utilities.excel_utils import get_excel_data


@pytest.mark.parametrize(
    "product, sort_option",
    get_excel_data()
)
def test_search_select(setup, product, sort_option):

    driver = setup

    search = SearchPage(driver)

    select = SelectPage(driver)

    # Search product
    search.search_product(product)

    # Select Sort By option
    select.select_sort_option(sort_option)