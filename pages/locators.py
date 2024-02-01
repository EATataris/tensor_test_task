from selenium.webdriver.common.by import By


class ContactsPageLocators():
    CONTACTS_LINK = (By.CSS_SELECTOR, '.sbisru-Header__menu-item:nth-child(2)')
    TENSOR_LINK = (By.XPATH, '//a[@href="https://tensor.ru/"]')


class TensorPageLocator():
    POWER_IN_PEOPLE_BLOCK = (By.XPATH, '//p[contains(text(), "Сила в людях")]')
    POWER_IN_PEOPLE_BLOCK_ABOUT = (By.XPATH, '//a[@href="/about" and contains (@class, "tensor_ru-link")]')
