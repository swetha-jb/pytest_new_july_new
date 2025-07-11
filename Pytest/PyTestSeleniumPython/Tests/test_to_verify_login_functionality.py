import time

import pytest
from pages.login_page import LoginPage


@pytest.mark.usefixtures('driver_setup')
class TestLogin:

    def test_verify_login_functionality_is_working(self):
        Login_Page_Driver = LoginPage(self.driver)
        Login_Page_Driver.opening_the_login_page()
        Login_Page_Driver.enter_the_email_or_mobile_number(email_or_mobile="8800511094")
        Login_Page_Driver.click_on_continue_btn()
        Login_Page_Driver.enter_the_password(password="Amazon@123")
        Login_Page_Driver.click_on_sign_in_submit_btn()
        time.sleep(120)

