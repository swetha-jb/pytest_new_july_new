from selenium.webdriver.common.by import By


class   MobileListLocators:
    searchBtn = By.XPATH,"//*[@type='text' or @id='twotabsearchtextbox']"
    clickSearchBtn=By.XPATH,"//button[@type='submit']"
    list_of_mobile_name = By.XPATH, '//div[@class="col col-7-12"]/div[@class="_4rR01T"]'


