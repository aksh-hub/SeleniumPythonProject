"""
# 1. Create 2 folder Test & pages
# 2. Create simple test
# 3. Convert to unit test
# 4. Implement POM
#     -- Identify all objects and action methods on the pages
#  and create a class for each web pages
# 5. Import the page classes in the test class
# 6. Create object ffor page classes to access methods and create the tests
# 7. Run & Validate """

from selenium import webdriver
from selenium.webdriver.common.by import By
from  selenium.webdriver.common.keys import Keys
import time
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
from POMDemo.Pages.LoginPages import LoginPage
from POMDemo.Pages.homePage import HomePage
import HtmlTestRunner
class LoginOrangeTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)

    def test_login_valid(self):
        driver=self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")

        login=LoginPage(driver)
        login.enter_Username("Admin")
        login.enter_Password("admin123")
        login.click_Login()

        home=HomePage(driver)
        home.click_welcome()
        home.click_Logout()


        #self.driver.get("https://opensource-demo.orangehrmlive.com/")

        # self.driver.find_element(By.NAME, "username").send_keys("Admin")
        # self.driver.find_element(By.NAME, "password").send_keys("admin123")
        # self.driver.find_element(By.XPATH, "//button[contains(@class,'login-button')]").click()
        # self.driver.find_element(By.CLASS_NAME, "oxd-userdropdown-name").click()
        # self.driver.find_element(By.LINK_TEXT, "Logout").click()

    @classmethod
    def tearDownClass(cls):
        time.sleep(3)
        cls.driver.close()
        cls.driver.quit()

if __name__=='__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/ashetti/PycharmProjects/SeleniumProject/Report1"))

print("Test completed")