import allure

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from src.locators.base_page_locators import BasePageLocators



class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    @allure.step('Поиск элемента по локатору')
    def find_element(self, locator, timeout =10):
        with allure.step(f"Поиск элемента по локатору{locator}"):
            return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    @allure.step('Поиск элемента по локатору и клик по нему')
    def click_element(self, locator, timeout=10):
        with allure.step(f"Клик по найденному элементу {locator}"):
            self.find_element(locator, timeout).click()

    @allure.step('Получение текстового значения по найденному элементу')
    def get_description(self, locator):
        with allure.step(f"Получение текстового значения по найденному элементу {locator}"):
            return self.find_element(locator).text

    @allure.step('Пролистывание до нужного элемента')
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def wait_for_element_visible(self, locator, timeout=10):
        with allure.step(f"Ожидание видимости элемента {locator}"):
            return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step('Нажатие на кнопку Принять Куки')
    def click_cookie(self):
        self.click_element(BasePageLocators.ACCEPT_COOKIE)

    @allure.step('Запрашиваем URL текущей страницы')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Переключение на последнюю открытую страницу')
    def switch_page(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step('Ожидание появления заголовка на странице')
    def wait_for_title_is_dzen(self):
        WebDriverWait(self.driver, 10).until(EC.title_contains("Дзен"))



