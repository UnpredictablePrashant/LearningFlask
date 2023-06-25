from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

# Initialize the Chrome Driver
driver = webdriver.Chrome()

# Open the login page
driver.get("http://localhost:8000/login")

# Find the email and password fields and enter data
email_field = driver.find_element("id","floatingInput")
email_field.send_keys("pk@test.com")

password_field = driver.find_element("id","floatingPassword")
password_field.send_keys("passwordpk")

# Find the submit button and click it
# /html/body/main/form/input
submit_button = driver.find_element("xpath","//input[@type='submit']")
submit_button.click()
sleep(2)

# When you're done, close the browser
driver.quit()
