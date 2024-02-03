import os
from .base_page import BasePage
from .locators import SbisContactsPageLocators, SbisHomePageLocators, SbisDownloadPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SbisHomePage(BasePage):
    def go_to_contacts_page(self):
        print("Going to contacts page")
        self.click_element(SbisHomePageLocators.CONTACTS_LINK)

    def go_to_tensor_page(self):
        print("Going to tensor page")

        current_window_handle = self.browser.current_window_handle
        self.click_element(SbisContactsPageLocators.TENSOR_LINK)
        WebDriverWait(self.browser, 10).until(
            lambda browser: len(browser.window_handles) > 1
        )

        new_window_handle = [handle for handle in self.browser.window_handles if handle != current_window_handle][0]
        self.browser.switch_to.window(new_window_handle)

        WebDriverWait(self.browser, 10).until(
            lambda browser: browser.current_url.startswith("https://tensor.ru")
        )

    def go_to_download_sbis_page(self):
        download_page_link = self.browser.find_element(*SbisHomePageLocators.DOWNLOAD_PAGE_LINK)
        self.browser.execute_script(
            "arguments[0].scrollIntoViewIfNeeded();", download_page_link)
        self.click_element(download_page_link)


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
        region = self.browser.find_element(*SbisContactsPageLocators.REGION_CHOOSER_TEXT).text
        assert region, 'Регион не определяется!'
        print(f'Автоопределился регион {region}')

    def is_partners_list_present(self):
        region = self.browser.find_element(*SbisContactsPageLocators.REGION_CHOOSER_TEXT).text
        assert  self.browser.find_element(*SbisContactsPageLocators.PARTNERS_LIST), 'Партнеры не найдены!'
        print(f'Список партнеров в регионе {region} представлен!')

    def change_region(self):
        region_modal_verb = self.browser.find_element(*SbisContactsPageLocators.REGION_CHOOSER_TEXT)
        self.click_element(region_modal_verb)

        kamchatka_region_tab = self.browser.find_element(*SbisContactsPageLocators.KAMCHATKA_REGION_TAB)
        kamchatka_region_tab_text = kamchatka_region_tab.get_attribute('title')
        self.click_element(kamchatka_region_tab)

        WebDriverWait(self.browser, 10).until(
            EC.text_to_be_present_in_element(SbisContactsPageLocators.REGION_CHOOSER_TEXT, kamchatka_region_tab_text)
        )
    def is_region_label_text_was_changed(self):
        region = self.browser.find_element(*SbisContactsPageLocators.REGION_CHOOSER_TEXT).text
        assert region == 'Камчатский край', 'Регион не соответствует выбранному!'
        print(f'Выбран регион {region}')

    def is_partners_list_was_changed(self):
        kamchatka_partners = self.browser.find_element(*SbisContactsPageLocators.KAMCHATKA_PARTNERS_LIST_ELEMENT)
        assert kamchatka_partners, 'Список партнеров не поменялся!'
        print('Список партнеров изменился на соответствующий!')

    def is_tittle_was_changed(self):
        region = self.browser.find_element(*SbisContactsPageLocators.REGION_CHOOSER_TEXT)
        assert region.text in self.get_current_title(), 'Title страницы не соответсвует выбраному региону'
        print(f'Title странцы "{self.get_current_title()}" и регион "{region.text}"')

    def is_url_was_changed(self):
        assert '41-kamchatskij-kraj' in self.get_current_url(), 'url нерпвильный'
        print('Url страницы изменился на нужный')


class SbisDownloadPage(BasePage):
    def testing_sbis_download_page(self):
        self.go_to_sbis_plugin_download_area()
        self.download_file()
        self.compare_file_size()

    def go_to_sbis_plugin_download_area(self):
        new_url = 'https://sbis.ru/download?tab=plugin&innerTab=default'
        self.browser.execute_script(f"window.location.href = '{new_url}';")

    def download_file(self):
        current_dir = os.path.abspath(os.path.dirname(__file__))
        download_link = self.browser.find_element(*SbisDownloadPageLocators.DOWNLOAD_LINK)
        self.click_element(download_link)

        WebDriverWait(self.browser, 10).until(
            lambda x: any(f.endswith('.exe') for f in os.listdir(current_dir))
        )

        downloaded_files = [f for f in os.listdir(current_dir) if f.endswith('.exe')]
        print(f"Список скачанных файлов: {downloaded_files}")
        assert len(downloaded_files) == 1, "Скачивание файла не выполнено или скачано более одного файла"

    def compare_file_size(self):
        current_dir = os.path.abspath(os.path.dirname(__file__))
        downloaded_files = [f for f in os.listdir(current_dir) if f.endswith('.exe')]
        file_path = os.path.join(current_dir, downloaded_files[0])

        file_size_mb = os.path.getsize(file_path) / (1024 * 1024)
        expected_size_mb = float(self.browser.find_element(*SbisDownloadPageLocators.DOWNLOAD_LINK).text.split(' ')[2])

        assert file_size_mb == expected_size_mb, f"Размер файла {file_path} составляет {file_size_mb} Мб, ожидалось {expected_size_mb} Мб"