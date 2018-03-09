from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

import unittest

class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://172.16.1.1:8090")
        print("Opened")

    def test_login(self):
        driver=self.driver
        cyberUsername = ""
        cyberPassword = ""
        usnfieldID = "//input[@name='username']"
        passfieldID = "//input[@name='password']"
        loginbuttonPath = "//input[@value='Login']"
        print("Starting Input")
        emailFieldElement = WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_xpath(usnfieldID))
        print("Entered email")
        passFieldElement = WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_xpath(passfieldID))
        print("Entered pass")
        loginButtonElement = WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_xpath(loginbuttonPath))
        print("Logging In....")
        emailFieldElement.clear()
        emailFieldElement.send_keys(cyberUsername)
        passFieldElement.clear()
        passFieldElement.send_keys(cyberPassword)
        loginButtonElement.click()
        print("Login Success")
        
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
