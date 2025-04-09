import allure
import pytest

from src.pages.order_page import OrderPage
from data import FirstSetOrderData


class TestOrderPage:

    @allure.title('Заполнение формы заказа самоката')
    @allure.description('Заполнение формы заказа самоката, через 2 различные кнопки заказа (в хидере и в конце страницы)')
    @pytest.mark.parametrize('order_button', ['header_click_order_button', 'click_order_button_bottom'])
    def test_order_page(self, driver, order_button):
        order_page = OrderPage(driver)
        order_page.click_cookie()
        order_button_func = getattr(order_page, order_button)
        order_button_func()
        order_page.set_input_name(FirstSetOrderData.NAME)
        order_page.set_input_surname(FirstSetOrderData.SURNAME)
        order_page.set_input_address(FirstSetOrderData.ADDRESS)
        order_page.find_metro_field()
        order_page.choose_metro_station_mitino()
        order_page.set_input_phone_number(FirstSetOrderData.PHONE_NUMBER)
        order_page.continue_click_button()
        order_page.enter_delivery_date()
        order_page.choosing_rental_period_two_days()
        order_page.choosing_color_scooter_black()
        order_page.set_input_comment_for_courier(FirstSetOrderData.COMMENT_TO_COURIER)
        order_page.order_confirmation()

        assert order_page.order_confirmed()



