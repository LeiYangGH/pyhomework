# coding = utf-8

from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(r'C:\Installs\chromedriver.exe')
print("Chrome")

driver.get(r'http://photo.sina.com.cn/')
driver.maximize_window()
driver.execute_script("window.scrollTo(0, document.body.scrollHeight/2);")
div = driver.find_element_by_class_name("column-subshow-tab")
#print(type(div))
#print(type(div.text))
print(div.text)
#print(div.get_attribute('innerHTML'))
#div.location_once_scrolled_into_view
print("scrolled")
#subs = div.find_elements_by_xpath(".//*")
subs = div.find_elements_by_xpath(".//ul/*")
#sub0 = div.findElement(By.xpath("./ul/li"));
#[print(sb.text) for sb in subs]
for sb in subs:
    if len(sb.text) >= 2:
        sb.click()
        time.sleep(1)
 

input("exit?")
driver.quit()



