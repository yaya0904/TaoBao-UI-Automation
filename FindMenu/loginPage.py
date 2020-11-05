# coding=utf-8
__auther__ = 'ya'

from FindMenu import basePage
from selenium.webdriver.common.by import By

class Loginpage(basePage.Base):
    userName_loc = (By.ID, 'fm-login-id')
    passWord_loc = (By.ID, 'm-login-password')
    loginButton_loc = (By.XPATH, '//*[@id="login-form"]/div[4]/button')

    def input_username(self, username):
        self.find_element(*self.userName_loc).send_key(username)

    def input_password(self, password):
        self.find_element(*self.passWord_loc).send_key(password)

    def click_loginbutton(self):
        self.find_element(*self.loginButton_loc).Click()