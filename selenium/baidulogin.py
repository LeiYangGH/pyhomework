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
    dr=WebDriverWait(driver,10)#10����ÿ��500����ɨ��1��ҳ��仯��������ָ����Ԫ�غ����,driver��������ľ��
    '''WebDriverWait�μ��£�
http://selenium.googlecode.com/svn/trunk/docs/api/py/webdriver_support/selenium.webdriver.support.wait.html'''
    dr.until(lambda the_driver:the_driver.find_element_by_css_selector('.user-name-top').is_displayed())
except  Exception:
    print ('��¼ʧ��')   
user=driver.find_element_by_id('s_username_top')   
#user=driver.find_element_by_css_selector('.user-name-top')
webdriver.ActionChains(driver).move_to_element(user).perform()#��궨λ���û���

