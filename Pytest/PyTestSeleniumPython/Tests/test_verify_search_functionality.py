import time

import pytest
from pages.home_page import HomePage


@pytest.mark.usefixtures('driver_setup')
class TestSearch:
    driver = None

    # def test_verify_search_functionality_is_working(self):
    #     Home_Page_Driver = HomePage(self.driver)
    #
    #     Home_Page_Driver.enter_the_value_in_search_box("Iphone")
    #     Home_Page_Driver.click_on_search_button()

    def test_verify_search_functionality2_is_working(self):
        Home_Page_Driver = HomePage(self.driver)
        time.sleep(2)
        Home_Page_Driver.close_the_signIn_btn()
        Home_Page_Driver.enter_the_value_in_search_box("laptops")
        window_before = self.driver.window_handles[0]
        Home_Page_Driver.click_on_search_button_and_click_on_laptop()
        window_after = self.driver.window_handles[1]
        time.sleep(1)
        self.driver.switch_to.window(window_after)
        Home_Page_Driver.click_on_the_Buy()
        time.sleep(2)
        print(Home_Page_Driver.print_verify_text())
        self.driver.close()
        time.sleep(2)
        self.driver.switch_to.window(window_before)
        print(Home_Page_Driver.print_return_on_previous_page_verification_text())
        time.sleep(1)


        # Home_Page_Driver.adding_items_in_cart(2)






