# coding=utf-8
__auther__ = 'ya'

from FindMenu import loginPage, mainPage
from Operation import loginUser
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import unittest
import ddt
import sys
from utility import excel, HTMLTestRunner, logger
from selenium.webdriver import ChromeOptions
import os

path = sys.path[0]
ex = excel.ExcelUtil(path + r'/Case/case_login.xls', 'different login')

@ddt.ddt
class Login(unittest.TestCase):
    def setUp(self):
        self.resultpath = '/Users/yaya/Desktop/TaoBao UI automation/screenshot'
        self.driver = webdriver.Chrome(r'/Users/yaya/Desktop/ChromeDriver/chromedriver')
        self.driver.get('https://www.taobao.com')
        self.loginOpe = loginUser.Login(self.driver)
        self.main = mainPage.Main(self.driver)
        self.loginpage = loginPage.Loginpage(self.driver)

    def assert_check(self, login_Ornot, assertionKey):
        try:
            time.sleep(1)
            if login_Ornot == 'success':
                WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.main.userprofile_loc))
                user = self.driver.find_element_by_xpath(self.main.userprofile_path).text
                assert assertionKey == user
                print('------logined user is: %s------' %user)
                print('-----Login user successfully, pass!-----')
                logger.Log().info('------------login successfully! %s---------' %user)
                #self.loginOpe.logout_User()
            elif login_Ornot == 'fail':
                print('-------assertionKey: %s-------'%assertionKey)
                errorMessage = self.driver.find_element_by_xpath(self.loginpage.error_message_path).text
                assert errorMessage == assertionKey
                print('--------login failed, pass %s-------' %errorMessage)
        except AssertionError as e:
            return e
            logger.Log().info('-------Case failed: %s-----', e)
            assert False

    @ddt.data(*ex.next())
    def test_Login(self, data):
        try:
            casenum = str(data['num'])
            username = str(data['username'])
            password = str(data['password'])
            run_ornot = int(data['run'])
            loginresult = str(data['login_result'])
            if run_ornot == 0:
                print('--------No need to run this case: %s, just pass it -------'%casenum)
                return
            else:
                print('-------start to test %s--------'%casenum)
                # ChromeOptions.add_experimental_option('excludeSwitches'['enable-automation'])
                if self.loginOpe.is_login():
                    self.loginOpe.logout_User()
                self.loginOpe.login_User(username, password, loginresult)
                self.assert_check(data['login_result'], data['keywords'])
        except AssertionError as e:
            return e
            logger.Log.info("------Case failed! %s------" %e)
            assert False

    def tearDown(self):
        self.driver.quit()
        print('--------------Finish this case!-----------')

if __name__ == '__main__':
    suit = unittest.TestLoader().loadTestsFromTestCase(Login)
    result = '/Users/yaya/Desktop/TaoBao UI automation/testresult/login_result.html'
    fb = open(result, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fb, title="Login_TestResult", description="Login_TestResult")
    unittest.TextTestRunner(verbosity=2).run(suit)
    fb.close()