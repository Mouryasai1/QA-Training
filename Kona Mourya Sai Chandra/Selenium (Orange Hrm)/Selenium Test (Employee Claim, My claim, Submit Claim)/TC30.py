import time
import requests
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

time.sleep(7)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(7)
driver.find_element(By.NAME, "username").send_keys("Admin")
time.sleep(7)
driver.find_element(By.NAME, "password").send_keys("admin123")
time.sleep(7)
button = driver.find_element(By.CSS_SELECTOR, '.oxd-button')
time.sleep(7)
if button.is_enabled():
    button.click()
else:
    print("Button is not enabled")
time.sleep(7)
driver.find_element(By.LINK_TEXT, "Claim").click()
time.sleep(7)
driver.find_element(By.LINK_TEXT, "Assign Claim").click()
time.sleep(7)
driver.find_element(By.LINK_TEXT, "Assign Claim")
time.sleep(7)
driver.find_element(By.CSS_SELECTOR, "[placeholder='Type for hints...']")
time.sleep(7)
text2 = "Jo"
driver.find_element(By.CSS_SELECTOR, "[placeholder='Type for hints...']").send_keys(text2)
time.sleep(7)
driver.find_element(By.XPATH, "//div[@class='oxd-autocomplete-option'][3]").click()
time.sleep(7)
driver.find_element(By.XPATH, "(//div[@class='oxd-select-text-input'])").click()
time.sleep(7)
driver.find_element(By.XPATH, "(//div[@class='oxd-select-option'][3])").click()
time.sleep(7)
driver.find_element(By.XPATH, "(//div[@class='oxd-select-text-input'])[2]").click()
time.sleep(7)
driver.find_element(By.XPATH, "(//div[@class='oxd-select-option'])[3]").click()
time.sleep(7)
driver.find_element(By.XPATH, "//textarea[@class='oxd-textarea oxd-textarea--active oxd-textarea--resize-vertical']").send_keys("Good Attitude")
time.sleep(7)
driver.find_element(By.XPATH, "(//button[@type='submit'])").click()
time.sleep(7)
