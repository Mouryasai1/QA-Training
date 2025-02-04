from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
import time
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,"[placeholder='Username']").send_keys('Admin')
time.sleep(3)
driver.find_element(By.CSS_SELECTOR,"[placeholder='Password']").send_keys('admin123')
time.sleep(3)
driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()
time.sleep(3)
driver.find_element(By.LINK_TEXT,"Claim").click()
time.sleep(2)
driver.find_element(By.XPATH,"(//input[@placeholder='Type for hints...'])[2]").send_keys("111")
time.sleep(2)
driver.find_element(By.XPATH,"//*[@type='submit']").click()
time.sleep(5)


