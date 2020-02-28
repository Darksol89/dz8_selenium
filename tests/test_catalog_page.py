"""Test for different web element in Catalog page"""
from pages.catalog_page import CatalogPage


def test_catalog_page(browser_driver, get_url):
    browser_driver.find_element(*CatalogPage.OPEN_CATALOG_PAGE).click()
    browser_driver.find_element(*CatalogPage.GRID_BUTTON)
    browser_driver.find_element(*CatalogPage.LIST_BUTTON)
    browser_driver.find_element(*CatalogPage.PRODUCT_LIST)
    browser_driver.find_element(*CatalogPage.SHOW_COMBOBOX)
    browser_driver.find_element(*CatalogPage.SORT_BY)