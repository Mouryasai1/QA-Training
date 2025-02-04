import datetime

import pytest
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
import time

class TestEmployeeClaims:

    @staticmethod
    def login(browser, username="Admin", password="admin123"):
        """
        Helper method to log in to the application.
        """
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(7)
        browser.find_element(By.NAME, "username").send_keys(username)
        time.sleep(7)
        browser.find_element(By.NAME, "password").send_keys(password)
        time.sleep(7)
        browser.find_element(By.CSS_SELECTOR, ".oxd-button").click()
        time.sleep(7)

    @staticmethod
    def navigate_to_AssignClaims(browser):

        browser.find_element(By.LINK_TEXT, "Claim").click()
        time.sleep(7)
        browser.find_element(By.LINK_TEXT, "Assign Claim").click()
        time.sleep(7)

    def test_tc1(self, browser):

        self.login(browser)
        self.navigate_to_AssignClaims(browser)

        try:
            browser.find_element(By.CSS_SELECTOR, "[placeholder='Type for hints...']").send_keys("Jo")
            time.sleep(7)
            browser.find_element(By.XPATH, "//div[@class='oxd-autocomplete-option'][3]").click()
            time.sleep(7)
            browser.find_element(By.XPATH, "(//div[@class='oxd-select-text-input'])").click()
            time.sleep(7)
            browser.find_element(By.XPATH, "(//div[@class='oxd-select-option'][3])").click()
            time.sleep(7)
            browser.find_element(By.XPATH, "(//div[@class='oxd-select-text-input'])[2]").click()
            time.sleep(7)
            browser.find_element(By.XPATH, "(//div[@class='oxd-select-option'])[3]").click()
            time.sleep(7)
            browser.find_element(By.XPATH, "//textarea[@class='oxd-textarea oxd-textarea--active oxd-textarea--resize-vertical']").send_keys(
                "Good Attitude")
            time.sleep(7)
            browser.find_element(By.XPATH, "//button[normalize-space()='Create']").click()
            time.sleep(7)

        except Exception as e:
            pytest.fail(f"Test failed: {e}")

    def test_tc2(self, browser):

        self.login(browser)
        self.navigate_to_AssignClaims(browser)

        try:
            browser.find_element(By.CSS_SELECTOR, "[placeholder='Type for hints...']").send_keys("Jo")
            time.sleep(7)
            browser.find_element(By.XPATH, "//div[@class='oxd-autocomplete-option'][3]").click()
            time.sleep(7)
            browser.find_element(By.XPATH, "(//div[@class='oxd-select-text-input'])").click()
            time.sleep(7)
            browser.find_element(By.XPATH, "(//div[@class='oxd-select-option'][3])").click()
            time.sleep(7)
            browser.find_element(By.XPATH, "(//div[@class='oxd-select-text-input'])[2]").click()
            time.sleep(7)
            browser.find_element(By.XPATH, "(//div[@class='oxd-select-option'])[3]").click()
            time.sleep(7)
            browser.find_element(By.XPATH,
                                "//textarea[@class='oxd-textarea oxd-textarea--active oxd-textarea--resize-vertical']").send_keys(
                "Good Attitude")
            time.sleep(7)
            browser.find_element(By.XPATH, "(//button[@type='submit'])").click()
            time.sleep(7)

        except Exception as e:
            pytest.fail(f"Test failed: {e}")