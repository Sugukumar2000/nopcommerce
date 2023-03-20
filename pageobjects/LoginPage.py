from selenium import webdriver
from selenium.webdriver.common.by import By

class login:
    Tbox_username = "Email"
    Tbox_password = "Password"

    Login_button= "//button[contains(text(),'Log in')]"
    Logout_link = "Logout"

    def __init__(self,driver):
        self.driver = driver

    def setusername(self,username):
        self.driver.find_element(By.ID, self.Tbox_username).clear()
        self.driver.find_element(By.ID, self.Tbox_username).send_keys(username)

    def setpassword(self,password):
        self.driver.find_element(By.ID,self.Tbox_password).clear()
        self.driver.find_element(By.ID,self.Tbox_password).send_keys(password)

    def clicklogin(self):
        self.driver.find_element(By.XPATH,self.Login_button).click()

    def clickloginout(self):
        self.driver.find_element(By.LINK_TEXT,self.Logout_link).click()
