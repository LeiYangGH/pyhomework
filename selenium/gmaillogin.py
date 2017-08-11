#coding:gbk
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time
driver=webdriver.Chrome(r'C:\Installs\chromedriver.exe')
driver.get('http://gmail.com')


emailElem = driver.find_element_by_id('identifierId')
emailElem.send_keys('leiyanghello@gmail.com')
nextButton = driver.find_element_by_class_name('CwaK9')

nextButton.click()

time.sleep(3)


actions = ActionChains(driver)
actions.send_keys('password')
actions.perform()
driver.find_element_by_class_name('CwaK9').click()
input("pause")

