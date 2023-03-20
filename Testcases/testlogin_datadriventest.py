import time

import pytest
from selenium import webdriver
from pageobjects.LoginPage import login
from Utilities.readproperties import readconfig
from Utilities.customlogger import loggen
from Utilities import XLUltly
# import warnings

class Test_02_DDT_Login:
    baseURL = readconfig.getbaseurl()
    path = ".//TestData//Loginexcel.xlsx"

    logger = loggen.LogGen()

    def test_DDT_login(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseURL)

        self.lp = login(self.driver)

        self.rows= XLUltly.getRowCount(self.path,'Sheet1')
        print("no of rows",self.rows)

        for i in range(2,self.rows+1):
            self.user = XLUltly.readdata(self.path,'Sheet1',i,1)
            self.paswrd = XLUltly.readdata(self.path, 'Sheet1', i, 2)
            self.exp = XLUltly.readdata(self.path, 'Sheet1', i, 3)
            self.lp.setusername(self.user)
            self.lp.setpassword(self.paswrd)
            self.lp.clicklogin()
            time.sleep(5)
            print('DDT_login success for :',self.user)

            Act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"
            lst_status=[]  # to Store the login status in an array

            if Act_title ==  exp_title:
                if self.exp=="Pass":
                    print("Login Title Matched")
                    lst_status.append("pass")
                    self.lp.clickloginout()
                    print("logged out from :", self.user)
                elif self.exp=="Fail":
                    print("Login Title Not Matched")
                    lst_status.append("fail")
                    self.driver.save_screenshot(".\\Screenshot\\"+"test_login.png")
                    self.lp.clickloginout()
                    print("logged out from :", self.user)
                Act_title = ""
                print("title is Empty",Act_title)
            elif Act_title !=  exp_title:
                if self.exp=="Pass":
                    print("Login Title Not Matched")
                    lst_status.append("fail")
                    self.driver.save_screenshot(".\\Screenshot\\" + "test_login.png")
                elif self.exp=="Fail":
                    print("Login Title Matched")
                    lst_status.append("pass")
                Act_title = ""
                print("title is Empty", Act_title)
        if "fail" not in lst_status:
            print("DDT test is passed")
            assert True
        else:
            print("DDT test is failed")
            assert False
        self.driver.close()
