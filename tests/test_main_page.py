import allure
import src.config

from src.pages.main_page import MainPage

class TestImportantQuestions:

    @allure.title('Проверка ответа на вопрос: сколько стоит?')
    def test_check_text_important_questions_how_much(self, driver):
        main_page = MainPage(driver)
        question_locator, answer_locator, expected_answer  = main_page.get_how_much_locators()
        main_page.verify_question_answer(question_locator, answer_locator, expected_answer)

    @allure.title('Проверка ответа на вопрос: хочу несколько самокатов?')
    def test_check_text_important_questions_multiple_scooters(self,driver):
        main_page = MainPage(driver)
        question_locator, answer_locator, expected_answer = main_page.get_multiple_scooters_locators()
        main_page.verify_question_answer(question_locator, answer_locator, expected_answer)

    @allure.title('Проверка ответа на вопрос: как считается время аренды?')
    def test_check_text_important_questions_rental_time_calculated(self, driver):
        main_page = MainPage(driver)
        question_locator, answer_locator, expected_answer = main_page.get_rental_time_calculated_locators()
        main_page.verify_question_answer(question_locator, answer_locator, expected_answer)

    @allure.title('Проверка ответа на вопрос: можно заказать самокат на сегодня?')
    def test_check_text_important_questions_order_scooter_today(self, driver):
        main_page = MainPage(driver)
        question_locator, answer_locator, expected_answer = main_page.get_order_scooter_today_locators()
        main_page.verify_question_answer(question_locator, answer_locator, expected_answer)

    @allure.title('Проверка ответа на вопрос: можно продлить самокат?')
    def test_check_text_important_questions_extend_order(self, driver):
        main_page = MainPage(driver)
        question_locator, answer_locator, expected_answer = main_page.get_extend_order_locators()
        main_page.verify_question_answer(question_locator, answer_locator, expected_answer)

    @allure.title('Проверка ответа на вопрос: вы привозите зарядку с самокатом?')
    def test_check_text_important_questions_charging_for_a_scooter(self, driver):
        main_page = MainPage(driver)
        question_locator, answer_locator, expected_answer = main_page.get_charging_for_a_scooter_locators()
        main_page.verify_question_answer(question_locator, answer_locator, expected_answer)

    @allure.title('Проверка ответа на вопрос: можно отменить заказ?')
    def test_check_text_important_questions_cancel_the_order(self, driver):
        main_page = MainPage(driver)
        question_locator, answer_locator, expected_answer = main_page.get_cancel_the_order_locators()
        main_page.verify_question_answer(question_locator, answer_locator, expected_answer)

    @allure.title('Проверка ответа на вопрос: привозите за МКАД?')
    def test_check_text_important_questions_i_live_across_the_mkad(self, driver):
        main_page = MainPage(driver)
        question_locator, answer_locator, expected_answer = main_page.get_i_live_across_the_mkad_locators()
        main_page.verify_question_answer(question_locator, answer_locator, expected_answer)

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






