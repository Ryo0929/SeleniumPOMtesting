import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.webdriver.support.ui import WebDriverWait
class BasePage:
    def __init__(self,driver):
        self.driver=driver
    def tryToClick(self,By,path):
        str_error=None
        for x in range(10):
            try:
                element=self.driver.find_element(By,path)
                element.click()
                str_error=None
                print("click success")
            except Exception as e:
                print(e)
                str_error=True
                pass
            if str_error:
                time.sleep(2)
                print("try click-",x)
            else:
                break
class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://support.getac.com/")
        self.driver.set_window_size(1960,1280)
    account = (By.ID, 'account')
    password = (By.ID,'password')
    submitButton = (By.XPATH,'//*[@id="loginForm"]/div[4]/button')
    name=(By.XPATH,'/html/body/div[1]/div[2]/nav/ul/li[2]/div/a')
    driverManualsButton=(By.XPATH,'/html/body/div[3]/div[3]/div[3]/div[1]/div[1]/h5')
    def set_email(self, account):
        emailElement = self.driver.find_element(*LoginPage.account)
        emailElement.send_keys(account)
    def set_password(self, password):
        pwordElement = self.driver.find_element(*LoginPage.password)
        pwordElement.send_keys(password)        
    def click_submit(self):
        submitBttn = self.driver.find_element(*LoginPage.submitButton)
        submitBttn.click()
    def login(self, account, password):
        self.set_password(password)
        self.set_email(account)
        self.click_submit()
    def getName(self):
    	nameItem=self.driver.find_element(*LoginPage.name)
    	return nameItem.text
    def click_DriverManualsBtn(self):
        self.tryToClick(*LoginPage.driverManualsButton)
        return DriverSoftware(self.driver)
        #targetBtn.click()

class DriverSoftware(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    inputBox=(By.NAME,'txtkeyword')
    submitBtb=(By.ID,'hplSubmit')
class ServicePortalTest(unittest.TestCase):
    """A sample test class to show how page object works"""

    def setUp(self):
        self.driver = webdriver.Chrome()

    #def test_login_correct_account(self):
    #	account="samjason515@gmail.com"
    #	password="Getac123"
    #	name="liao weitung"
    #	login_page = LoginPage(self.driver)
    #	login_page.login(account,password)
    #	print("HERE",login_page.getName())
    #	assert login_page.getName()==name
    def test_DriverManuals(self):
        account="samjason515@gmail.com"
        password="Getac123"
        name="liao weitung"
        login_page = LoginPage(self.driver)
        login_page.login(account,password)
        driverSoftware_page=login_page.click_DriverManualsBtn()
    #def tearDown(self):
        

if __name__ == "__main__":
    unittest.main()