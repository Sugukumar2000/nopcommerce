import datetime
import time

from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

class AddCustomer:
    lnkcustomermainmenu_xpath = "//a[@href='#']" # //span[contains(text(),'Customer')]"
    time.sleep(15)
    lnkCustomer_submenu_xpath = "//a[@href='/Admin/Customer/List']"

    btnaddnew_xpath = "//a[@class='btn btn-primary']"
    txtEmail_xpath = "//input[@id='Email']"
    txtPass_xpath = "//input[@id='Password']"
    txtfname_xpath = "//input[@id='FirstName']"
    txtlname_xpath = "//input[@id='LastName']"
    rdmalegender_xpath = "//input[@id='Gender_Male']"
    rdfemalegender_xpath = "//input[@id='Gender_Female']"
    txtdob_xpath = "//input[@id='DateOfBirth']"
    txtcompname_xpath = "//input[@id='Company']"
    ckboxtax_id = "IsTaxExempt"
    txtnewsletter_id = "//input[@id='SelectedNewsletterSubscriptionStoreIds']"
    Newsletteroption_store_xpath = "//option[contains(text(),'Your store name')]"
    Newsletteroption_teststore_xpath = "//option[contains(text(),'Test store 2')]"

    txtcustomerrole_xpath="//ul[@id='SelectedCustomerRoleIds_taglist']"
    liAdminrole_xpath = "//option[contains(text(),'Administrators')]"
    limoderators_xpath = "//option[contains(text(),'Forum Moderators')]"
    lireg_xpath = "//option[contains(text(),'Registered')]"
    liguest_xpath = "//option[contains(text(),'Guests')]"
    cmbx_vendor_id = "VendorId"
    cmbop_vendor1_xpath = "//option[contains(text(),'Vendor 1')]"
    cmbop_vendor2_xpath = "//option[contains(text(),'Vendor 2')]"
    ckbx_Active_id = "Active"
    admin_cmt_xpath = "//textarea[@id='AdminComment']"
    btsave_xpath = "//button[@name='save']"

    def __init__(self,driver):
        self.driver=driver

    def clickoncustmermainmenu(self):
        self.driver.find_element(By.XPATH,self.lnkcustomermainmenu_xpath).click()

    def clickoncustmersubmenu(self):
        self.driver.find_element(By.XPATH ,self.lnkCustomer_submenu_xpath).click()

    def addnew(self):
        self.driver.find_element(By.XPATH, self.btnaddnew_xpath).click()

    def setemail(self,email):
        self.driver.find_element(By.XPATH, self.txtEmail_xpath).send_keys(email)

    def setpsd(self,password):
        self.driver.find_element(By.XPATH, self.txtEmail_xpath).send_keys(password)

    def setfname(self,fname):
        self.driver.find_element(By.XPATH, self.txtfname_xpath).send_keys(fname)

    def setlname(self,lname):
        self.driver.find_element(By.XPATH, self.txtlname_xpath).send_keys(lname)

    def setgender(self,gender):
        if gender == "Gender_Male":
            self.driver.find_element(By.XPATH, self.rdmalegender_xpath).click()
        else:
            self.driver.find_element(By.XPATH, self.rdfemalegender_xpath).click()

    def setdob(self,dob):
        self.driver.find_element(By.XPATH, self.txtdob_xpath).send_keys(dob)


    def setcustomerrole(self,role):
        self.driver.find_element(By.XPATH, self.txtcustomerrole_xpath).click()
        time.sleep(5)
        if role=="Administrators":
            # Select.select_by_value("Administrators")
            self.driver.find_element(By.XPATH, self.liAdminrole_xpath).click()
        elif role  == "Forum Moderators":
            self.driver.find_element(By.XPATH, self.limoderators_xpath).click()
        elif role   == "Registered":
            self.driver.find_element(By.XPATH, self.lireg_xpath).click()
        elif role == "Guests":
            self.driver.find_element(By.XPATH, self.liguest_xpath).click()
        time.sleep(5)

    def setadmincmt(self,adcmt):
        self.driver.find_element(By.XPATH, self.admin_cmt_xpath).send_keys(adcmt)

    def clicksave(self):
        self.driver.find_element(By.XPATH, self.btsave_xpath).click()

