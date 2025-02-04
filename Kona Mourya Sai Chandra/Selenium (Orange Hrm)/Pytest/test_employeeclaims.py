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
    def navigate_to_claims(browser):

        browser.find_element(By.LINK_TEXT, "Claim").click()
        time.sleep(7)
        browser.find_element(By.LINK_TEXT, "Employee Claims").click()
        time.sleep(7)

    def test_tc1(self, browser):

        self.login(browser)
        self.navigate_to_claims(browser)

        try:
            browser.find_element(By.CSS_SELECTOR, "[placeholder='Type for hints...']").send_keys("sri"
                    )
            time.sleep(7)
            browser.find_element(By.XPATH, "//span[text()='sri chandra shekhar']").click()
            time.sleep(7)
            browser.find_element(By.XPATH, "(//input[@placeholder='Type for hints...'])[2]").send_keys(
                "202412090000029")
            time.sleep(7)
            browser.find_element(By.XPATH, "(//div[contains(text(),'-- Select --')])[1]").click()
            time.sleep(7)
            browser.find_element(By.XPATH, "//span[text()='Travel Allowance']").click()
            time.sleep(7)
            browser.find_element(By.XPATH, "(//div[@class='oxd-select-text-input'])[2]").click()
            time.sleep(7)
            browser.find_element(By.XPATH, "//span[text()='Paid']").click()
            time.sleep(7)
            browser.find_element(By.XPATH, "(//div[contains(text(),'Current Employees Only')])[1]").click()
            time.sleep(7)
            browser.find_element(By.XPATH, "//span[text()='Current Employees Only']").click()
            time.sleep(7)
            browser.find_element(By.XPATH, "//button[normalize-space()='Search']").click()
            time.sleep(7)
        except Exception as e:
            pytest.fail(f"Test failed: {e}")

    # def test_tc2(self, browser):
    #     """
    #     Test case to search for employee claims.
    #     """
    #     self.login(browser)
    #     self.navigate_to_claims(browser)
    #
    #     try:
    #         browser.find_element(By.XPATH, "//button[normalize-space()='Search']").click()
    #         time.sleep(7)
    #     except Exception as e:
    #         pytest.fail(f"Test failed: {e}")
    #
    # def test_tc3(self, browser):
    #     """
    #     Test case to filter claims based on criteria.
    #     """
    #     self.login(browser)
    #     self.navigate_to_claims(browser)
    #
    #     try:
    #
    #         browser.find_element(By.XPATH, "(//input[@placeholder='Type for hints...'])[2]").send_keys("202412090000025")
    #         time.sleep(7)
    #         browser.find_element(By.XPATH, "(//div[contains(text(),'-- Select --')])[1]").click()
    #         time.sleep(7)
    #         browser.find_element(By.XPATH, "//span[text()='Travel Allowance']").click()
    #         time.sleep(7)
    #         browser.find_element(By.XPATH, "(//div[@class='oxd-select-text-input'])[2]").click()
    #         time.sleep(7)
    #         browser.find_element(By.XPATH, "//span[text()='Initiated']").click()
    #         time.sleep(7)
    #         browser.find_element(By.XPATH, "(//div[contains(text(),'Current Employees Only')])[1]").click()
    #         time.sleep(7)
    #         browser.find_element(By.XPATH, "//span[text()='Current Employees Only']").click()
    #         time.sleep(7)
    #         browser.find_element(By.XPATH, "//button[normalize-space()='Search']").click()
    #         time.sleep(7)
    #     except Exception as e:
    #         pytest.fail(f"Test failed: {e}")
    #
    def test_tc4(self, browser):
        """
        Test case to filter claims based on criteria.
        """
        self.login(browser)
        self.navigate_to_claims(browser)

        try:
            browser.find_element(By.CSS_SELECTOR, "[placeholder='Type for hints...']").send_keys("sri"
                                                                                                 )
            time.sleep(7)
            browser.find_element(By.XPATH, "//span[text()='sri chandra shekhar']").click()
            time.sleep(7)
            browser.find_element(By.XPATH, "(//input[@placeholder='Type for hints...'])[2]").send_keys(
                "202412090000029")
            time.sleep(7)
            browser.find_element(By.XPATH, "(//div[contains(text(),'-- Select --')])[1]").click()
            time.sleep(7)
            browser.find_element(By.XPATH, "//span[text()='Travel Allowance']").click()
            time.sleep(7)
            browser.find_element(By.XPATH, "(//div[@class='oxd-select-text-input'])[2]").click()
            time.sleep(7)
            browser.find_element(By.XPATH, "//span[text()='Paid']").click()
            time.sleep(7)

            # browser.find_element(By.XPATH, "(//input[@placeholder='yyyy-dd-mm'])[1]").click()
            # time.sleep(2)
            # current_date = datetime.now()next_date = current_date + timedelta(days=1)  # current date + 1
            # formatted_date = next_date.strftime("%Y-%d-%m")
            # browser.find_element(By.XPATH, "(//*[@placeholder='yyyy-dd-mm'])[1]").send_keys(formatted_date + Keys.TAB)
            #  #Keys.TAB clicks the tab key
            # time.sleep(5)

            browser.find_element(By.XPATH, "(//div[contains(text(),'Current Employees Only')])[1]").click()
            time.sleep(2)

            browser.find_element(By.XPATH, "//span[text()='Current Employees Only']").click()
            time.sleep(4)

            browser.find_element(By.XPATH, "//button[normalize-space()='Search']").click()
            time.sleep(10)

        except Exception as e:
            pytest.fail(f"Test failed: {e}")
    #
    # def test_tc5(self, browser):
    #     """
    #     Test case to filter claims based on criteria.
    #     """
    #     self.login(browser)
    #     self.navigate_to_claims(browser)
    #
    #     try:
    #         browser.find_element(By.CSS_SELECTOR, "[placeholder='Type for hints...']").send_keys("@Peter")
    #         time.sleep(2)
    #
    #         browser.find_element(By.XPATH, "(//input[@placeholder='Type for hints...'])[2]").send_keys("20230718000003")
    #         time.sleep(2)
    #
    #         browser.find_element(By.XPATH, "(//div[contains(text(),'-- Select --')])[1]").click()
    #         time.sleep(2)
    #
    #         browser.find_element(By.XPATH, "//span[text()='Travel Allowance']").click()
    #         time.sleep(4)
    #
    #         browser.find_element(By.XPATH, "(//div[@class='oxd-select-text-input'])[2]").click()
    #         time.sleep(4)
    #         browser.find_element(By.XPATH, "//span[text()='Approved']").click()
    #         time.sleep(4)
    #
    #         # driver.find_element(By.XPATH, "(//input[@placeholder='yyyy-dd-mm'])[1]").click()
    #         # time.sleep(2)
    #         # current_date = datetime.now()next_date = current_date + timedelta(days=1)  # current date + 1
    #         # formatted_date = next_date.strftime("%Y-%d-%m")
    #         # driver.find_element(By.XPATH, "(//*[@placeholder='yyyy-dd-mm'])[1]").send_keys(formatted_date + Keys.TAB)
    #         #  #Keys.TAB clicks the tab key
    #         # time.sleep(5)
    #
    #         browser.find_element(By.XPATH, "(//div[contains(text(),'Current Employees Only')])[1]").click()
    #         time.sleep(2)
    #
    #         browser.find_element(By.XPATH, "//span[text()='Current Employees Only']").click()
    #         time.sleep(4)
    #
    #         browser.find_element(By.XPATH, "//button[normalize-space()='Search']").click()
    #         time.sleep(10)
    #     except Exception as e:
    #         pytest.fail(f"Test failed: {e}")
    #
    # def test_tc6(self, browser):
    #     """
    #     Test case to filter claims based on criteria.
    #     """
    #     self.login(browser)
    #     self.navigate_to_claims(browser)
    #
    #     try:
    #         browser.find_element(By.XPATH, "(//button[normalize-space()='Assign Claim'])[1]").click()
    #
    #         time.sleep(5)
    #     except Exception as e:
    #         pytest.fail(f"Test failed: {e}")
    #
    #
    def test_tc7(self, browser):
        """
        Test case to filter claims based on criteria.
        """
        self.login(browser)
        self.navigate_to_claims(browser)

        try:
            browser.find_element(By.CSS_SELECTOR, "[placeholder='Type for hints...']").send_keys("sri"
                                                                                                 )
            time.sleep(7)
            browser.find_element(By.XPATH, "//span[text()='sri chandra shekhar']").click()
            time.sleep(7)
            browser.find_element(By.XPATH, "(//input[@placeholder='Type for hints...'])[2]").send_keys(
                "202412090000029")
            time.sleep(7)
            browser.find_element(By.XPATH, "(//div[contains(text(),'-- Select --')])[1]").click()
            time.sleep(7)
            browser.find_element(By.XPATH, "//span[text()='Travel Allowance']").click()
            time.sleep(7)
            browser.find_element(By.XPATH, "(//div[@class='oxd-select-text-input'])[2]").click()
            time.sleep(7)
            browser.find_element(By.XPATH, "//span[text()='Paid']").click()
            time.sleep(7)

            # browser.find_element(By.XPATH, "(//input[@placeholder='yyyy-dd-mm'])[1]").click()
            # time.sleep(2)
            # current_date = datetime.now()next_date = current_date + timedelta(days=1)  # current date + 1
            # formatted_date = next_date.strftime("%Y-%d-%m")
            # browser.find_element(By.XPATH, "(//*[@placeholder='yyyy-dd-mm'])[1]").send_keys(formatted_date + Keys.TAB)
            #  #Keys.TAB clicks the tab key
            # time.sleep(5)

            browser.find_element(By.XPATH, "(//div[contains(text(),'Current Employees Only')])[1]").click()
            time.sleep(2)

            browser.find_element(By.XPATH, "//span[text()='Current Employees Only']").click()
            time.sleep(4)

            browser.find_element(By.XPATH, "//button[normalize-space()='Search']").click()
            time.sleep(5)

            browser.find_element(By.XPATH, "(//button[normalize-space()='View Details'])[1]").click()
            time.sleep(5)
        except Exception as e:
            pytest.fail(f"Test failed: {e}")
    #
    # def test_tc8(self, browser):
    #     """
    #     Test case to filter claims based on criteria.
    #     """
    #     self.login(browser)
    #     self.navigate_to_claims(browser)
    #
    #     try:
    #         browser.find_element(By.CSS_SELECTOR, "[placeholder='Type for hints...']").send_keys("Peter")
    #         time.sleep(4)
    #         browser.find_element(By.XPATH, "//span[text()='Peter Mac Anderson']").click()
    #         time.sleep(4)
    #
    #         browser.find_element(By.XPATH, "(//input[@placeholder='Type for hints...'])[2]").send_keys("202412060000007")
    #         time.sleep(4)
    #
    #         browser.find_element(By.XPATH, "(//div[contains(text(),'-- Select --')])[1]").click()
    #         time.sleep(4)
    #
    #         browser.find_element(By.XPATH, "//span[text()='Accommodation']").click()
    #         time.sleep(10)
    #
    #         browser.find_element(By.XPATH, "(//div[@class='oxd-select-text-input'])[2]").click()
    #         time.sleep(4)
    #         browser.find_element(By.XPATH, "//span[text()='Paid']").click()
    #         time.sleep(4)
    #
    #         # browser.find_element(By.XPATH, "(//input[@placeholder='yyyy-dd-mm'])[1]").click()
    #         # time.sleep(2)
    #         # current_date = datetime.now()next_date = current_date + timedelta(days=1)  # current date + 1
    #         # formatted_date = next_date.strftime("%Y-%d-%m")
    #         # browser.find_element(By.XPATH, "(//*[@placeholder='yyyy-dd-mm'])[1]").send_keys(formatted_date + Keys.TAB)
    #         #  #Keys.TAB clicks the tab key
    #         # time.sleep(5)
    #
    #         browser.find_element(By.XPATH, "(//div[contains(text(),'Current Employees Only')])[1]").click()
    #         time.sleep(2)
    #
    #         browser.find_element(By.XPATH, "//span[text()='Current Employees Only']").click()
    #         time.sleep(4)
    #
    #         browser.find_element(By.XPATH, "//button[normalize-space()='Search']").click()
    #         time.sleep(5)
    #
    #         browser.find_element(By.XPATH, "(//button[normalize-space()='View Details'])[1]").click()
    #         time.sleep(5)
    #     except Exception as e:
    #         pytest.fail(f"Test failed: {e}")

    def test_tc14(self, browser):
        """
        Test case to filter claims based on criteria.
        """
        self.login(browser)
        self.navigate_to_claims(browser)

        try:
            ref = browser.find_element(By.XPATH, "(//input[@placeholder='Type for hints...'])[2]")
            time.sleep(2)
            action = ActionChains(browser)
            action.click(ref).perform()
            time.sleep(2)
            action.send_keys("1")
            action.send_keys(Keys.DOWN).click().perform()
            time.sleep(2)
            action.send_keys(Keys.ARROW_DOWN)
            time.sleep(2)
            action.send_keys(Keys.ENTER).perform()
            time.sleep(2)
            browser.find_element(By.XPATH, "//button[normalize-space()='Search']").click()
            time.sleep(5)

        except Exception as e:
            pytest.fail(f"Test failed: {e}")

    def test_tc15(self, browser):
        """
        Test case to filter claims based on criteria.
        """
        self.login(browser)
        self.navigate_to_claims(browser)

        try:
            browser.find_element(By.XPATH, "(//div[@class='oxd-select-text--after'])[2]").click()
            time.sleep(2)
            browser.find_element(By.XPATH, "(//div[@class='oxd-select-option'])[4]").click()
            time.sleep(2)
            browser.find_element(By.XPATH, "(//button[@class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space'])").click()
            time.sleep(5)

        except Exception as e:
            pytest.fail(f"Test failed: {e}")

    def test_tc16(self, browser):
        """
        Test case to filter claims based on criteria.
        """
        self.login(browser)
        self.navigate_to_claims(browser)

        try:
            ref = browser.find_element(By.XPATH, "(//input[@placeholder='Type for hints...'])[2]")
            time.sleep(2)
            action = ActionChains(browser)
            action.click(ref).perform()
            time.sleep(2)
            action.send_keys("111111111111111111111111111111111111").perform()
            browser.find_element(By.XPATH, "//button[normalize-space()='Search']").click()
            time.sleep(5)

        except Exception as e:
            pytest.fail(f"Test failed: {e}")

    def test_tc17(self, browser):
        """
                        Test case to filter claims based on criteria.
                        """
        self.login(browser)
        self.navigate_to_claims(browser)

        try:
            browser.find_element(By.XPATH, "(//div[@class='oxd-select-text--after'])[2]").click()
            time.sleep(2)
            browser.find_element(By.XPATH, "(//div[@class='oxd-select-option'])[4]").click()
            time.sleep(2)
            browser.find_element(By.XPATH,
                                "(//button[@class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space'])").click()
            time.sleep(5)

        except Exception as e:
            pytest.fail(f"Test failed: {e}")

    def test_tc18(self, browser):
        """
                        Test case to filter claims based on criteria.
                        """
        self.login(browser)
        self.navigate_to_claims(browser)

        try:
            browser.find_element(By.XPATH, "(//div[@class='oxd-select-text--after'])[1]").click()
            time.sleep(2)
            browser.find_element(By.XPATH, "(//div[@class='oxd-select-option'])[3]").click()
            browser.find_element(By.XPATH,
                                "(//button[@class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space'])").click()
            time.sleep(5)
        except Exception as e:
            pytest.fail(f"Test failed: {e}")

    def test_tc19(self, browser):
        """
                        Test case to filter claims based on criteria.
                        """
        self.login(browser)
        self.navigate_to_claims(browser)

        try:
            browser.find_element(By.XPATH, "(//div[@class='oxd-select-text--after'])[2]").click()
            time.sleep(2)
            browser.find_element(By.XPATH, "(//div[@class='oxd-select-option'])[3]").click()
            time.sleep(2)
            browser.find_element(By.XPATH,
                                "(//button[@class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space'])").click()
            time.sleep(5)

        except Exception as e:
            pytest.fail(f"Test failed: {e}")

    def test_tc20(self, browser):
        """
                        Test case to filter claims based on criteria.
                        """
        self.login(browser)
        self.navigate_to_claims(browser)

        try:
            cal = browser.find_element(By.XPATH, "(//input[@class='oxd-input oxd-input--focus'])")
            date = datetime.datetime.strptime("2024-06-05", "%Y-%m-%d")
            cal.send_keys(date)
            browser.find_element(By.XPATH,
                                "(//button[@class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space'])").click()
            time.sleep(5)

        except Exception as e:
            pytest.fail(f"Test failed: {e}")

