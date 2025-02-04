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
    def test_FP_019(self):
        object=Login(self.driver)
        locator1=(By.XPATH, "(//div[@class='oxd-select-text--after'])[2]")
        object.hrm_btn_click(locator1)
        time.sleep(2)
        locator2=(By.XPATH, "(//div[@class='oxd-select-option'])[3]")
        object.hrm_btn_click(locator2)
        time.sleep(2)
        locator3=(By.XPATH,"(//button[@class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space'])")
        object.hrm_btn_click(locator3)
        time.sleep(5)