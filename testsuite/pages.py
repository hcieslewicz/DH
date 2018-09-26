from base import Page
from testsuite.locators import *
from selenium.common.exceptions import TimeoutException
from testsuite.delayed_assert import expect, assert_expectations

class CommonPage(Page):
    def input_search_text(self, search_text):
        self.find_element(*self.locator.SEARCH_FIELD).clear()
        self.find_element(*self.locator.SEARCH_FIELD).send_keys(search_text)

    def click_search_button(self):
        self.find_element(*self.locator.SEARCH_BUTTON).click()

class SearchResultsPage(CommonPage):
    def __init__(self, driver):
        self.locator = SearchResultsPageLocators
        super(SearchResultsPage, self).__init__(driver)

    def verify_results(self, text_to_search):
        counter = 0
        while True:
            for result in self.find_element(*self.locator.SEARCH_RESULT_LIST).find_elements_by_tag_name('li'):
                counter += 1
                if "Gesponsert" in result.text:
                    #Skip sponsored links, cause sometimes they are not releated to search text
                    continue
                else:
                    # Fail with first situation, where searched text is not in item description:
                    # "assert text_to_search.lower() in result.text.lower()"
                    # Second way is to gather failed assertions and fail the test at the end of execution
                    # using "expect" and "assert_expectations" calls
                    # Looking for the fraze (or any word from it) will fail, when returned results
                    # will contain items related to searched fraze, but in the same time they don't contain any of words
                    # from the fraze.
                    # In this case "zuma" is part of "paw patrol", but item from results don't contain "zuma" word.
                    # Test will fail in above case. Final result: 101/148 passed

                    word_list = text_to_search.lower().split()
                    item_description = result.text.lower()

                    found = 0
                    for word in word_list:
                        if word in item_description:
                            found =1
                    expect(found >=1 ,"Text \"%s\" not in \"%s\"" % (text_to_search.lower(),result.text.lower()))

            try:
                next_button = self.find_element(*self.locator.PAGINATION_NEXT_LINK)
            except TimeoutException:
                break

            self.open(next_button.get_attribute('href'))
        assert_expectations()


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
