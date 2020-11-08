from  FindMenu import loginPage, mainPage
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
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

    @ddt.data(*ex.next())
    def test_Login(self):

    def tearDown(self):

if __name__ == '__main__':
    suit = unittest.TestLoader().loadTestsFromTestCase()
    unittest.TextTestRunner(verbosity=2).run(suit)