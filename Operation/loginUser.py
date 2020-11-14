# coding=utf-8
__auther__ = 'ya'

from FindMenu import basePage, loginPage, mainPage
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

    def login_User(self, userName, password):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.main.loginbutton_loc))
            self.main.clickloginMenu()
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.login.userName_loc))
            self.login.input_username(userName)
            self.login.input_password(password)
            self.login.click_loginbutton()
            if self.main.userprofile_loc.text() == userName:
                print("----login successfully----")
            else:
                print('---login failed----')
        except AssertionError as e:
            return e
            assert False

    def logout_User(self):
        try:
            self.driver.move_to_element(self.main.userprofile_loc)
            self.main.clickexitButton()
            if self.main.loginbutton_loc.is_displayed():
                print('----Logout successfully----')
                return True
        except:
            print('----logout failed----')
            return False

    def is_login(self):
        try:
            if self.driver.find_element_by_xpath(self.main.userprofile_loc).is_displayed():
                print("----User is login----")
            return True
        except:
            print('----User does not login now----')
            return False