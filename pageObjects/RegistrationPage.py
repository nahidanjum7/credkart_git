from selenium.webdriver.common.by import By


class RegistrationClass:
    Text_UserName_ID="name"
    Text_UserEmail_ID="email"
    Text_Password_Name="password"
    Text_ConfirmPwd_Name="password_confirmation"
    Click_Register_Button_XPATH="//button[@type='submit']"
    Validate_Status_XPATH="//h2[normalize-space()='CredKart']"

    def __init__(self,driver):
        self.driver=driver

    def Enter_Uname(self,name):
        self.driver.find_element(By.ID,self.Text_UserName_ID).send_keys(name)

    def Enter_Uemail(self,email):
        self.driver.find_element(By.ID,self.Text_UserEmail_ID).send_keys(email)

    def Enter_Upwd(self,pwd):
        self.driver.find_element(By.NAME,self.Text_Password_Name).send_keys(pwd)

    def Enter_Ucnfpwd(self,cnfpwd):
        self.driver.find_element(By.NAME,self.Text_ConfirmPwd_Name).send_keys(cnfpwd)

    def Enter_Registerclick(self):
        self.driver.find_element(By.XPATH,self.Click_Register_Button_XPATH).click()









