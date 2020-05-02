"""
Python Script to Log in to reddit directly.

The following script only functions for Windows Users who have Chrome Installed.

"""
from selenium import webdriver

# Initialize selenium web driver
device = webdriver.Chrome('Drivers/chromedriver.exe')
device.get("https://www.reddit.com/login/?dest=https%3A%2F%2Fwww.reddit.com%2F")


# Initialize the 'Enter_Reddit_Username' area with your Reddit Username
emailbox = device.find_element_by_xpath('//*[@id="loginUsername"]')
emailbox.send_keys("Enter_Reddit_Username")


# Initialize the 'Enter_Reddit_Password' area with your Reddit Password
passwordbox = device.find_element_by_xpath('//*[@id="loginPassword"]')
passwordbox.send_keys("Enter_Reddit_Password")


# Procced for Login
submitbtn = device.find_element_by_xpath(
    '/html/body/div/div/div[2]/div/form/div/fieldset[5]/button')
submitbtn.click()
