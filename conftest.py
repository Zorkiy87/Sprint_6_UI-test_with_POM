import pytest
from selenium import webdriver
from src.config import URL



@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(URL)
    yield driver
    driver.quit()