import time
from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from .locators import TensorPageLocators


class TensorHomePage(BasePage):

    def is_block_sila_present(self):
        try:
            element = WebDriverWait(self.browser, 15).until(
                EC.presence_of_element_located(TensorPageLocators.POWER_IN_PEOPLE_BLOCK)
            )
            print(f"Block 'Сила в людях' found: {element.text}")
        except TimeoutException:
            print("TimeoutException: Block 'Сила в людях' not found!")
            raise

    def go_to_about_page(self):
        about_link = self.browser.find_element(*TensorPageLocators.POWER_IN_PEOPLE_BLOCK_ABOUT)
        self.browser.execute_script(
            # "arguments[0].scrollIntoView({behavior: 'smooth', block: 'start', inline: 'nearest'});", about_link)
            "arguments[0].scrollIntoViewIfNeeded();", about_link)
        self.click_element(TensorPageLocators.POWER_IN_PEOPLE_BLOCK_ABOUT)
        time.sleep(3)

    def is_about_page_opened(self):
        assert 'tensor.ru/about' in self.get_current_url(), 'Открыта какая-то хрень'
        print('Открытая ссылка является ссылкой "tensor.ru/about"')

    def is_pictures_sizes_are_equal(self):
        work_block = self.browser.find_element(*TensorPageLocators.WORK_BLOCK)
        self.browser.execute_script(
            "arguments[0].scrollIntoViewIfNeeded();", work_block)

        images = self.browser.find_elements(*TensorPageLocators.IMAGE)
        for img in images:
            width = img.get_attribute('width')
            height = img.get_attribute('height')
            assert width == images[0].get_attribute('width') and height == images[0].get_attribute('height'), 'Размеры изображений не равны!'
        print(f'Изображения в блоке "{work_block.text}" одинакового размера')