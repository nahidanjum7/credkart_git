from selenium.webdriver.common.by import By


class LoginPageClass:
    Text_username_Xpath="//input[@id='email']"
    Text_Password_ID="password"
    Click_LoginButton_Xpath="//button[@type='submit']"
    Validate_Status_Xpath="//h2[normalize-space()='CredKart']"

    def __init__(self,driver):
        self.driver=driver

    def Enter_UName(self,name):
        self.driver.find_element(By.XPATH,self.Text_username_Xpath).send_keys(name)

    def Enter_UPwd(self,pwd):
        self.driver.find_element(By.ID, self.Text_Password_ID).send_keys(pwd)

    def Enter_loginclick(self):
        self.driver.find_element(By.XPATH, self.Click_LoginButton_Xpath).click()

    def Validate_Status(self):
        try:
            self.driver.find_element(By.XPATH,self.Validate_Status_Xpath)
            print("TestCase is Passed")
            return "Test Case Passed"
        except:
            print("TestCase is Failed")
            return "TestCase Failed"


