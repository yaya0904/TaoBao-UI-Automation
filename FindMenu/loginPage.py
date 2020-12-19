# coding=utf-8
__auther__ = 'ya'

from FindMenu import basePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class Loginpage(basePage.Base):
    userName_loc = (By.ID, 'fm-login-id')
    passWord_loc = (By.ID, 'fm-login-password')
    loginButton_loc = (By.CSS_SELECTOR, '.fm-btn')
    error_message_path = "//*[@class='login-error-msg']"  # message xpath
    auth_scroll = (By.ID, 'nc_1__scale_text')  # ID for scroll bar
    scroll_menu = (By.ID, 'nc_1_n1z')
    scrollsuccess_msgbox = '//div[@id="nc_1__scale_text"]/span'  # xpath for scroll success message

    def input_username(self, username):
        self.find_element(*self.userName_loc).send_keys(username)

    def input_password(self, password):
        self.find_element(*self.passWord_loc).send_keys(password)

    def click_loginbutton(self):
        self.find_element(*self.loginButton_loc).click()

    def drop_scroll(self):
        scroll_bar = self.find_element(*self.scroll_menu)
        ActionChains(self.driver).drag_and_drop_by_offset(scroll_bar, 400, 0).perform()

    def auth_scrollbar(self):
        self.auth = self.find_element(*self.auth_scroll)
        return self.auth