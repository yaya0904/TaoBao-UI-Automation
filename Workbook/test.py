from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from FindMenu import loginPage, mainPage, basePage
from selenium.webdriver.common import action_chains

wd = webdriver.Chrome(r'/Users/yaya/Desktop/ChromeDriver/chromedriver')
time.sleep(2)

wd.get('https://www.taobao.com')
wd.implicitly_wait(5)
loginpath = '//*[@id="J_SiteNavLogin"]/div[1]/div[1]/a[1]'
action_chains.ActionChains(wd).move_to_element(wd.find_element_by_xpath(loginpath)).perform()
# userprofile_loc1 = wd.find_element_by_xpath(path)
# userprofile_loc1.click()
#text = wd.find_element_by_xpath(path).text
#print('username: %s'%text)
wd.quit()
pass