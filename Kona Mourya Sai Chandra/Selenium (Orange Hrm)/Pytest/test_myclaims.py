import pytest
from selenium.webdriver.common.by import By
import time

class TestMyClaims:

    @staticmethod
    def login(browser, username="Admin", password="admin123"):
        """
        Helper method to log in to the application.
        """
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(5)
        browser.find_element(By.NAME, "username").send_keys(username)
        time.sleep(5)
        browser.find_element(By.NAME, "password").send_keys(password)
        time.sleep(5)
        browser.find_element(By.CSS_SELECTOR, ".oxd-button").click()
        time.sleep(5)

    @staticmethod
    def navigate_to_MyClaims(browser):
        """
        Helper method to navigate to the Employee Claims section.
        """
        browser.find_element(By.LINK_TEXT, "Claim").click()
        time.sleep(4)

        browser.find_element(By.LINK_TEXT, "My Claims").click()
        time.sleep(4)

    def test_tc8(self, browser):
        """
        Test case to filter claims based on criteria.
        """
        self.login(browser)
        self.navigate_to_MyClaims(browser)

        try:
            browser.find_element(By.XPATH, "(//input[@placeholder='Type for hints...'])[1]").send_keys(
                "202307180000003")
            time.sleep(2)

            browser.find_element(By.XPATH, "(//div[contains(text(),'-- Select --')])[1]").click()
            time.sleep(2)

            browser.find_element(By.XPATH, "//span[text()='Travel Allowance']").click()
            time.sleep(7)

            browser.find_element(By.XPATH, "(//div[@class='oxd-select-text-input'])[2]").click()

            browser.find_element(By.XPATH, "//span[text()='Approved']").click()
            time.sleep(4)

            # browser.find_element(By.XPATH, "(//input[@placeholder='yyyy-dd-mm'])[1]").click()
            # time.sleep(2)
            # current_date = datetime.now()next_date = current_date + timedelta(days=1)  # current date + 1
            # formatted_date = next_date.strftime("%Y-%d-%m")
            # browser.find_element(By.XPATH, "(//*[@placeholder='yyyy-dd-mm'])[1]").send_keys(formatted_date + Keys.TAB)
            #  #Keys.TAB clicks the tab key
            # time.sleep(5)

            browser.find_element(By.XPATH, "//button[normalize-space()='Search']").click()
            time.sleep(5)
        except Exception as e:
            pytest.fail(f"Test failed: {e}")

    def test_tc9(self, browser):
        """
        Test case to filter claims based on criteria.
        """
        self.login(browser)
        self.navigate_to_MyClaims(browser)

        try:
            browser.find_element(By.XPATH, "//button[normalize-space()='Search']").click()
            time.sleep(5)
        except Exception as e:
            pytest.fail(f"Test failed: {e}")

