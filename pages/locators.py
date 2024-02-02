from selenium.webdriver.common.by import By


class ContactsPageLocators():
    CONTACTS_LINK = (By.CSS_SELECTOR, '.sbisru-Header__menu-item:nth-child(2)')
    TENSOR_LINK = (By.XPATH, '//a[@href="https://tensor.ru/"]')
    REGION_CHOOSER_TEXT = (By.XPATH, '//div[@class="s-Grid-col s-Grid-col--xm12"]//span['
                                     '@class="sbis_ru-Region-Chooser__text sbis_ru-link"]')

    PARTNERS_LIST = (By.CSS_SELECTOR, '.sbisru-Contacts-List__col.ws-flex-shrink-1.ws-flex-grow-1')
    KAMCHATKA_REGION_TAB = (By.XPATH, '//span[@title="Камчатский край"]')
    KAMCHATKA_PARTNERS_LIST_ELEMENT = (By.XPATH, '//div[@title="СБИС - Камчатка"]')
    TITLE = (By.CSS_SELECTOR, 'title.state-1')


class TensorPageLocators():
    POWER_IN_PEOPLE_BLOCK = (By.XPATH, '//p[contains(text(), "Сила в людях")]')
    POWER_IN_PEOPLE_BLOCK_ABOUT = (By.XPATH, '//a[@href="/about" and contains (@class, "tensor_ru-link")]')
    WORK_BLOCK = (By.XPATH, '//h2[contains(text(), "Работаем")]')
    IMAGE = (By.CSS_SELECTOR, '.tensor_ru-About__block3-image')
