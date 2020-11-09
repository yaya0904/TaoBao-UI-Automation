# coding=utf-8
__auther__ = 'ya'

from FindMenu import basePage
from selenium.webdriver.common.by import By

class Main(basePage.Base):
    loginbutton_loc = (By.CSS_SELECTOR, '[href="https://login.taobao.com/member/login.jhtml?f=top&redirectURL=https%3A%2F%2Fwww.taobao.com%2F"]')
    userprofile_loc = (By.XPATH, '//*[@id="J_SiteNavLogin"]/div[1]/div[2]/a')