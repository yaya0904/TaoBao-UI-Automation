from selenium import webdriver
import time
wd = webdriver.Chrome(r'/Users/yaya/Desktop/ChromeDriver/chromedriver')
time.sleep(2)
wd.get('http://www.baidu.com')
pass