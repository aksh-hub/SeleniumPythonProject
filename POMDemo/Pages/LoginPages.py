
from selenium.webdriver.common.by import By
from POMDemo.Locators.locators import Locators

class LoginPage():
    def __init__(self,driver):
        self.driver=driver

        # self.username_textbox_name="username"
        # self.password_textbox_name="password"
        # self.login_button_xpath="//button[contains(@class,'login-button')]"

        self.username_textbox_name = Locators.username_textbox_name
        self.password_textbox_name=Locators.password_textbox_name
        self.login_button_xpath=Locators.login_button_xpath

    def enter_Username(self,username):
        self.driver.find_element(By.NAME, self.username_textbox_name).clear()
        self.driver.find_element(By.NAME, self.username_textbox_name).send_keys(username)

    def enter_Password(self,password):
        self.driver.find_element(By.NAME,self.password_textbox_name).clear()
        self.driver.find_element(By.NAME, self.password_textbox_name).send_keys(password)

    def click_Login(self):
        self.driver.find_element(By.XPATH,self.login_button_xpath).click()
