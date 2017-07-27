# coding = utf-8

from selenium import webdriver
import time
driver = webdriver.Chrome(r'C:\Installs\chromedriver.exe')

def navigate_page_home():
    driver.get(r'http://localhost:801/')

def navigate_page_txt():
    driver.get(r'http://localhost:801/Txt')
    elems = driver.find_elements_by_xpath("//a[@href]")
    for txturl in [e.get_attribute("href") for e in elems]:
        #txturl = elem.get_attribute("href")
        print (txturl)
        if('txt' in txturl):
            driver.get(txturl)
        time.sleep(1)

navigate_page_txt()
driver.get(r'http://localhost:801/Txt')
#print(driver.title)

#driver.quit()

