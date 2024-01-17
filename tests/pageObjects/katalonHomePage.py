# Page Class
import time

# Page Locators
# Page Actions
# Webdriver - Init
# Custom Functions
# No Assertion here

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class KatalonHomePage():

    def __init__(self, driver):
        self.driver = driver

    # Page Locators
    make_appointment = (By.ID, "btn-make-appointment")

    # Return a WebElement ->  username
    def get_make_appointment(self):
        return self.driver.find_element(*KatalonHomePage.make_appointment)

    # Page Actions

    def click_homepage(self):
        time.sleep(3)
        self.get_make_appointment().click()
