from .pages.sbis_page import SbisHomePage, SbisDownloadPage


def test_run(browser):
    link = "https://sbis.ru"
    page = SbisHomePage(browser, link)
    page.open()
    page.go_to_download_sbis_page()
    download_page = SbisDownloadPage(browser, browser.current_url)
    download_page.testing_sbis_download_page()
