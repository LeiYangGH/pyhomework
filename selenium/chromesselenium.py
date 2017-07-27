# coding = utf-8

from selenium import webdriver

driver = webdriver.Chrome(r'C:\Installs\chromedriver.exe')

driver.get(r'http://www.baidu.com')

print(driver.title)

driver.quit()
