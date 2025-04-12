import allure

from src.locators.base_page_locators import BasePageLocators
from src.pages.base_page import BasePage
from src.locators.order_page_locators import OrderPageLocators

class OrderPage(BasePage):

    @allure.step('Нажатие на кнопку Принять Куки')
    def click_cookie(self):
        self.click_element(BasePageLocators.ACCEPT_COOKIE)

    @allure.step('Ввод имени')
    def set_input_name(self, name):
        input_name = self.find_element(OrderPageLocators.FIELD_INPUT_NAME)
        input_name.send_keys(name)


    @allure.step('Ввод фамилии')
    def set_input_surname(self, surname):
        input_surname = self.find_element(OrderPageLocators.FIELD_INPUT_SURNAME)
        input_surname.send_keys(surname)

    @allure.step('Ввод адреса')
    def set_input_address(self, address):
        input_address = self.find_element(OrderPageLocators.FIELD_INPUT_ADDRESS)
        input_address.send_keys(address)

    @allure.step('Поиск поля "Метро"')
    def find_metro_field(self):
        self.click_element(OrderPageLocators.FIELD_INPUT_METRO_STATION)

    @allure.step('Выбор станции метро Митино')
    def choose_metro_station_mitino(self):
        self.click_element(OrderPageLocators.MITINO_STATION)

    @allure.step('Выбор станции метро Спартак')
    def choose_metro_station_spartak(self):
        self.click_element(OrderPageLocators.SPARTAK_STATION)

    @allure.step('Выбор станции метро')
    def choose_metro_station(self, locator):
        self.click_element(locator)

    @allure.step('Ввод номера телефона для связи')
    def set_input_phone_number(self,phone):
        input_phone = self.find_element(OrderPageLocators.FIELD_INPUT_PHONE_NUMBER)
        input_phone.send_keys(phone)

    @allure.step('Нажатие на кнопку Продолжить')
    def continue_click_button(self):
        self.click_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step('Выбор даты доставки')
    def enter_delivery_date(self):
        self.click_element(OrderPageLocators.FIELD_DATE_DELIVERY_SCOOTER)
        self.click_element(OrderPageLocators.DATE_CHOOSE_DATE)

    @allure.step('Выбор периода аренды в два дня')
    def choosing_rental_period_two_days(self):
        self.click_element(OrderPageLocators.FIELD_RENTAL_PERIOD)
        self.click_element(OrderPageLocators.RENTAL_PERIOD_TWO_DAYS)

    @allure.step('Выбор периода аренды в три дня')
    def choosing_rental_period_three_days(self):
        self.click_element(OrderPageLocators.FIELD_RENTAL_PERIOD)
        self.click_element(OrderPageLocators.RENTAL_PERIOD_THREE_DAYS)

    @allure.step('Выбор цвета самоката чёрный')
    def choosing_color_scooter_black(self):
        self.click_element(OrderPageLocators.COLOR_SCOOTER_BLACK)

    @allure.step('Выбор цвета самоката серый')
    def choosing_color_scooter_grey(self):
        self.click_element(OrderPageLocators.COLOR_SCOOTER_GREY)

    @allure.step('Ввод комментария для курьера')
    def set_input_comment_for_courier(self, comment):
        input_comment = self.find_element(OrderPageLocators.FIELD_COMMENT_FOR_COURIER)
        input_comment.send_keys(comment)

    @allure.step('Подтверждение заказа')
    def order_confirmation(self):
        self.click_element(OrderPageLocators.ORDER_BUTTON)
        self.click_element(OrderPageLocators.CONFIRM_ORDER_BUTTON)

    @allure.step('Заказ подтверждён')
    def order_confirmed(self):
        self.find_element(OrderPageLocators.ORDER_COMPLETE)
        return True

    @allure.step('Нажатие на кнопку заказа в хидере')
    def header_click_order_button(self):
        self.click_element(OrderPageLocators.ORDER_BUTTON_HEADER)

    @allure.step('Нажатие на кнопку заказа в внизу страницы')
    def click_order_button_bottom(self):
        self.click_element(OrderPageLocators.ORDER_BUTTON_BOTTOM)


