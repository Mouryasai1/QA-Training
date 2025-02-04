from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

from POM_Login.Login import Login

import time
import pytest
class Test_TC_FP_016:
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
        locator2 = (By.LINK_TEXT, "Assign Claim")
        object.hrm_btn_click(locator2)
        time.sleep(2)
    def test_TC_FP_026(self,setup):
        object=Login(self.driver)
        locator2 = (By.CSS_SELECTOR, "[placeholder='Type for hints...']")
        text2 = "Jo"
        object.hrm_send_keys(locator2, text2)
        locator=(By.XPATH,"//div[@class='oxd-autocomplete-option'][3]")
        object.hrm_btn_click(locator)
        locator3=(By.XPATH,"(//div[@class='oxd-select-text-input'])")
        object.hrm_btn_click(locator3)
        locator4=(By.XPATH,"(//div[@class='oxd-select-option'][3])")
        object.hrm_btn_click(locator4)
        locator5=(By.XPATH,"(//div[@class='oxd-select-text-input'])[2]")
        object.hrm_btn_click(locator5)
        locator6=(By.XPATH,"(//div[@class='oxd-select-option'])[3]")
        object.hrm_btn_click(locator6)
        locator10 = (By.XPATH, "(//button[@type='submit'])")
        object.hrm_btn_click(locator10)
        time.sleep(5)