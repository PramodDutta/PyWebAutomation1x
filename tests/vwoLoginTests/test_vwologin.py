# Assertion here
import time

import allure
import pytest
from selenium import webdriver

from tests.pageObjects.loginPage import LoginPage


# Start the web
@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://app.vwo.com")
    return driver


@allure.epic("VWO Login Test")
@allure.feature("TC#0 - VWO App Negative Test")
def test_vwologin_negative(setup):
    driver = setup
    loginPage = LoginPage(driver)
    loginPage.login_to_vwo(user="admin", pwd="admin")
    time.sleep(5)
    error_message = loginPage.get_error_message_text()
    assert error_message == "Your email, password, IP address or location did not match"
    time.sleep(2)



@allure.epic("VWO Login Test")
@allure.feature("TC#1 - VWO App Positive Test")
def test_vwologin_positive(setup):
    driver = setup
    loginPage = LoginPage(driver)
    loginPage.login_to_vwo(user="contact+atb5x@thetestingacademy.com", pwd="ATBx@1234")
    time.sleep(5)
    assert "Dashboard" in driver.title
    time.sleep(2)
