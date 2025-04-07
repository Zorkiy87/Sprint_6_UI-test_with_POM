from selenium.webdriver.common.by import By


class BasePageLocators:
    ACCEPT_COOKIE = By.ID, "rcc-confirm-button"
    YANDEX_LOGO = By.CLASS_NAME, "Header_LogoYandex__3TSOI"
    SCOOTER_LOGO = By.XPATH,'//a[@class="Header_LogoScooter__3lsAR"]'


