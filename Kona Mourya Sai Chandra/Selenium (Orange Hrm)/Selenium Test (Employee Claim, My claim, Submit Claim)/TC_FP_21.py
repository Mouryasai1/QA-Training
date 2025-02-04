import datetime

from selenium import webdriver
import datetime as dt
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
import time
# driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
# time.sleep(2)
# date = driver.find_element(By.XPATH, "(//input[@class='oxd-input oxd-input--focus'])[1]")
# time.sleep(2)
# current_date = datetime.date.today()
# next_date = current_date + dt.timedelta(days=1)  # current date + 1
# time.sleep(2)
# formatted_date = next_date.strftime("%Y-%d-%m")
# driver.find_element(By.XPATH, "(//*[@placeholder='yyyy-dd-mm'])[1]").send_keys(formatted_date + Keys.TAB)
# #Keys.TAB clicks the tab key
# time.sleep(5)
from selenium import webdriver
import datetime
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
driver.find_element(By.XPATH,"(//input[@class='oxd-input oxd-input--focus'])").send_keys("2024-12-24")
time.sleep(5)