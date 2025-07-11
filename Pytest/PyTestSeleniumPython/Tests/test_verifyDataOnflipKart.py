import time

import pytest
from pages.flipKart import FlipkartPage


@pytest.mark.usefixtures('driver_setup')
class TestFlipKart:
    driver = None

    def test_to_verify_the_Login_page(self):
        flipkart_page = FlipkartPage(self.driver)
        time.sleep(1)
        flipkart_page.move_to_element()
        time.sleep(3)
        flipkart_page.mobile_list()
        # flipkart_page.close_login_pan()
        # time.sleep(2)
        #
        # time.sleep(2000)

    #     flipkart_page.Enter_the_mobile_number(8800511094)
    #
    #     flipkart_page.click_on_request_otp_btn()
    #     time.sleep(100)


        # flipkart_page.close_login_pan()

        # flipkart_page.click_on_verify_otp_btn()
        # time.sleep(2)









