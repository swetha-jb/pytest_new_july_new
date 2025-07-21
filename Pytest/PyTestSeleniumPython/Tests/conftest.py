import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(autouse=True, scope='class')
def driver_setup(request):
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Comment this line if you want a visible browser
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Set up Chrome using Service and webdriver-manager
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Launch URL
    driver.get('https://www.flipkart.com/search?q=mobiles&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_1_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_1_0_na_na_na&as-pos=1&as-type=HISTORY&suggestionId=mobiles&requestId=7609e629-7334-4126-900e-366c621f426d')
    driver.implicitly_wait(5)
    driver.maximize_window()
    time.sleep(1)

    request.cls.driver = driver
    yield
    driver.quit()

