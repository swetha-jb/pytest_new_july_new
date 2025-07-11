from selenium.webdriver.common.by import By


class LoginPageLocators:
    sign_in_btn = By.XPATH, "//a[@class='nav-action-signin-button']//parent::div[@id='nav-flyout-ya-signin']"  #"//a[@class='action-button']//span[text()='Sign in']"
    email_or_phone_input = By.XPATH, "//input[@id='ap_email']"
    continue_btn = By.ID, "continue"
    password_input = By.ID, "ap_password"
    signIn_Submit = By.ID, "signInSubmit"

