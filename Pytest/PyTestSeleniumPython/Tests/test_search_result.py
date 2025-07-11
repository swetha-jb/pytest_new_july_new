import time

import pytest
from pages.MobileLIst_page import MobileListPage

@pytest.mark.usefixtures('driver_setup')
class TestMobileList:
    def test_to_verify_the_searchFunctionality(self):
        MobileListPage_driver=MobileListPage(self.driver)
        MobileListPage_driver.enter_the_text_in_the_search_field_andClick("")
        MobileListPage_driver.getMobileName()




