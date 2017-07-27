# coding = utf-8

from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(r'C:\Installs\chromedriver.exe')


driver.get(r'http://dnvmmsisb1.prod.mcafee.com/Home/Index?ReturnUrl=%2fSubscription')
inputElement = driver.find_element_by_id("UserName")
inputElement.send_keys('sinayeth')
inputElement = driver.find_element_by_id("Password")
inputElement.send_keys('notsecure')

driver.find_element_by_xpath("//input[@type='submit']").click()

inputElement = driver.find_element_by_id("McafeeEmail")
inputElement.send_keys('inmon726hw13@mailinator.com')

driver.find_element_by_xpath("//input[@type='submit']").click()

trs = driver.find_elements(By.TAG_NAME, "tr") 

for tr in trs:
    tds = tr.find_elements(By.TAG_NAME, "td")
    print([el.text for el in  tds])
    print("")


#driver.quit()


