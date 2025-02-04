import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize the WebDriver
driver = webdriver.Chrome()

time.sleep(7)

# Open the URL
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(7)

# Enter username
driver.find_element(By.NAME, "username").send_keys("Admin")
time.sleep(7)

# Enter password
driver.find_element(By.NAME, "password").send_keys("admin123")
time.sleep(7)

# Click on login button
button = driver.find_element(By.CSS_SELECTOR, ".oxd-button")
time.sleep(7)
if button.is_enabled():
    button.click()
else:
    print("Button is not enabled")
time.sleep(7)

# Navigate to Claim
try:
    driver.find_element(By.LINK_TEXT, "Claim").click()
    time.sleep(7)

    # Click on Submit Claim
    driver.find_element(By.LINK_TEXT, "Submit Claim").click()
    time.sleep(7)

    # Interact with dropdowns and options
    driver.find_element(By.XPATH, "(//div[@class='oxd-select-text-input'])").click()
    time.sleep(7)
    driver.find_element(By.XPATH, "(//div[@class='oxd-select-option'][3])").click()
    time.sleep(7)

    driver.find_element(By.XPATH, "(//div[@class='oxd-select-text-input'])[2]").click()
    time.sleep(7)
    driver.find_element(By.XPATH, "(//div[@class='oxd-select-option'])[3]").click()
    time.sleep(7)

    # Enter comments
    driver.find_element(By.XPATH, "//textarea[@class='oxd-textarea oxd-textarea--active oxd-textarea--resize-vertical']").send_keys("Good Attitude")
    time.sleep(7)

    # Submit the form
    driver.find_element(By.XPATH, "(//button[@type='submit'])").click()
    time.sleep(7)

except Exception as e:
    print(f"An error occurred: {e}")

# Close the WebDriver
driver.quit()
