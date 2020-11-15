# coding=utf-8
__auther__ = 'ya'

from FindMenu import basePage
from selenium.webdriver.common.by import By

class Main(basePage.Base):
    loginbutton_loc = (By.XPATH, '//*[@id="J_SiteNavLogin"]/div[1]/div[1]/a[1]')
    userprofile_loc = (By.XPATH, '//*[@id="J_SiteNavLogin"]/div[1]/div[2]/a[1]')
    userprofile_path = '//*[@id="J_SiteNavLogin"]/div[1]/div[2]/a[1]'
    exituser_loc = (By.XPATH, '//*[@id="J_SiteNavLoginPanel"]/div/div[2]/p[1]/a[2]')

    def clickloginMenu(self):
        self.driver.find_element(*self.loginbutton_loc).click()

    def clickexitButton(self):
        self.driver.find_element(*self.exituser_loc).click()