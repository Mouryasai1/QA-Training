from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

from POM_Login.Login import Login

import time
import pytest
class Test_TC_FP_031:
    def __int__(self,driver):
        self.driver=driver

    def test_login(self, setup):
        object = Login(self.driver)
        object.login("Admin", "admin123")
        time.sleep(2)
        object = Login(self.driver)
        locator = (By.LINK_TEXT, "Claim")
        object.hrm_btn_click(locator)
        time.sleep(2)
        locator2 = (By.LINK_TEXT, "Submit Claim")
        object.hrm_btn_click(locator2)
        time.sleep(2)
    def test_TC_FP_33(self):
        object=Login(self.driver)
        locator7 = (By.XPATH, "//textarea[@class='oxd-textarea oxd-textarea--active oxd-textarea--resize-vertical']")
        object.hrm_send_keys(locator7, "Good Attitude")
        time.sleep(2)
        locator10 = (By.XPATH, "(//button[@type='submit'])")
        object.hrm_btn_click(locator10)
        time.sleep(5)