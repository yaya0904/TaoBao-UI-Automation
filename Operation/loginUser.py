# coding=utf-8
__auther__ = 'ya'

from FindMenu import loginPage, mainPage
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common import action_chains

class Login(object):
    #define the class method, other method can call it directly
    def __init__(self, webdriver):
        self.driver = webdriver
        self.login = loginPage.Loginpage(self.driver)
        self.main = mainPage.Main(self.driver)

    def login_User(self, userName, passWord, assertType):
        try:
            self.driver.maximize_window()
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.main.loginbutton_loc))
            self.main.clickloginMenu()
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.login.userName_loc))
            self.login.input_username(userName)
            self.login.input_password(passWord)
            self.login.click_loginbutton()
            time.sleep(3)
            if self.login.auth_scrollbar().is_displayed():
                self.login.drop_scroll()
                self.login.click_loginbutton()
            else:
                pass
            if assertType == 'success':
                WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.main.userprofile_loc))
                if self.driver.find_element_by_xpath(self.main.userprofile_path).text == userName:
                    print("----login successfully----")
            else:
                pass
        except AssertionError as e:
            return e
            assert False

    def logout_User(self):
        try:
            userlocation = self.driver.find_element(self.main.userprofile_loc)
            action_chains.ActionChains(self.driver).move_to_element(userlocation).perform()
            self.main.clickexitButton()
            if self.main.loginbutton_loc.is_displayed():
                print('----Logout successfully----')
                return True
        except:
            print('----logout failed----')
            return False
            assert False

    def is_login(self):
        try:
            #time.sleep(2)
            if self.driver.find_element_by_xpath(self.main.userprofile_loc).is_displayed():
                print("----User is login----")
            return True
        except:
            print('----User does not login now----')
            return False