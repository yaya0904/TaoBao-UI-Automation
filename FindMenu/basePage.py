#encoding=utf-8
__auther__ = 'ya'

from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC


class Base():
    # redefine driver
    def __init__(self, webdriver):
        self.driver = webdriver

    # redefine find element
    def find_element(self, *loc):
        # return self.driver.find_element(*loc)
        try:
            WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element(*loc).is_displayed())
            return self.driver.find_element(*loc)
        except AssertionError as e:
            return e
            print('maybe cannot find the element %s element'%(self.loc))

    def send_key(self, key, loc, clean_first=True, click_first=True):
        try:
            # get the loc value
            loc = getattr(self, '%s'%(loc))
            if click_first:
                self.find_element(loc).click()
            if clean_first:
                self.find_element(loc).clean()
                self.find_element(loc).send_key(key)
        except AssertionError as e:
            return e