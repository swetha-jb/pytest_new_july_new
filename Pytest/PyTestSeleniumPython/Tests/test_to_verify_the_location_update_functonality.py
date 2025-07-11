from pages.location_page import LocationPage
import pytest


@pytest.mark.usefixtures('driver_setup')
class TestLocation:
    def __init__(self):
        self.driver = None

    def test_to_verify_that_update_location_is_working(self):
        Location_Page_driver = LocationPage(self.driver)
        Location_Page_driver.click_on_the_location()
        Location_Page_driver.Enter_the_pin_code(PIN="201301")
        Location_Page_driver.Click_on_apply_btn()
