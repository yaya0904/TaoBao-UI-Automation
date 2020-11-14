from FindMenu import loginPage, mainPage
from Operation import loginUser
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import unittest
import ddt
import sys
from utility import excel

path = sys.path[0]
ex = excel.ExcelUtil(path + r'/Case/case_login.csv', 'login for different account')

@ddt.ddt
class Login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(r'/Users/yaya/Desktop/ChromeDriver/chromedriver')
        self.driver.get('https://www.taobao.com')
        self.loginOpe = loginUser.Login(self.driver)
        self.mainpage = mainPage.Main(self.driver)
        self.loginpage = loginPage.Loginpage(self.driver)

    def assert_check(self, login_ornot, assertionKey):
        try:
            time.sleep(1)
            if login_ornot == 'success':
                WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.mainpage.userprofile_loc).display())
                user = self.driver.find_element_by_xpath("a[class*='site-nav-login-info-nick']")
                assert assertionKey == user
                print('-----Login user successfully, pass!-----')
            elif login_ornot == 'fail':
                keyword = self.loginpage.error_message_lco.text()
                assert keyword == assertionKey
                print('--------login failed, pass %s-------'%keyword)
        except AssertionError as e:
            return e
            assert False

    @ddt.data(*ex.next())
    def test_Login(self, data):
        try:
            testNum = data['case num']
            username = data['userName']
            password = data['password']
            if self.loginOpe.is_login():
                self.loginOpe.logout_User()
            self.loginOpe.login_User(username, password)
            self.assert_check(data['login_result'], data['keywords'])
        except AssertionError as e:
            return e
            assert False

    def tearDown(self):
        self.loginOpe.logout_User()
        self.driver.quit()
        print('--------------Finish this case!-----------')

if __name__ == '__main__':
    suit = unittest.TestLoader().loadTestsFromTestCase(Login)
    unittest.TextTestRunner(verbosity=2).run(suit)