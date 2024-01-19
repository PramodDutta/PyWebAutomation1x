import time

import allure
import pytest
from tests.pageObjects.katalonHomePage import KatalonHomePage


class TestLogin():

    @allure.epic("Katalon Home page")
    @allure.feature("TC#0 - Katalon Home Page")
    @pytest.mark.usefixtures("setup")
    def test_katalon_login(self, setup):
        driver = setup
        # Use the Excel here
        driver.get(self.katalon_url)
        khp = KatalonHomePage(driver)
        khp.click_homepage()
        assert "profile.php#login" in driver.current_url
        time.sleep(2)


