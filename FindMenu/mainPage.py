# coding=utf-8
__auther__ = 'ya'

from FindMenu import basePage
from selenium.webdriver.common.by import By

class Main(basePage.Base):
    loginbutton_loc = (By.XPATH, 'a[href*="https://login.taobao.com/member/login.jhtml?"]')
    userprofile_loc = (By.XPATH, "a[class*='site-nav-login-info-nick']")
    exituser_loc = (By.XPATH, "a[href*='//login.taobao.com/member/logout.jhtml?']")

    def clickloginMenu(self):
        self.driver.find_element(*self.loginbutton_loc).click()

    def clickexitButton(self):
        self.driver.find_element(*self.exituser_loc).click()