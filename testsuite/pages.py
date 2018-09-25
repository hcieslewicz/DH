from base import Page
from testsuite.locators import *

class CommonPage(Page):
    def input_search_text(self, search_text):
        self.find_element(*self.locator.SEARCH_FIELD).clear()
        self.find_element(*self.locator.SEARCH_FIELD).send_keys(search_text)

    def click_search_button(self):
        self.find_element(*self.locator.SEARCH_BUTTON).click()

class SearchResultsPage(CommonPage):
    pass

class HomePage(CommonPage):
    def __init__(self, driver):
        self.locator = HomePageLocators
        super(HomePage, self).__init__(driver)

    def is_title_matches(self):
        """Verifies that the hardcoded text "Amazon" appears in page title"""
        return "Amazon" in self.driver.title


class LoginPage(CommonPage):
    pass


class SignUpPage(CommonPage):
    pass
