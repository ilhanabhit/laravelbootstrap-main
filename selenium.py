from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Library function to initialize the WebDriver
def initialize_webdriver():
    return webdriver.Chrome()

# Initialize the WebDriver using the library function
driver = initialize_webdriver()

try:
    # Open the web application
    driver.get("http://http://127.0.0.1:8000")  # Replace with your web application's URL

    # Example: Test login functionality
    # Locate the username field and input a test username
    username_field = driver.find_element(By.NAME, "username")  # Replace 'username' with the actual field name
    username_field.send_keys("testuser")

    # Locate the password field and input a test password
    password_field = driver.find_element(By.NAME, "password")  # Replace 'password' with the actual field name
    password_field.send_keys("testpassword")

    # Submit the login form
    password_field.send_keys(Keys.RETURN)

    # Wait for the page to load
    time.sleep(3)

    # Verify login success (example: check for a specific element on the dashboard)
    assert "Dashboard" in driver.title  # Replace with a more specific check if needed

    print("Login test passed!")

finally:
    # Close the browser
    driver.quit()
