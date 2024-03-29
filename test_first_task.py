from .pages.sbis_page import SbisHomePage
from .pages.tensor_page import TensorHomePage


def test_run(browser):
    link = "https://sbis.ru"
    page = SbisHomePage(browser, link)
    page.open()
    page.go_to_contacts_page()
    page.go_to_tensor_page()

    tensor_page = TensorHomePage(browser, browser.current_url)
    tensor_page.is_block_sila_present()
    tensor_page.go_to_about_page()
    tensor_page.is_about_page_opened()
    tensor_page.are_pictures_sizes_equal()