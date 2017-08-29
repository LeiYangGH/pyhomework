# coding = utf-8
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
#driver = None
def get_current_page(driver):
    #是否每次滚动都会获取到所有重复的历史纪录？
    vedios = driver.find_elements_by_class_name("video_detail")
    descriptions = [v.find_element_by_tag_name('h3').text for v in vedios]
    return descriptions

def no_more_page(driver):
    #滚动到最底部看不见没有更多了元素，要回滚一下才看见
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight*4/5);")
    no_more_ele = driver.find_element_by_xpath("//*[contains(text(), '没有更多了')]")
    no_more = no_more_ele.is_displayed()
    print(no_more)
    return no_more
    #return '没有更多了' in driver.page_source

def sina_pic_tabs(browser='Chrome'):
    if browser == 'Chrome':
        driver = webdriver.Chrome(executable_path=r'C:\Installs\chromedriver.exe')
        print("Chrome")
    else:
        driver = webdriver.Firefox(executable_path=r'C:\Installs\geckodriver.exe')
        print("Firefox")
    driver.set_page_load_timeout(5)
    try:
        driver.get(r'http://v.163.com/special/video/#tech')
    except:
        driver.execute_script('window.stop()')
    if browser == 'Chrome':
        driver.maximize_window()
    else:
        driver.set_window_size("1024", "768")

    allpages_descriptions = []
    
    #for i in range(1,3):
    while not no_more_page(driver):
        allpages_descriptions = allpages_descriptions + get_current_page(driver)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(0.5)
        
    uniqueset = set(allpages_descriptions)
    print(uniqueset)
    driver.quit()
 
#sina_pic_tabs()
sina_pic_tabs("Firefox")
