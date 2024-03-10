import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from config.action import SeleniumAction


@pytest.fixture
def browser():
    current_dir = r"C:\Users\ninal\PycharmProjects\PythonProjectGit\config"
    gecko_path = r"C:\Users\ninal\PycharmProjects\PythonProjectGit\config\geckodriver.exe"
    web_service = Service(gecko_path)
    driver = webdriver.Firefox(service=web_service)
    yield driver
    driver.quit()


@pytest.fixture
def selenium_action(browser):
    selenium_action = SeleniumAction(browser)
    yield selenium_action
