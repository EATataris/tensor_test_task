from selenium.webdriver.common.by import By


class BasePageLocator():
    CONTACTS_LINK = (By.CSS_SELECTOR, '.sbisru-Header__menu-item:nth-child(2)')