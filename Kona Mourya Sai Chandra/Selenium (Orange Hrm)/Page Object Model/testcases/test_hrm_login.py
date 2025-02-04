import time

import pytest
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

from POM_Login.Login import Login

@pytest.mark.usefixtures("setup")
class Test_Login:
    def __int__(self,driver):
        self.driver=driver

    def test_login(self, setup):
        object = Login(self.driver)
        object.login("Admin", "admin123")
        time.sleep(5)
    def test_TC_FP012(self):
        object = Login(self.driver)
        locator=(By.LINK_TEXT,"Claim")
        object.hrm_btn_click(locator)
        time.sleep(2)
        locator2=(By.CSS_SELECTOR, "[placeholder='Type for hints...']")
        text2="Peter Mac Anderson"
        object.hrm_send_keys(locator2,text2)
        time.sleep(2)
        locator3=((By.XPATH, "//*[@type='submit']"))
        object.hrm_btn_click(locator3)
        time.sleep(5)
    def test_TC_FP013(self):
        object=Login(self.driver)
        locator1=(By.XPATH, "(//input[@placeholder='Type for hints...'])[2]")
        text1="111"
        object.hrm_send_keys(locator1,text1)
        time.sleep(2)
        locator2=(By.XPATH, "//*[@type='submit']")
        object.hrm_btn_click(locator2)
        time.sleep(5)
    #this is not working
    # def test_TC_FP_014(self):
    #     object=Login(self.driver)
    #     locator1= (By.XPATH, "(//input[@placeholder='Type for hints...'])[2]")
    #     object.hrm_btn_click(locator1)
    #     time.sleep(2)
    #     action = ActionChains(self.driver)
    #     action.click().perform()
    #     time.sleep(2)
    #     action.send_keys("1")
    #     action.send_keys(Keys.DOWN).click().perform()
    #     time.sleep(2)
    #     action.send_keys(Keys.ARROW_DOWN)
    #     time.sleep(2)
    #     action.send_keys(Keys.ENTER).perform()
    #     time.sleep(2)
    #     locator2=(By.XPATH, "//*[@type='submit']")
    #     object.hrm_btn_click(locator2)
    #     time.sleep(5)
    def test_TC_FP_015(self):
        object=Login(self.driver)
        locator1=(By.XPATH, "(//div[@class='oxd-select-text--after'])[2]")
        object.hrm_btn_click(locator1)
        time.sleep(2)
        locator2=(By.XPATH, "(//div[@class='oxd-select-option'])[4]")
        object.hrm_btn_click(locator2)
        time.sleep(2)
        locator3=(By.XPATH,"(//button[@class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space'])")
        object.hrm_btn_click(locator3)
        locator4 = (By.XPATH, "//*[@type='submit']")
        object.hrm_btn_click(locator4)
        time.sleep(5)
        time.sleep(5)




