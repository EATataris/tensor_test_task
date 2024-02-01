import time

from selenium.common import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage():

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def is_element_present(self, locator):
        try:
            self.browser.find_element(locator)
        except NoSuchElementException:
            return False
        return True

    def click_element(self, locator):
        print(f"Clicking element: {locator}")
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(locator)).click()

    def find_elements(self, locator):
        return self.browser.find_elements(*locator)

    def get_current_url(self):
        return self.browser.current_url

    def open(self):
        self.browser.get(self.url)

