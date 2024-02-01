from .pages.base_page import BasePage


def test_guest_can_go_to_login_page(browser):
    link = "https://sbis.ru/"
    page = BasePage(browser, link)
    page.open()
    page.go_to_contacts_page()