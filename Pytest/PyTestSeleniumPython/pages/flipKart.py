import time

from locators.flipkartLocators import FlipKartLocators

# from locators.home_page_locators import HomePageLocators

from selenium.webdriver.common.action_chains import ActionChains

class FlipkartPage:

    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(driver)

    def move_to_element(self):
        element=self.driver.find_element(*FlipKartLocators.electronics_xpath)
        self.action.move_to_element(element).perform()
        time.sleep(4)
    def mobile_list(self):
        mobiles=self.driver.find_elements(*FlipKartLocators.MobileList_Xpath)
        mobile_name_list=[]
        for item in mobiles:
            mobile_name_list.append(item.text)
        print(mobile_name_list)
    # def close_login_pan(self):
    #     self.driver.find_element(*FlipKartLocators.closeLogin_Xpath).click()

    # def Click_On_Login_btn(self):
    #     self.driver.find_element(*FlipKartLocators.loginXpath).click()
    #
    # def Enter_the_mobile_number(self, MobileNumber):
    #     self.driver.find_element(*FlipKartLocators.MobileNumber_Xpath).send_keys(MobileNumber)
    #
    # def click_on_request_otp_btn(self):
    #     self.driver.find_element(*FlipKartLocators.requestOTP_xpath).click()




    # def click_on_verify_otp_btn(self):
    #     self.driver.find_element(*FlipKartLocators.verifyOTP_xpath).click()

