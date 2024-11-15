from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up the driver
driver = webdriver.Chrome()
driver.maximize_window()

try:
    # Go to the login page
    driver.get("https://your-telephony-app.com/login")
    time.sleep(2)  # Wait for page to load

    # Login
    print("Logging in...")
    username = driver.find_element(By.ID, "username")
    password = driver.find_element(By.ID, "password")
    
    username.send_keys("test_user")
    password.send_keys("test_pass")
    
    login_btn = driver.find_element(By.ID, "login-btn")
    login_btn.click()
    
    # Wait for dashboard to load
    time.sleep(3)
    
    # Check if login worked
    if "dashboard" in driver.current_url:
        print("Login successful!")
    else:
        print("Login failed!")
        driver.quit()
        exit()

    # Go to dialer page
    print("Going to dialer page...")
    dialer_link = driver.find_element(By.ID, "dialer-menu")
    dialer_link.click()
    time.sleep(2)

    # Make a call
    print("Making a call...")
    phone_input = driver.find_element(By.ID, "phone-number")
    phone_input.send_keys("1234567890")
    
    call_button = driver.find_element(By.ID, "call-btn")
    call_button.click()

    # Wait for call to connect
    time.sleep(5)
    
    # Check if call connected
    call_status = driver.find_element(By.ID, "call-status")
    if "connected" in call_status.text.lower():
        print("Call connected successfully!")
    else:
        print("Call failed to connect!")

except Exception as e:
    print(f"Something went wrong: {str(e)}")

finally:
    # Clean up
    print("Closing browser...")
    driver.quit()