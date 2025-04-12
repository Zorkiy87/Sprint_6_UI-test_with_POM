from selenium.webdriver.common.by import By

from src.locators.base_page_locators import BasePageLocators


class QuestionsLocators(BasePageLocators):
    HOW_MUCH = By.ID, "accordion__heading-0"
    MULTIPLE_SCOOTERS = By.ID, "accordion__heading-1"
    RENTAL_TIME_CALCULATED = By.ID, "accordion__heading-2"
    ORDER_SCOOTER_TODAY = By.ID, "accordion__heading-3"
    EXTEND_THE_ORDER = By.ID, "accordion__heading-4"
    CHARGING_FOR_A_SCOOTER = By.ID, "accordion__heading-5"
    CANCEL_THE_ORDER = By.ID, "accordion__heading-6"
    I_LIVE_ACROSS_THE_MKAD = By.ID, "accordion__heading-7"

    HOW_MUCH_TEXT = By.ID, "accordion__panel-0"
    MULTIPLE_SCOOTERS_TEXT = By.ID, "accordion__panel-1"
    RENTAL_TIME_CALCULATED_TEXT = By.ID, "accordion__panel-2"
    ORDER_SCOOTER_TODAY_TEXT = By.ID, "accordion__panel-3"
    EXTEND_THE_ORDER_TEXT = By.ID, "accordion__panel-4"
    CHARGING_FOR_A_SCOOTER_TEXT = By.ID, "accordion__panel-5"
    CANCEL_THE_ORDER_TEXT = By.ID, "accordion__panel-6"
    I_LIVE_ACROSS_THE_MKAD_TEXT = By.ID, "accordion__panel-7"



