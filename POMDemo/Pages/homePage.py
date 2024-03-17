import time

from selenium.webdriver.common.by import By
from POMDemo.Locators.locators import Locators
class HomePage():
    def __init__(self,driver):
        self.driver=driver

        # self.welcome_link_className="oxd-userdropdown-name"
        # self.logout_linkText="Logout"

        self.welcome_link_className=Locators.welcome_link_className
        self.logout_linkText=Locators.logout_linkText


    def click_welcome(self):
        time.sleep(2)
        self.driver.find_element(By.CLASS_NAME, self.welcome_link_className).click()

    def click_Logout(self):
        time.sleep(2)
        self.driver.find_element(By.LINK_TEXT, self.logout_linkText).click()
