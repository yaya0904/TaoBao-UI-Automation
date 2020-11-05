# coding=utf-8
__auther__ = 'ya'

from FindMenu import basePage
from selenium.webdriver.common.by import By

class Main(basePage.Base):
    loginbutton_loc = (By.CLASS_NAME, 'h')
    userprofile_loc = (By.XPATH, '//*[@id="J_SiteNavLogin"]/div[1]/div[2]/a')