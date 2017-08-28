# coding = utf-8

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
#driver = None
def sina_pic_tabs(browser='Chrome'):
    if browser == 'Chrome':
        driver = webdriver.Chrome(r'C:\Installs\chromedriver.exe')
        print("Chrome")
    else:
        driver = webdriver.Firefox(executable_path=r'C:\Installs\geckodriver.exe')
        print("Firefox")
    

    driver.get(r'http://photo.sina.com.cn/')
    if browser == 'Chrome':
        driver.maximize_window()
    else:
        driver.set_window_size("1024", "768")


    driver.execute_script("window.scrollTo(0, document.body.scrollHeight/2);")
    div = driver.find_element_by_class_name("column-subshow-tab")
    print(div.text)
    div.location_once_scrolled_into_view
    print("scrolled")
    subs = div.find_elements_by_xpath(".//ul/*")
    for sb in subs:
        if len(sb.text) >= 2:
            sb.click()
            time.sleep(1)
    input("exit?")
    driver.quit()
 
sina_pic_tabs()
#sina_pic_tabs("Firefox")




