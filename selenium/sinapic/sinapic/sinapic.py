# coding = utf-8
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

def sina_pic_tabs(browser='Chrome'):
    if browser == 'Chrome':
        driver = webdriver.Chrome(executable_path=r'C:\Installs\chromedriver.exe')
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

    tabs = driver.find_elements_by_class_name("subshow-tab-item")
    dic = {}
    for tab in tabs[1:len(tabs) - 1]:
    ##for tab in tabs[1:2]:
        tab.click()
        time.sleep(1)
        #subshow_cont = driver.find_element_by_id("column_subshow_cont_like")
        subshow_cont = driver.find_element_by_id("column_subshow_cont")
        #print(subshow_cont.get_attribute('outerHTML'))
        h3 = subshow_cont.find_elements_by_tag_name('h3')
        dic[tab.text] = [h.text for h in h3]
    print(dic)
    driver.quit()
 
sina_pic_tabs()
#sina_pic_tabs("Firefox")