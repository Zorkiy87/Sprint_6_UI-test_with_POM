import allure

from src.locators.base_page_locators import BasePageLocators
from src.locators.order_page_locators import OrderPageLocators
from src.pages.base_page import BasePage
from src.locators.main_page_locators import QuestionsLocators
from data import Answers


class MainPage(BasePage):

    @allure.step('Нажатие на кнопку сервиса Самокат вверху страницы')
    def scooter_logo_button_click(self):
        self.click_element(BasePageLocators.SCOOTER_LOGO)

    @allure.step('Нажатие на кнопку Яндекса вверху страницы')
    def yandex_logo_button_click(self):
        self.click_element(BasePageLocators.YANDEX_LOGO)

    @allure.step('Нажатие на кнопку заказа вверху страницы')
    def header_click_order_button(self):
        self.click_element(OrderPageLocators.ORDER_BUTTON_HEADER)

    @allure.step('Нажатие на кнопку Принять Куки')
    def click_cookie(self):
        self.click_element(BasePageLocators.ACCEPT_COOKIE)

    @allure.step('Получение локаторов и данных для вопроса: сколько стоит? ')
    def get_how_much_locators(self):
        locator = QuestionsLocators.HOW_MUCH
        question = QuestionsLocators.HOW_MUCH_TEXT
        answer = Answers.HOW_MUCH_ANSWER
        return locator, question, answer

    @allure.step('Получение локаторов и данных для вопроса: хочу несколько самокатов? ')
    def get_multiple_scooters_locators(self):
        locator = QuestionsLocators.MULTIPLE_SCOOTERS
        question = QuestionsLocators.MULTIPLE_SCOOTERS_TEXT
        answer = Answers.MULTIPLE_SCOOTERS_ANSWER
        return locator, question, answer

    @allure.step('Получение локаторов и данных для вопроса: как считается время аренды?  ')
    def get_rental_time_calculated_locators(self):
        locator = QuestionsLocators.RENTAL_TIME_CALCULATED
        question = QuestionsLocators.RENTAL_TIME_CALCULATED_TEXT
        answer = Answers.RENTAL_TIME_CALCULATED_ANSWER
        return locator, question, answer

    @allure.step('Получение локаторов и данных для вопроса: можно заказать самокат на сегодня? ')
    def get_order_scooter_today_locators(self):
        locator = QuestionsLocators.ORDER_SCOOTER_TODAY
        question = QuestionsLocators.ORDER_SCOOTER_TODAY_TEXT
        answer = Answers.ORDER_SCOOTER_TODAY_ANSWER
        return locator, question, answer

    @allure.step('Получение локаторов и данных для вопроса: можно продлить самокат? ')
    def get_extend_order_locators(self):
        locator = QuestionsLocators.EXTEND_THE_ORDER
        question = QuestionsLocators.EXTEND_THE_ORDER_TEXT
        answer = Answers.EXTEND_THE_ORDER_ANSWER
        return locator, question, answer

    @allure.step('Получение локаторов и данных для вопроса: вы привозите зарядку с самокатом?')
    def get_charging_for_a_scooter_locators(self):
        locator = QuestionsLocators.CHARGING_FOR_A_SCOOTER
        question = QuestionsLocators.CHARGING_FOR_A_SCOOTER_TEXT
        answer = Answers.CHARGING_FOR_A_SCOOTER_ANSWER
        return locator, question, answer

    @allure.step('Получение локаторов и данных для вопроса: можно отменить заказ? ')
    def get_cancel_the_order_locators(self):
        locator = QuestionsLocators.CANCEL_THE_ORDER
        question = QuestionsLocators.CANCEL_THE_ORDER_TEXT
        answer = Answers.CANCEL_THE_ORDER_ANSWER
        return locator, question, answer

    @allure.step('Получение локаторов и данных для вопроса: привозите за МКАД? ')
    def get_i_live_across_the_mkad_locators(self):
        locator = QuestionsLocators.I_LIVE_ACROSS_THE_MKAD
        question = QuestionsLocators.I_LIVE_ACROSS_THE_MKAD_TEXT
        answer = Answers.I_LIVE_ACROSS_THE_MKAD_ANSWER
        return locator, question, answer

    @allure.step('Проверка ответов на основные вопросы на главной странице')
    def verify_question_answer(self, question_locator, answer_locator, expected_answer):
        self.click_cookie()
        self.scroll_to_element(question_locator)
        self.click_element(question_locator)
        self.wait_for_element_visible(answer_locator)
        actual_answer = self.get_description(answer_locator)
        assert actual_answer == expected_answer, f"Ожидался ответ: '{expected_answer}', но получен '{actual_answer}'"



