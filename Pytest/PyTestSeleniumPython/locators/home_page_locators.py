from selenium.webdriver.common.by import By


class HomePageLocators:
    search_input = By.XPATH, '//input[@type="text"]'
    search_button = By.XPATH, '//button[@type="submit"]'
    laptopsXpath=By.XPATH,'(//div[@class="_4rR01T"])[1]'
    LoginCloseXpath=By.XPATH,'//span[@role="button"]'
    # add_to_cart = By.ID, 'add-to-cart-button'
    BuyXpath=By.XPATH,'//button[@class="_2KpZ6l _2U9uOA ihZ75k _3AWRsL"]'
    VerifyBuyXpath=By.XPATH,'//button[@class="_2KpZ6l _20xBvF _3AWRsL"]'