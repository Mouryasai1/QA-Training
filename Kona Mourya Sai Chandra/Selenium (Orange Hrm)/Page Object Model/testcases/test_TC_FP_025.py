from selenium.webdriver.common.by import By

from POM_Login.Login import Login

import time
import pytest
class Test_TC_FP_019:
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
    def test_TC_FP_025(self):
        object=Login(self.driver)
        locator1=(By.XPATH, "(//input[@placeholder='Type for hints...'])[2]")
        object.hrm_send_keys(locator1,"9279218")
        time.sleep(3)
        locator2=(By.XPATH, "//*[@type='submit']")
        object.hrm_btn_click(locator2)
        time.sleep(5)