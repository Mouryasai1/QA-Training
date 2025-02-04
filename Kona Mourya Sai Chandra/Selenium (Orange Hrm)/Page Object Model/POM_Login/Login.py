import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

from utility.Basepage import Basepage


class Login(Basepage):
    username = (By.NAME, "username")
    password = (By.NAME, "password")
    submit = (By.CSS_SELECTOR, '.oxd-button')
    click = (By.CSS_SELECTOR, '.oxd-userdropdown-name')
    direct = (By.LINK_TEXT, "My Info")
    personal = (By.CSS_SELECTOR, "input[placeholder='First Name']")
    # ID = (By.XPATH,"(//*[@class='oxd-input oxd-input--active'])[2]")
    Nationality = (By.CLASS_NAME, "oxd-select-text oxd-select-text--active")
    Logout = (By.LINK_TEXT, "Logout")

    def __init__(self, driver):
        super().__init__(driver)

    def login(self, namevalue, pwdvalue):
        self.hrm_send_keys(self.username, namevalue)
        self.hrm_send_keys(self.password, pwdvalue)
        self.hrm_btn_click(self.submit)
    def logout(self):
        self.hrm_btn_click(self.click)
        self.hrm_btn_click(self.Logout)
        time.sleep(3)

    def get_title(self, title):
        self.hrm_get_title(title)
###login