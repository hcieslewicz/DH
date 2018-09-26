import unittest
from selenium import webdriver
from testsuite.pages import *
from testsuite.locators import *
import pytest


class TestSearchPages(unittest.TestCase):
    def setUp(self):
        grid_url = 'http://localhost:4444/wd/hub'

        if pytest.config.getoption('driver') == 'chrome':
            desired_capabilities = webdriver.DesiredCapabilities.CHROME
        elif pytest.config.getoption('driver') == 'ie':
            desired_capabilities = webdriver.DesiredCapabilities.INTERNETEXPLORER
        else:
            desired_capabilities = webdriver.DesiredCapabilities.FIREFOX

        self.driver = webdriver.Remote(command_executor=grid_url, desired_capabilities=desired_capabilities)
        self.driver.get("https://www.amazon.de/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    """
    def test_a_page_load(self):
        #print "\n" + str(case_description(0))
        print "\n test a page load"
        home_page = HomePage(self.driver)
        assert home_page.is_title_matches(), "Amazon title doesn't match."
    """

    def test_searchpage(self):
        text_to_search = 'zuma t-shirt'
        print "\ntest a search page using keywards: %s" % text_to_search
        home_page = HomePage(self.driver)
        assert home_page.is_title_matches(), "Amazon title doesn't match."
        home_page.input_search_text(text_to_search)
        assert home_page.verify_elem_value(text_to_search, *HomePageLocators.SEARCH_FIELD), "Test search is not correct"
        home_page.click_search_button()
        search_results_page = SearchResultsPage(self.driver)
        assert search_results_page.verify_results(text_to_search)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSearchPages)
    unittest.TextTestRunner(verbosity=5).run(suite)
