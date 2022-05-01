from selenium.webdriver.common.by import By
from tests.config import HOME_URL
from tests.step_defs import conftest


class SearchResultPage:
    SEARCH_RESULTS_TITLES = (By.XPATH, "//a[@class='product-name' and @itemprop='url']")
    SEARCH_RESULT_COUNTER = (By.XPATH, "//span[@class='heading-counter']")
    NO_RESULTS_ALERT = (By.XPATH, "//p[@class='alert alert-warning']")

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(str(HOME_URL))

    def get_search_items(self):
        conftest.wait_for_element(self.browser, self.SEARCH_RESULT_COUNTER)
        results = self.browser.find_elements(*self.SEARCH_RESULTS_TITLES)
        return results

    def get_no_results_element(self):
        conftest.wait_for_element(self.browser, self.NO_RESULTS_ALERT)
        return self.browser.find_element(*self.NO_RESULTS_ALERT)

    def get_result_counter(self):
        conftest.wait_for_element(self.browser, self.SEARCH_RESULT_COUNTER)
        return self.browser.find_element(*self.SEARCH_RESULT_COUNTER)
