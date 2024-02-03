import pytest, os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def browser(request):
    chrome_options = Options()
    chrome_options.add_experimental_option("prefs", {
        "download.default_directory": os.path.abspath(os.path.dirname(__file__)),
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    })

    print("\nstart browser for test..")
    browser = webdriver.Chrome(options=chrome_options)
    # browser.implicitly_wait(10)
    yield browser
    print("\nquit browser..")
    browser.quit()