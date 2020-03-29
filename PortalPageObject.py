import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def try_to_click(self, By, path):
        str_error = None
        for x in range(5):
            try:
                element = self.driver.find_element(By, path)
                element.click()
                str_error = None
                print("click success")
            except Exception as e:
                print(e)
                str_error = True
                pass
            if str_error:
                time.sleep(2)
                print("try click again")
            else:
                break

    def try_get_text(self, By, path):
        str_error = None
        for x in range(5):
            try:
                element = self.driver.find_element(By, path)
                text = element.text
                return text
            except Exception as e:
                print(e)
                str_error = True
                pass
            if str_error:
                time.sleep(2)
                print("try get text again")
            else:
                break

    def send_key(self, by, path, keys):
        element = self.driver.find_element(by, path)
        element.send_keys(keys)

    def switch_frame(self, by, xpath):
        str_error = None
        for x in range(5):
            try:
                frame = self.driver.find_element_by_xpath(xpath)
                self.driver.switch_to.frame(frame)
                str_error = None
                print("switch success")
            except Exception as e:
                print(e)
                str_error = True
                pass
            if str_error:
                time.sleep(2)
                print("try switch again")
            else:
                break

    def select_ddl_by_value(self, by, path, value):
        element = self.driver.find_element(by, path)
        element = Select(element)
        element.select_by_index(value)


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://support.getac.com/Portal/SetLanguage?languageCode=en")
        self.driver.set_window_size(1024, 768)

    account = (By.ID, 'account')
    password = (By.ID, 'password')
    submitButton = (By.XPATH, '//*[@id="loginForm"]/div[4]/button')
    name = (By.XPATH, '/html/body/div[1]/div[2]/nav/ul/li[2]/div/a')
    driverManualsButton = (By.XPATH, '/html/body/div[3]/div[3]/div[3]/div[1]/div[1]/h5')
    warrantyCheckButton = (By.XPATH, '/html/body/div[3]/div[3]/div[3]/div[1]/div[2]/h5')
    serviceRepairButton = (By.XPATH, '/html/body/div[3]/div[3]/div[3]/div[2]/div[1]/h5')
    productRegistrationButton = (By.XPATH, '/html/body/div[3]/div[3]/div[3]/div[2]/div[3]/h5')
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
        nameItem = self.driver.find_element(*LoginPage.name)
        return nameItem.text

    def click_DriverManualsBtn(self):
        self.try_to_click(*LoginPage.driverManualsButton)
        return DriverSoftware(self.driver)

    def click_warranty_check(self):
        self.try_to_click(*LoginPage.warrantyCheckButton)
        return WarrantyCheck(self.driver)

    def click_service_repair(self):
        self.try_to_click(*LoginPage.serviceRepairButton)
        time.sleep(1)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        return GSS(self.driver)

    def click_product_registration(self):
        self.try_to_click(*LoginPage.productRegistrationButton)
        return ProductRegistration(self.driver)


