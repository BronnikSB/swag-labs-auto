from pages.reports.main_page import MainPage
from playwright.sync_api import expect


def test_01(auth_page):
    main_page = MainPage(auth_page)
    count = main_page.get_count_product_list()
    product_names = main_page.get_name_product_list()
    assert count == 6
    assert "Sauce Labs Backpack" in product_names
