import allure
import src.config

from conftest import driver
from src.locators.main_page_locators import QuestionsLocators
from data import Answers
from src.pages.main_page import MainPage


class TestImportantQuestions:

    @allure.title('Проверка ответа на вопрос: сколько стоит?')
    def test_check_text_important_questions_how_much(self, driver):
        main_page = MainPage(driver)
        locator = QuestionsLocators.HOW_MUCH
        question = QuestionsLocators.HOW_MUCH_TEXT
        answer = Answers.HOW_MUCH_ANSWER
        main_page.test_check_text_important_questions(driver, locator, question, answer)

    @allure.title('Проверка ответа на вопрос: хочу несколько самокатов?')
    def test_check_text_important_questions_multiple_scooters(self,driver):
        main_page = MainPage(driver)
        locator = QuestionsLocators.MULTIPLE_SCOOTERS
        question = QuestionsLocators.MULTIPLE_SCOOTERS_TEXT
        answer = Answers.MULTIPLE_SCOOTERS_ANSWER
        main_page.test_check_text_important_questions(driver, locator, question, answer)

    @allure.title('Проверка ответа на вопрос: как считается время аренды?')
    def test_check_text_important_questions_rental_time_calculated(self, driver):
        main_page = MainPage(driver)
        locator = QuestionsLocators.RENTAL_TIME_CALCULATED
        question = QuestionsLocators.RENTAL_TIME_CALCULATED_TEXT
        answer = Answers.RENTAL_TIME_CALCULATED_ANSWER
        main_page.test_check_text_important_questions(driver, locator, question, answer)

    @allure.title('Проверка ответа на вопрос: можно заказать самокат на сегодня?')
    def test_check_text_important_questions_order_scooter_today(self, driver):
        main_page = MainPage(driver)
        locator = QuestionsLocators.ORDER_SCOOTER_TODAY
        question = QuestionsLocators.ORDER_SCOOTER_TODAY_TEXT
        answer = Answers.ORDER_SCOOTER_TODAY_ANSWER
        main_page.test_check_text_important_questions(driver, locator, question, answer)

    @allure.title('Проверка ответа на вопрос: можно продлить самокат?')
    def test_check_text_important_questions_extend_order(self, driver):
        main_page = MainPage(driver)
        locator = QuestionsLocators.EXTEND_THE_ORDER
        question = QuestionsLocators.EXTEND_THE_ORDER_TEXT
        answer = Answers.EXTEND_THE_ORDER_ANSWER
        main_page.test_check_text_important_questions(driver, locator, question, answer)

    @allure.title('Проверка ответа на вопрос: вы привозите зарядку с самокатом?')
    def test_check_text_important_questions_charging_for_a_scooter(self, driver):
        main_page = MainPage(driver)
        locator = QuestionsLocators.CHARGING_FOR_A_SCOOTER
        question = QuestionsLocators.CHARGING_FOR_A_SCOOTER_TEXT
        answer = Answers.CHARGING_FOR_A_SCOOTER_ANSWER
        main_page.test_check_text_important_questions(driver, locator, question, answer)

    @allure.title('Проверка ответа на вопрос: можно отменить заказ?')
    def test_check_text_important_questions_cancel_the_order(self, driver):
        main_page = MainPage(driver)
        locator = QuestionsLocators.CANCEL_THE_ORDER
        question = QuestionsLocators.CANCEL_THE_ORDER_TEXT
        answer = Answers.CANCEL_THE_ORDER_ANSWER
        main_page.test_check_text_important_questions(driver, locator, question, answer)

    @allure.title('Проверка ответа на вопрос: привозите за МКАД?')
    def test_check_text_important_questions_i_live_across_the_mkad(self, driver):
        main_page = MainPage(driver)
        locator = QuestionsLocators.I_LIVE_ACROSS_THE_MKAD
        question = QuestionsLocators.I_LIVE_ACROSS_THE_MKAD_TEXT
        answer = Answers.I_LIVE_ACROSS_THE_MKAD_ANSWER
        main_page.test_check_text_important_questions(driver, locator, question, answer)

class TestMainPageSwitchingPage:

    @allure.title('Проверка перехода по лого самокат')
    def test_switching_page_scooter_logo(self,driver):
        main_page = MainPage(driver)
        main_page.header_click_order_button()
        main_page.scooter_logo_button_click()
        assert main_page.get_current_url() == src.config.URL

    @allure.title('Проверка перехода по лого Яндекс')
    def test_switching_page_yandex(self, driver):
        main_page = MainPage(driver)
        main_page.yandex_logo_button_click()
        main_page.switch_page()
        main_page.wait_for_title_is_dzen()
        assert '/dzen' in main_page.get_current_url()






