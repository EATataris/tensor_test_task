import time

from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from .locators import TensorPageLocator


class TensorHomePage(BasePage):
    # def is_block_sila_present(self):
    #     assert self.is_element_present(TensorPageLocator.POWER_IN_PEOPLE_BLOCK), "Блок 'Сила в людях' не найден!"

    def is_block_sila_present(self):
        try:
            element = WebDriverWait(self.browser, 15).until(
                EC.presence_of_element_located(TensorPageLocator.POWER_IN_PEOPLE_BLOCK)
            )
            print(f"Block 'Сила в людях' found: {element.text}")
        except TimeoutException:
            print("TimeoutException: Block 'Сила в людях' not found!")
            raise

    def go_to_about_page(self):
        about_link = self.browser.find_element(*TensorPageLocator.POWER_IN_PEOPLE_BLOCK_ABOUT)
        self.browser.execute_script(
            "arguments[0].scrollIntoView({behavior: 'auto', block: 'center', inline: 'center'});", about_link)
        self.click_element(TensorPageLocator.POWER_IN_PEOPLE_BLOCK_ABOUT)
        time.sleep(3)

    def is_about_page_opened(self):
        try:
            if 'tensor.ru/about' in self.get_current_url():
                print(f'Открытая ссылка является ссылкой "tensor.ru/about"')
        except NoSuchElementException:
            print(f'Открыта какая-то хрень')
            raise
        # return 'tensor.ru/about' in self.get_current_url()