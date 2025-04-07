from selenium.webdriver.common.by import By

class OrderPageLocators():
    FIELD_INPUT_NAME = By.CSS_SELECTOR, "input[placeholder='* Имя']"
    FIELD_INPUT_SURNAME = By.CSS_SELECTOR, "input[placeholder='* Фамилия']"
    FIELD_INPUT_ADDRESS = By.CSS_SELECTOR, "input[placeholder='* Адрес: куда привезти заказ']"
    FIELD_INPUT_METRO_STATION = By.CSS_SELECTOR, "input[placeholder='* Станция метро']"
    FIELD_INPUT_PHONE_NUMBER = By.CSS_SELECTOR, "input[placeholder='* Телефон: на него позвонит курьер']"

    FIELD_DATE_DELIVERY_SCOOTER = By.CSS_SELECTOR, "input[placeholder='* Когда привезти самокат']"
    DATE_CHOOSE_DATE =By.XPATH, "//div[@aria-label='Choose четверг, 1-е мая 2025 г.']"

    FIELD_RENTAL_PERIOD = By.XPATH, "//div[@class='Dropdown-control']"
    RENTAL_PERIOD_TWO_DAYS = By.XPATH, "//div[@class='Dropdown-option' and text()='двое суток']"
    RENTAL_PERIOD_THREE_DAYS = By.XPATH, "//div[@class='Dropdown-option' and text()='трое суток']"

    FIELD_COMMENT_FOR_COURIER = By.CSS_SELECTOR, "input[placeholder='Комментарий для курьера']"

    NEXT_BUTTON = By.XPATH, "//button[text()='Далее']"
    ORDER_BUTTON = By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"
    CONFIRM_ORDER_BUTTON = By.XPATH, "//button[text()='Да']"
    ORDER_COMPLETE = By.XPATH, "//div[@class='Order_ModalHeader__3FDaJ']"

    MITINO_STATION = By.XPATH, "//button[contains(@class, 'select-search__option')]//div[contains(@class, 'Order_Text__2broi') and text()='Митино']"
    SPARTAK_STATION = By.XPATH, "//button[contains(@class, 'select-search__option')]//div[contains(@class, 'Order_Text__2broi') and text()='Спартак']"


    COLOR_SCOOTER_BLACK = By.ID, "black"
    COLOR_SCOOTER_GREY = By.ID, "grey"

    ORDER_BUTTON_HEADER = By.CLASS_NAME, "Button_Button__ra12g"
    ORDER_BUTTON_BOTTOM = By.XPATH, "//button[contains(@class, 'Button_Button') and contains(text(), 'Заказать')]"





