import time

from selenium.webdriver.common.by import By

from locators.mobileList_locators import MobileListLocators
class MobileListPage:
    def __init__(self,driver):
        self.driver=driver


    def enter_the_text_in_the_search_field_andClick(self, searchText):
        self.driver.find_element(*MobileListLocators.searchBtn).send_keys(searchText)
        time.sleep(1)
        self.driver.find_element(*MobileListLocators.clickSearchBtn).click()
        time.sleep(10)


    def getMobileName(self):
        print("i am going to getMobileName")
        mobile_list = self.driver.find_elements(*MobileListLocators.list_of_mobile_name)
        name_list = []
        # dict1={}
        for web_name in mobile_list:
            name_list.append(web_name.text)
        print(name_list)

        for name in name_list:
            price = self.driver.find_element(By.XPATH, f"//h2/a/span[text()='{name}']/../../../..//span[@class='a-price']").text
            print(f'mobile_name =  {name}' '\n', f"price = {price}", "\n", "----------------------------------------------------------" )
        #     dict1[name]=price
        # print(dict1)







