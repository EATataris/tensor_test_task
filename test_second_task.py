from .pages.sbis_page import SbisHomePage, SbisContactsPage


def test_go_to_contacts_page(browser):
    link = "https://sbis.ru"
    page = SbisHomePage(browser, link)
    page.open()
    page.go_to_contacts_page()
    contacts_page = SbisContactsPage(browser, browser.current_url)
    contacts_page.testing_sbis_contacts_page()