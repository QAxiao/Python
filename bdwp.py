#coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time
import os

driver=webdriver.Chrome()

driver.get("http://www.baidu.com")
driver.maximize_window()
time.sleep(1)

driver.find_element_by_xpath('//*[@id="u1"]/a[6]').click()
time.sleep(2)

div=driver.find_element_by_xpath('//*[@id="passport-login-pop"]').find_element_by_name('userName')
div.clear()
div.send_keys('jily123')
driver.find_element_by_name('password').clear()
driver.find_element_by_name('password').send_keys('066682840')
driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_8__submit"]').submit()
time.sleep(2)

driver.find_element_by_id('kw').send_keys('wangpan')
driver.find_element_by_id('su').click()
title=driver.title
print "title is :",title
link=driver.current_url
print link
driver.implicitly_wait(10)

driver.find_element_by_xpath('//*[@id="1"]/h3/a').click()
driver.implicitly_wait(10)
title1=driver.title
print "title is :",title1
url1=driver.current_url
print url1

handles=driver.window_handles
driver.switch_to_window(handles[1])
title1=driver.title
print "title is :",title1
url1=driver.current_url
print url1
driver.implicitly_wait(10)

driver.find_element_by_xpath('/html/body/div[6]/div[1]').find_element_by_xpath('//*[@id="_disk_id_12"]').click()

inputs=driver.find_elements_by_tag_name('span')
n=0
for i in inputs:
    if i.get_attribute('node-type')=='chk':
        n=n+1
print 'Files number is : %d'%n
time.sleep(5)

driver.close()
    
