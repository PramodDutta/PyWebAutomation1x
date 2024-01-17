import time

import allure
import pytest
from tests.pageObjects.loginPage import LoginPage


#Login - 1 Positive, 1 Negative, 2 more Negative, Start Trail, Remember is checked,
# 15+ Testcase - P0 - 2-3(P0)

class TestLogin():

    @allure.epic("VWO Login Test")
    @allure.feature("TC#0 - VWO App Negative Test")
    @pytest.mark.usefixtures("setup")
    @pytest.mark.smoke
    def test_vwo_login_negative(self, setup):
        driver = setup
        driver.get(self.base_url)
        loginPage = LoginPage(driver)
        loginPage.login_to_vwo(user="admin", pwd="admin")
        time.sleep(5)
        error_message = loginPage.get_error_message_text()
        assert error_message == "Your email, password, IP address or location did not match"
        time.sleep(2)

    @allure.epic("VWO Login Test")
    @allure.feature("TC#1 - VWO App Positive Test")
    @pytest.mark.usefixtures("setup")
    def test_vwo_login_positive(self, setup):
        driver = setup
        driver.get(self.base_url)
        loginPage = LoginPage(driver)
        loginPage.login_to_vwo(user=self.username, pwd=self.password)
        time.sleep(5)
        assert "Dashboard" in driver.title
        time.sleep(2)


