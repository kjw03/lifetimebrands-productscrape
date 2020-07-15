"""Runner test

Contains all unit tests for the lifetimewebscrape.runner module.
"""

from typing import List
import os

import pytest
 
from lifetimewebscrape import runner

class TestRunner(object):
    """Runner test class"""

    module_dir = os.path.dirname(os.path.abspath(__file__))

    @pytest.fixture()
    def in_stock_product_web_page_scrapes(self) -> List[str]:
        """A list of files containing web page scrapes for in stock products"""
        return ['./../../../resources/instock_farber_knife']

    @pytest.fixture()
    def out_of_stock_product_web_page_scrapes(self) -> List[str]:
        """A list of files containing web page scrapes for out of stock products"""
        return ['./../../../resources/outofstock_trampoline']

    def test_check_web_page_text_for_in_stock_indicator(self, in_stock_product_web_page_scrapes):
        """Each test in this set should return a value of true to indicate an in stock item"""
        for web_scrape_file in in_stock_product_web_page_scrapes:
            with open(os.path.join(self.module_dir, web_scrape_file), 'r') as f:
                assert True == runner.check_web_page_text_for_in_stock_indicator(f.read())

    def test_check_web_page_text_for_out_of_stock_indicator(self, out_of_stock_product_web_page_scrapes):
        """Each test in this set should return a value of false to indicate an out of stock item"""
        for web_scrape_file in out_of_stock_product_web_page_scrapes:
            with open(os.path.join(self.module_dir, web_scrape_file), 'r') as f:
                assert False == runner.check_web_page_text_for_in_stock_indicator(f.read())

