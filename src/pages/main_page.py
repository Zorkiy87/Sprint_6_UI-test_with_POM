import allure

from src.locators.base_page_locators import BasePageLocators
from src.locators.order_page_locators import OrderPageLocators
from src.pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Проверка ответов на основные вопросы на главной странице')
    def test_check_text_important_questions (self, driver, locator, question, answer):
        questions_page = MainPage(driver)
        questions_page.click_cookie()
        questions_page.scroll_to_element(locator)
        questions_page.click_element(locator)
        questions_page.wait_for_element_visible(question)
        description = questions_page.get_description(question)
        assert description == answer

    @allure.step('Нажатие на кнопку сервиса Самокат вверху страницы')
    def scooter_logo_button_click(self):
        self.click_element(BasePageLocators.SCOOTER_LOGO)

    @allure.step('Нажатие на кнопку Яндекса вверху страницы')
    def yandex_logo_button_click(self):
        self.click_element(BasePageLocators.YANDEX_LOGO)

    @allure.step('Нажатие на кнопку заказа вверху страницы')
    def header_click_order_button(self):
        self.click_element(OrderPageLocators.ORDER_BUTTON_HEADER)

