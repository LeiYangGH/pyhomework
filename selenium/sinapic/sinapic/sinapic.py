# coding = utf-8

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from pyquery import PyQuery as pq
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
    #print(div.text)
    div.location_once_scrolled_into_view
    print("scrolled")
    subs = div.find_elements_by_xpath(".//ul/*")
    dic = {}
    for sb in subs:
        if len(sb.text) >= 2:
            sb.click()
            time.sleep(1)

            details = driver.find_elements_by_class_name("pic_detail")
            titles = [d.text for d in details if len(d.text)>1]
            dic[sb.text] = titles

    #input("exit?")
    print(dic)
    driver.quit()
 
sina_pic_tabs()
#sina_pic_tabs("Firefox")




