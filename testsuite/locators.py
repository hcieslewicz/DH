from selenium.webdriver.common.by import By

class CommonLocators(object):
    SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
    SEARCH_BUTTON = (By.CSS_SELECTOR, '.nav-search-submit > input:nth-child(2)')

class HomePageLocators(CommonLocators):
    pass

class SearchResultsPageLocators(CommonLocators):
    pass


class LoginPageLocatars(object):
    pass


class SignUpPageLocatars(object):
    pass
