from selenium.webdriver.common.by import By

from POM_Login.Login import Login

import time
import pytest
class Test_TC_FP_01:
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
    def test_TC_FP_01(self):
        object=Login(self.driver)
        locator1=(By.LINK_TEXT, "Employee Claims")
        object.hrm_btn_click(locator1)
        time.sleep(4)

        locator2=(By.CSS_SELECTOR, "[placeholder='Type for hints...']")
        text2="FNCypressTest Jacke1 LNCypressTest"
        object.hrm_send_keys(locator2,text2)

        time.sleep(2)

        locator3=(By.XPATH, "(//input[@placeholder='Type for hints...'])[2]")
        text3="202307180000003"
        object.hrm_send_keys(locator3,text3)
        time.sleep(2)

        locator4=(By.XPATH, "(//div[contains(text(),'-- Select --')])[1]")
        object.hrm_btn_click(locator4)
        time.sleep(2)

        locator5=(By.XPATH, "//span[text()='Travel Allowance']")
        object.hrm_btn_click(locator5)
        time.sleep(4)

        locator6=(By.XPATH, "(//div[@class='oxd-select-text-input'])[2]")
        object.hrm_btn_click(locator6)

        locator7=(By.XPATH, "//span[text()='Approved']")
        object.hrm_btn_click(locator7)
        time.sleep(4)



        # locator9=(By.XPATH, "(//input[@placeholder='yyyy-dd-mm'])[1]")
        # object.hrm_btn_click(locator9)
        # time.sleep(2)
        # current_date = datetime.now()
        # next_date = current_date + timedelta(days=1)  # current date + 1
        # formatted_date = next_date.strftime("%Y-%d-%m")
        # driver.find_element(By.XPATH, "(//*[@placeholder='yyyy-dd-mm'])[1]").send_keys(formatted_date + Keys.TAB)
        #  #Keys.TAB clicks the tab key
        # time.sleep(5)



        locator8=(By.XPATH, "(//div[contains(text(),'Current Employees Only')])[1]")
        object.hrm_btn_click(locator8)
        time.sleep(2)

        locator9=(By.XPATH, "//span[text()='Current Employees Only']")
        object.hrm_btn_click(locator9)
        time.sleep(4)

        locator10=(By.XPATH, "//button[normalize-space()='Search']")
        object.hrm_btn_click(locator10)
        time.sleep(5)

        # data1 = driver.find_element(By.TAG_NAME, "h6").text
        # time.sleep(2)
        # data2 = driver.find_element(By.LINK_TEXT, "PIM").text
        # assert data1 == data2
        #
        # links = driver.find_elements(By.TAG_NAME, 'a')
        # print(len(links))
        #
        # button = driver.find_element(By.CSS_SELECTOR, '.oxd-userdropdown').click()
        # time.sleep(4)
        # driver.find_element(By.LINK_TEXT, "Logout").click()
