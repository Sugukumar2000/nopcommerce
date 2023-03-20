import time

import pytest
import datetime
from pageobjects.LoginPage import login
from pageobjects.Addnewcustomer import AddCustomer
from Utilities.readproperties import readconfig
from Utilities.customlogger import loggen
import string
import random
from selenium.webdriver.common.by import By
from selenium import webdriver


class Test_003_addnewcustomer:
    baseURL = readconfig.getbaseurl()
    username = readconfig.getusername()
    password = readconfig.getpassword()

    logger = loggen.LogGen() # for adding logs

    @pytest.mark.sanity
    def test_addcustomer(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseURL)
        self.driver.maximize_window()


        self.lp = login(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.clicklogin() # calls login test
        print('login success-add customer')

        self.addcust = AddCustomer(self.driver)
        #self.addcust.clickoncustmermainmenu() # click main menu

        #self.addcust.clickoncustmersubmenu()
        self.baseURL = "https://admin-demo.nopcommerce.com/Admin/Customer/List"
        self.driver.get(self.baseURL)
        self.addcust.addnew()
        self.addcust.setemail("sugu@gmail.com")
        self.addcust.setpsd("admin")
        self.addcust.setfname("Sugu")
        self.addcust.setlname("Kumar")

        self.addcust.setdob("3/18/2010")
        self.addcust.setadmincmt("ok")
        self.addcust.clicksave()

        msg= self.driver.find_element(By.TAG_NAME,"body")
        print(msg)
        print("added new customer")

        self.driver.close()


