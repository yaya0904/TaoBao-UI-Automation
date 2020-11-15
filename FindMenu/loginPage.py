# coding=utf-8
__auther__ = 'ya'

from FindMenu import basePage
from selenium.webdriver.common.by import By

class Loginpage(basePage.Base):
    userName_loc = (By.ID, 'fm-login-id')
    passWord_loc = (By.ID, 'fm-login-password')
    loginButton_loc = (By.CSS_SELECTOR, '.fm-btn')
    error_message_loc = (By.XPATH, "//*[@class='login-error-msg']")

    def input_username(self, username):
        self.find_element(*self.userName_loc).send_keys(username)

    def input_password(self, password):
        self.find_element(*self.passWord_loc).send_keys(password)

    def click_loginbutton(self):
        self.find_element(*self.loginButton_loc).click()