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
   
    driver.get(r'http://v.163.com/special/video/#tech')
    if browser == 'Chrome':
        driver.maximize_window()
    else:
        driver.set_window_size("1024", "768")

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight/2);")

    vedios = driver.find_elements_by_class_name("video_detail")
    descriptions = [v.find_element_by_tag_name('h3').text for v in vedios]
    print(descriptions)
    driver.quit()
 
sina_pic_tabs()
#sina_pic_tabs("Firefox")