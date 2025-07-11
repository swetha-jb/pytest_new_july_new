import time
'''
selenium==4.8.3
webdrive-manage==3.7.1
pytest==7.3.2
'''

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(autouse=True, scope='class')
def driver_setup(request):
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    # login url (To execute login functionality uncomment this below url)
    # driver.get("https://www.amazon.in/ap/signin?openid.pape.max_auth_age=900&openid.return_to=https%3A%2F%2Fwww.amazon.in%2Fgp%2Fyourstore%2Fhome%3Fpath%3D%252Fgp%252Fyourstore%252Fhome%26useRedirectOnSuccess%3D1%26signIn%3D1%26action%3Dsign-out%26ref_%3Dnav_AccountFlyout_signout&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")
    # search url
    # driver.get("https://www.amazon.in/")
    driver.get('https://www.flipkart.com/search?q=mobiles&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_1_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_1_0_na_na_na&as-pos=1&as-type=HISTORY&suggestionId=mobiles&requestId=7609e629-7334-4126-900e-366c621f426d')
    driver.implicitly_wait(5)
    driver.maximize_window()
    time.sleep(1)
    request.cls.driver = driver #sending driver to the class level
    yield
    driver.quit()
