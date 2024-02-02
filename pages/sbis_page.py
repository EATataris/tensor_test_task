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


class SbisContactsPage(BasePage):

    def testing_sbis_contacts_page(self):
        self.get_region_label_text()
        self.is_partners_list_present()
        self.change_region()
        self.is_region_label_text_was_changed()
        self.is_partners_list_was_changed()
        self.is_tittle_was_changed()
        self.is_url_was_changed()

    def get_region_label_text(self):
        region = self.browser.find_element(*ContactsPageLocators.REGION_CHOOSER_TEXT).text
        assert region, 'Регион не определяется!'
        print(f'Автоопределился регион {region}')

    def is_partners_list_present(self):
        region = self.browser.find_element(*ContactsPageLocators.REGION_CHOOSER_TEXT).text
        assert  self.browser.find_element(*ContactsPageLocators.PARTNERS_LIST), 'Партнеры не найдены!'
        print(f'Список партнеров в регионе {region} представлен!')

    def change_region(self):
        region_modal_verb = self.browser.find_element(*ContactsPageLocators.REGION_CHOOSER_TEXT)
        self.click_element(region_modal_verb)

        kamchatka_region_tab = self.browser.find_element(*ContactsPageLocators.KAMCHATKA_REGION_TAB)
        kamchatka_region_tab_text = kamchatka_region_tab.get_attribute('title')
        self.click_element(kamchatka_region_tab)

        WebDriverWait(self.browser, 10).until(
            EC.text_to_be_present_in_element(ContactsPageLocators.REGION_CHOOSER_TEXT, kamchatka_region_tab_text)
        )

    def is_region_label_text_was_changed(self):
        region = self.browser.find_element(*ContactsPageLocators.REGION_CHOOSER_TEXT).text
        assert region == 'Камчатский край', 'Регион не соответствует выбранному!'
        print(f'Выбран регион {region}')

    def is_partners_list_was_changed(self):
        kamchatka_partners = self.browser.find_element(*ContactsPageLocators.KAMCHATKA_PARTNERS_LIST_ELEMENT)
        assert kamchatka_partners, 'Список партнеров не поменялся!'
        print('Список партнеров изменился на соответствующий!')

    def is_tittle_was_changed(self):
        region = self.browser.find_element(*ContactsPageLocators.REGION_CHOOSER_TEXT)
        assert region.text in self.get_current_title(), 'Title страницы не соответсвует выбраному региону'
        print(f'Title странцы "{self.get_current_title()}" и регион "{region.text}"')

    def is_url_was_changed(self):
        assert '41-kamchatskij-kraj' in self.get_current_url(), 'url нерпвильный'
        print('Url страницы изменился на нужный')