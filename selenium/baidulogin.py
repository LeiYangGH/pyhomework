#coding:gbk
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time
driver=webdriver.Chrome(r'C:\Installs\chromedriver.exe')
driver.get('http://www.baidu.com')


driver.find_elements_by_name(r'tj_login')[1].click()
time.sleep(6)

driver.find_element_by_name('userName').send_keys('leiyang-ge@163.com')
driver.find_element_by_name('password').send_keys('my pasword')
time.sleep(6)
driver.find_element_by_id('TANGRAM__PSP_10__submit').click()

try:
    dr=WebDriverWait(driver,10)#10秒内每隔500毫秒扫描1次页面变化，当出现指定的元素后结束,driver就是上面的句柄
    '''WebDriverWait参见下：
http://selenium.googlecode.com/svn/trunk/docs/api/py/webdriver_support/selenium.webdriver.support.wait.html'''
    dr.until(lambda the_driver:the_driver.find_element_by_css_selector('.user-name-top').is_displayed())
except  Exception:
    print ('登录失败')   
user=driver.find_element_by_id('s_username_top')   
#user=driver.find_element_by_css_selector('.user-name-top')
webdriver.ActionChains(driver).move_to_element(user).perform()#鼠标定位到用户名

