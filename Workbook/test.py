from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from FindMenu import loginPage, mainPage, basePage
from selenium.webdriver.common import action_chains
from Operation import loginUser

# wd = webdriver.Chrome(r'/Users/yaya/Desktop/ChromeDriver/chromedriver')
# time.sleep(2)
#
# wd.get('https://www.taobao.com')
# wd.implicitly_wait(5)
# #loginpath = '//*[@id="J_SiteNavLogin"]/div[1]/div[1]/a[1]'
# #action_chains.ActionChains(wd).move_to_element(wd.find_element_by_xpath(loginpath)).perform()
# # userprofile_loc1 = wd.find_element_by_xpath(path)
# # userprofile_loc1.click()
# #text = wd.find_element_by_xpath(path).text
# #print('username: %s'%text)
# username = 'fanghuiya6'
# psw = 'fanghuiya2008'
# loginUser.Login(wd).login_User(username, psw, 'fail')
# time.sleep(2)
# #dropbox_loca = (By.ID, 'nc_1__scale_text')
# dropbox_loca = wd.find_element_by_id('nc_1__scale_text')
# print(dropbox_loca)
# dropmenu = wd.find_element_by_id('nc_1_n1z')
# auth = wd.find_element_by_xpath('//div[@id="nc_1__scale_text"]/span')
# if dropbox_loca.is_displayed():
#     print('the scroll bar is enable')
#     action_chains.ActionChains(wd).drag_and_drop_by_offset(dropmenu, 400, 0).perform()
#     wd.find_element_by_css_selector('.fm-btn').click()
# #time.sleep(3600)
# wd.quit()
# pass