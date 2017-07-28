# coding = utf-8

from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(r'C:\Installs\chromedriver.exe')
print("Chrome")

driver.get(r'https://zhidao.baidu.com/ihome/answer?tab=1')
inputElement = driver.find_element_by_id("userbar-login")
inputElement.click()
print("login")

inputElement = driver.find_element_by_id("TANGRAM__PSP_10__userName")
inputElement.click()
inputElement.send_keys('leiyang-ge@163.com')
print("user")
inputElement = driver.find_element_by_id("TANGRAM__PSP_10__password")
inputElement.click()
inputElement.send_keys('')
print("pwd")

inputElement = driver.find_element_by_id("TANGRAM__PSP_10__submit")
inputElement.click()
print("click")


#driver.quit()


