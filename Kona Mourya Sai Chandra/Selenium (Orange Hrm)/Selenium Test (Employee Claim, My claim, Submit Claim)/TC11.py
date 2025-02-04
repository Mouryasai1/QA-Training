import time
import requests
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver import Keys
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# driver1 = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
time.sleep(2)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(2)
driver.find_element(By.NAME, "username").send_keys("Admin")
time.sleep(2)
driver.find_element(By.NAME, "password").send_keys("admin123")
button = driver.find_element(By.CSS_SELECTOR, '.oxd-button')
time.sleep(4)
if button.is_enabled():
    button.click()
else:
    print("Button is not enabled")
time.sleep(4)
driver.find_element(By.LINK_TEXT, "Claim").click()
time.sleep(4)

driver.find_element(By.LINK_TEXT, "My Claims").click()
time.sleep(4)

driver.find_element(By.XPATH, "(//input[@placeholder='Type for hints...'])[2]").send_keys("202412080000009")
time.sleep(2)

driver.find_element(By.XPATH, "(//div[contains(text(),'-- Select --')])[1]").click()
time.sleep(2)

driver.find_element(By.XPATH, "//span[text()='Medical Reimbursement']").click()
time.sleep(7)

driver.find_element(By.XPATH, "(//div[@class='oxd-select-text-input'])[2]").click()

driver.find_element(By.XPATH, "//span[text()='Initiated']").click()
time.sleep(4)

driver.find_element(By.XPATH, "(//input[@placeholder='yyyy-dd-mm'])[1]").click()
time.sleep(5)
# current_date = datetime.now()next_date = current_date + timedelta(days=1)  # current date + 1
# formatted_date = next_date.strftime("%Y-%d-%m")
# driver.find_element(By.XPATH, "(//*[@placeholder='yyyy-dd-mm'])[1]").send_keys(formatted_date + Keys.TAB)
#  #Keys.TAB clicks the tab key
# time.sleep(5)

driver.find_element(By.XPATH, "//button[normalize-space()='Search']").click()
time.sleep(5)


driver.find_element(By.XPATH, "//button[normalize-space()='View Details']").click()
time.sleep(2)



