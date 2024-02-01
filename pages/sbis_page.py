from .base_page import BasePage
from .locators import ContactsPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SbisHomePage(BasePage):
    def go_to_contacts_page(self):
        print("Going to contacts page")
        self.click_element(ContactsPageLocators.CONTACTS_LINK)

    def go_to_tensor_page(self):
        print("Going to tensor page")

        current_window_handle = self.browser.current_window_handle
        self.click_element(ContactsPageLocators.TENSOR_LINK)
        WebDriverWait(self.browser, 10).until(
            lambda browser: len(browser.window_handles) > 1
        )

        new_window_handle = [handle for handle in self.browser.window_handles if handle != current_window_handle][0]
        self.browser.switch_to.window(new_window_handle)

        WebDriverWait(self.browser, 10).until(
            lambda browser: browser.current_url.startswith("https://tensor.ru")
        )
