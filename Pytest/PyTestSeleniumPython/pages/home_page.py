from locators.home_page_locators import HomePageLocators


class HomePage:

    def __init__(self, driver):
        self.driver = driver
    def close_the_signIn_btn(self):
        self.driver.find_element(*HomePageLocators.LoginCloseXpath).click()
    def enter_the_value_in_search_box(self, search_text):
        self.driver.find_element(*HomePageLocators.search_input).clear()
        self.driver.find_element(*HomePageLocators.search_input).send_keys(search_text)

    def click_on_search_button_and_click_on_laptop(self):
        self.driver.find_element(*HomePageLocators.search_button).click()
        self.driver.find_element(*HomePageLocators.laptopsXpath).click()
    def click_on_the_Buy(self):
        self.driver.find_element(*HomePageLocators.BuyXpath).click()
    def print_verify_text(self):
        text = self.driver.find_element(*HomePageLocators.VerifyBuyXpath).text
        return text
    def print_return_on_previous_page_verification_text(self):
        text = self.driver.find_element(*HomePageLocators.laptopsXpath).text
        return text


    # def click_on_add_to_cartButton(self):
    #     self.driver.find_element(*HomePageLocators.add_to_cart).click()
    #
    # def adding_items_in_cart(self, count):
    #     loop_count = 0
    #     list_of_elements = self.driver.find_elements(*HomePageLocators.laptopsXpath)
    #     window_before = self.driver.window_handles[0]
    #     for item in list_of_elements:
    #         item.click()
    #         self.click_on_add_to_cartButton()
    #         window_after = self.driver.window_handles[1]
    #         self.driver.switch_to.window(window_after)
    #         self.driver.close()
    #         self.driver.switch_to.window(window_before)
    #         self.driver.back()
    #         self.driver.back()
    #         loop_count+=1
    #         if loop_count == count:
    #             break
    # def window_handle1(self):
    #     window_before = self.driver.window_handles[0]
    #     return window_before


    def window_handle2(self):
        window_after = self.driver.window_handles[1]
        return window_after
    def my_don(self):
        pass




