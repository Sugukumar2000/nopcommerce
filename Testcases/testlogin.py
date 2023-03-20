import pytest
from selenium import webdriver
from pageobjects.LoginPage import login
from Utilities.readproperties import readconfig
from Utilities.customlogger import loggen

# import warnings

class Test_01_Login:
    baseURL = readconfig.getbaseurl()
    username = readconfig.getusername()
    password = readconfig.getpassword()

    logger = loggen.LogGen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_homepagetitle(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseURL)
        acc_title = self.driver.title
        self.logger.info("***Test_01_Login***")
        self.logger.info("verifying title")

        if acc_title == "Your store. Login":
            assert True
            # self.driver.close()
            self.logger.info("titile verification successful")
        else:
            self.driver.save_screenshot(".\\Screenshot\\"+"test_homepagetitle.png")
            # self.driver.close()
            assert False
            # self.logger. error ("titile verification is not ok")


        self.driver.close()

    @pytest.mark.regression
    def test_login(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseURL)
        self.lp = login(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.clicklogin()
        print('login success through test login')
        Act_title = self.driver.title

        if Act_title == "Dashboard / nopCommerce administration" :
             assert True
        else:
            self.driver.save_screenshot(".\\Screenshot\\"+"test_login.png")
            assert False

        #self.lp.clickloginout()
        #print("logged out now")
        #self.driver.close()

        #self.logger.warning(UserWarning)

    #@pytest.Mark.optionalhook
    #def pytest_metadata(self):
    #self.pop("JAVA_HOME",None)
    #self.pop("Plugins", None)
