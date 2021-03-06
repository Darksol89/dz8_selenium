"""Selectors for different elements in the Opencart product page """
import logging
from selenium.common.exceptions import NoSuchElementException
from PageObject.GeneralLocators import GeneralSelectors
from PageObject.BasePage import BasePage
from selenium.webdriver.common.by import By
from helpers.page_helpers import wait_for_element

product_logger = logging.getLogger('Product Page')


class ProductPage(BasePage):
    ADD_TO_CARD = (By.CSS_SELECTOR, '.form-group #button-cart')
    QUANTITY = (By.CSS_SELECTOR, '#input-quantity')
    ADD_TO_WISH_LIST = (By.XPATH, '//button[@data-original-title="Add to Wish List"]')
    COMPARE_PRODUCT = (By.XPATH, "//button[@data-original-title='Compare this Product']")
    RATING = (By.CSS_SELECTOR, '.rating')

    def open_product_page(self):
        self._click_to_element(GeneralSelectors.OPEN_MACBOOK_PRODUCT_PAGE)
        product_logger.info('Open Product Page')
        return self

    def add_to_card(self):
        """Check add to card button"""
        try:
            wait_for_element(self.driver, self.ADD_TO_CARD)
            self._click_to_element(self.ADD_TO_CARD)
        except NoSuchElementException:
            print('Add to Card button is not displayed')

        return self

    def quantity(self, qty):
        """Check input quantity"""
        try:
            wait_for_element(self.driver, self.QUANTITY)
            self._send_keys(qty, self.QUANTITY)
        except NoSuchElementException:
            print('Quantity field is not available')

        return self

    def add_to_wish_list(self):
        self._click_to_element(self.ADD_TO_WISH_LIST)
        return self

    def compare_product(self):
        self._click_to_element(self.COMPARE_PRODUCT)
        return self

    def rating(self):
        """Check rating stage"""
        try:
            wait_for_element(self.driver, self.RATING)
            rating = self.driver.find_element(*self.RATING)
            rating.is_displayed()
        except NoSuchElementException:
            print('Rating stage is not displayed')

        return self