class DriverSoftware(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    inputBox = (By.ID, 'txtkeyword')
    submitBtn = (By.ID, 'hplSubmit')
    ResultIfFound = (By.XPATH, '//*[@id="divFileList"]/h3')
    titleIfResultNotFound = (By.ID, 'spaMessage')
    iframe = (By.XPATH, '/html/body/div[3]/div[2]/div/p/iframe')
    title = (By.ID, 'lblTitle')
    ddlProductList = (By.ID, 'ddlProductList')
    ddlModelList = (By.ID, 'ddlModelList')
    ddlGroupList = (By.ID, 'ddlGroupList')
    ddlOSList = (By.ID, 'ddlOSList')

    def click_input_box(self):
        self.try_to_click(*DriverSoftware.inputBox)

    def send_keys_input_box(self, keys):
        self.send_key(*DriverSoftware.inputBox, keys)

    def switch_iframe(self):
        self.switch_frame(*DriverSoftware.iframe)

    def click_submit(self):
        self.try_to_click(*DriverSoftware.submitBtn)

    def getResultIfFound(self):
        return self.try_get_text(*DriverSoftware.ResultIfFound)

    def get_title(self):
        return self.try_get_text(*DriverSoftware.title)

    def select_model_list(self, value):
        self.select_ddl_by_value(*DriverSoftware.ddlModelList, value)

    def select_group_list(self, value):
        self.select_ddl_by_value(*DriverSoftware.ddlGroupList, value)

    def select_product_list(self, value):
        self.select_ddl_by_value(*DriverSoftware.ddlProductList, value)

    def select_os_list(self, value):
        self.select_ddl_by_value(*DriverSoftware.ddlOSList, value)


class WarrantyCheck(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    iframe = (By.XPATH, '/html/body/div[3]/div[2]/div/p/iframe')
    pageTitle = (By.XPATH, '/html/body/div/div/div/div[1]/form/div[1]/table/tbody/tr/td[1]/h2')
    inputBox = (By.ID, 'sn')

    def switch_iframe(self):
        self.switch_frame(*WarrantyCheck.iframe)

    def get_title(self):
        return self.try_get_text(*WarrantyCheck.pageTitle)

    def send_keys_input_box(self, keys):
        self.send_key(*WarrantyCheck.inputBox, keys)

class GSS(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    pageTitle = (By.XPATH, '//*[@id="page-wrapper"]/div/div[1]/div/div/div[1]')

    def get_title(self):
        return self.try_get_text(*GSS.pageTitle)


class ProductRegistration(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    step2element = (By.ID, 'step2')
    iframe = (By.XPATH, '/html/body/div[3]/div[2]/div/p[1]/iframe')

    def get_title(self):
        return self.try_get_text(*ProductRegistration.step2element)

    def switch_iframe(self):
        self.switch_frame(*ProductRegistration.iframe)


class ServicePortalTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
    '''
    def test_login_correct_account(self):
        account = "samjason515@gmail.com"
        password = "123"
        name = "liao weitung"
        login_page = LoginPage(self.driver)
        login_page.login(account, password)
        assert login_page.getName() == name

    def test_driver_manuals(self):
        expectResult = "S410G2 (52628862XXXX)"
        expectTitle = "Download"
        login_page = LoginPage(self.driver)
        driverSoftware_page = login_page.click_DriverManualsBtn()
        driverSoftware_page.switch_iframe()
        driverSoftware_page.click_input_box()
        driverSoftware_page.send_keys_input_box('RJA03S1418')
        driverSoftware_page.click_submit()
        assert driverSoftware_page.getResultIfFound() == expectResult
        assert driverSoftware_page.get_title() == expectTitle
        driverSoftware_page.select_product_list(1)
        driverSoftware_page.select_model_list(1)
        driverSoftware_page.select_group_list(1)
        driverSoftware_page.select_os_list(1)
        assert driverSoftware_page.get_title() == expectTitle
    

    def test_warranty_check(self):
        expectTitle = 'Serial Number: '
        login_page = LoginPage(self.driver)
        warranty_page = login_page.click_warranty_check()
        warranty_page.switch_iframe()
        assert warranty_page.get_title() == expectTitle
        warranty_page.send_keys_input_box('test')
        assert warranty_page.get_title() == expectTitle

    
    def test_service_repair(self):
        account = "samjason515@gmail.com"
        password = "Getac123"
        expectTitle = 'GETAC SERVICE CENTER'
        login_page = LoginPage(self.driver)
        login_page.login(account, password)
        GSS_page = login_page.click_service_repair()
        assert GSS_page.get_title() == expectTitle
    '''
    def test_product_registration(self):
        account = "samjason515@gmail.com"
        password = "Getac123"
        expectTitle = 'Step 2.'
        login_page = LoginPage(self.driver)
        login_page.login(account, password)
        productRegistration_page = login_page.click_product_registration()
        productRegistration_page.switch_iframe()
        assert productRegistration_page.get_title() == expectTitle

if __name__ == "__main__":
    unittest.main()
