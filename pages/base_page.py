from .locators import BasePageLocator


class BasePage():

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def go_to_contacts_page(self):
        contacts_link = self.browser.find_element(*BasePageLocator.CONTACTS_LINK)
        contacts_link.click()