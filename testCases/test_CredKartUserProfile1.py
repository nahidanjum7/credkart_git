import random
import string
import time
import pytest

from selenium import webdriver
from pageObjects import LoginPage
from pageObjects.LoginPage import LoginPageClass
from pageObjects.RegistrationPage import RegistrationClass
from Utilities.readconfig import Readconfig
from Utilities.Logger import LogGenerator

#from foldername.filename import classname


@pytest.mark.usefixtures("setup")
class Test_UserProfile:
    UserEmail=Readconfig.getUserEmail()  #variable=class.getmethod
    UserPassword=Readconfig.getUserPassword() #variable=class.getmethod

    UserName = Readconfig.getUserName()  # variable=class.getmethod
    UserPwd = Readconfig.getUserPwd() # variable=class.getmethod
    UserCnfPwd = Readconfig.getUserCnfPwd() # variable=class.getmethod

    log=LogGenerator.logg() #variable=class.method


    def test_Userlogin(self,setup):
       # self.log.info("This is info") #this is message
       # self.log.warning("This is warning")  # this is message
       # self.log.error("This is error")  # this is message
       # self.log.critical("This is critical")  # this is message

       self.log.info("Testcase test_Userlogin is started")
       self.log.info("Opening browser")
       self.driver=setup  #this is the fixture captured from confest

       self.lp=LoginPageClass(self.driver) #imported Pageobject of login class

       self.lp.Enter_UName(self.UserEmail)  #hard code values replace
       self.log.info("Entering Username-->" + self.UserEmail)
       # print("UserEmail: ", self.UserEmail)

       self.lp.Enter_UPwd(self.UserPassword) #hard code values replace
       self.log.info("Entering Userpassword-->" + self.UserPassword)
       # print("UserPassword: ", self.UserPassword)

       self.lp.Enter_loginclick()
       self.log.info("Click on login button")

       if self.lp.Validate_Status() == "Test Case Passed":
           self.log.info("Testcase test_UserLogin is passed")
           self.driver.save_screenshot("..\\Screenshot\\test_Userlogin_pass.png")
           assert True
       else:
           self.log.info("Testcase test_UserLogin is failed")
           self.driver.save_screenshot("..\\Screenshot\\test_Userlogin_fail.png")
           assert False

       self.log.info("Testcase test_Userlogin is completed")

    def test_UserRegistration(self,setup):
        self.log.info("Testcase test_UserRegistration is started")

        self.driver=setup   #this is the fixture captured from confest
        self.rp=RegistrationClass(self.driver) #imported Pageobject of Register class

        self.driver.get("https://automation.credence.in/register")
        self.log.info("Opening browser")

        self.rp.Enter_Uname(self.UserName)
        self.log.info("Entering Username-->" + self.UserName)  #hard code values replace

        email=Generate_Email()  ##object created of generate method
        self.rp.Enter_Uemail(email)
        # print(email)
        # self.rp.Enter_Uemail("Credence_tpest1225@test.com")

        self.rp.Enter_Upwd(self.UserPwd)
        self.log.info("Entering Userpassword-->" + self.UserPwd) #hard code values replace

        self.rp.Enter_Ucnfpwd(self.UserCnfPwd)
        self.log.info("Entering User Confirm password-->" + self.UserCnfPwd)  #hard code values replace

        self.rp.Enter_Registerclick()
        self.log.info("Click on register button")

        self.lp=LoginPageClass(self.driver)

        if self.lp.Validate_Status() == "Test Case Passed":
            self.log.info("Testcase test_UserRegistration is passed")
            self.driver.save_screenshot("..\\Screenshot\\test_Userlogin_pass.png")
            assert True
        else:
            self.log.info("Testcase test_UserRegistration is failed")
            self.driver.save_screenshot("..\\Screenshot\\test_Userlogin_fail.png")
            assert False
        self.log.info("Testcase test_UserRegistration is Completed")
def Generate_Email():
    username=''.join(random.choices(string.ascii_lowercase, k=7)) #random 4 character lower case eg. poiuhjk
    domain = random.choice(['gmail.com','ymail.com','outlook.com'])
    return f"{username}@{str(domain)}" #random 4 character + domain name


# # pytest -v -s -n=2 --html=HtmlReports/report.html --browser chrome/edge/firefox


