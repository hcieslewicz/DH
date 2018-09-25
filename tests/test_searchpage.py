import unittest
from selenium import webdriver
from testsuite.pages import *
from testsuite.locators import *
from selenium.webdriver.firefox.options import Options


class TestSearchPages(unittest.TestCase):
    def setUp(self):

        options = Options()
        options.add_argument('-headless')
        binary_path = "E:\geckodriver\geckodriver-v0.19.1\geckodriver.exe"
        self.driver = webdriver.Firefox(executable_path=binary_path, firefox_options=options)
        self.driver.maximize_window()

        self.driver.get("https://www.amazon.de/")
        self.driver.implicitly_wait(2)

    def test_a_page_load(self):
        #print "\n" + str(case_description(0))
        print "\n test a page load"
        home_page = HomePage(self.driver)
        assert home_page.is_title_matches(), "Amazon title doesn't match."

    def test_searchpage(self):
        print "\n test a search page"
        home_page = HomePage(self.driver)
        assert home_page.is_title_matches(), "Amazon title doesn't match."
        text_to_search = 'paw patrol'
        home_page.input_search_text(text_to_search)
        assert home_page.verify_elem_value(text_to_search, *HomePageLocators.SEARCH_FIELD), "Test search is not correct"
        home_page.click_search_button()
        search_results_page = SearchResultsPage(self.driver)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSearchPages)
    unittest.TextTestRunner(verbosity=5).run(suite)
