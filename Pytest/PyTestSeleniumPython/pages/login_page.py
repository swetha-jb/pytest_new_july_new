from locators.login_page_locators import LoginPageLocators
import time


class LoginPage:

    def __init__(self, driver):  # constructor
        self.driver = driver

    def opening_the_login_page(self):
        self.driver.find_element(*LoginPageLocators.sign_in_btn).click()
        time.sleep(2)

    def enter_the_email_or_mobile_number(self, email_or_mobile):
        self.driver.find_element(*LoginPageLocators.email_or_phone_input).send_keys(email_or_mobile)

    def click_on_continue_btn(self):
        self.driver.find_element(*LoginPageLocators.continue_btn).click()
        time.sleep(2)

    def enter_the_password(self, password):
        self.driver.find_element(*LoginPageLocators.password_input).send_keys(password)

    def click_on_sign_in_submit_btn(self):
        self.driver.find_element(*LoginPageLocators.signIn_Submit).click()
        time.sleep(3)
