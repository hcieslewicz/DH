from selenium.webdriver.common.by import By


class CommonLocators(object):
    SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
    SEARCH_BUTTON = (By.CSS_SELECTOR, '.nav-search-submit > input:nth-child(2)')


class HomePageLocators(CommonLocators):
    pass


class SearchResultsPageLocators(CommonLocators):
    SEARCH_RESULT_LIST = (By.CSS_SELECTOR, '#s-results-list-atf')
    PAGINATION_NEXT_LINK = (By.ID, 'pagnNextLink')
    DATA_ATTRIBUTE_TITLE = (By.CSS_SELECTOR, 'h2[data-attribute]')


class LoginPageLocatars(object):
    pass


class SignUpPageLocatars(object):
    pass
