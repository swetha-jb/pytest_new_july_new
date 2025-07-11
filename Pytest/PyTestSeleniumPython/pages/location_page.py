import time

from locators.location_page_locators import LocationPageLocators
import time


class LocationPage:

    def __init__(self, driver):
        self.driver = driver

    def click_on_the_location(self):
        self.driver.find_element(*LocationPageLocators.locationID).click()
        time.sleep(2)

    def Enter_the_pin_code(self, PIN):
        self.driver.find_element(*LocationPageLocators.pincodeID).send_keys(PIN)

    def Click_on_apply_btn(self):
        self.driver.find_element(*LocationPageLocators.applyID).click()
        time.sleep(3)