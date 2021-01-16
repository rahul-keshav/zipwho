from selenium import webdriver
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from shutil import which
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import random
from basic import sheet_length,zip_code,county,city,save_cred

chrome_path = which('chromedriver.exe')
chrome_options = Options()
# chrome_options.add_argument('--headless')
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("start-maximized")


driver = webdriver.Chrome(executable_path = chrome_path,options=chrome_options)

driver.get("http://zipwho.com/")
time.sleep(5)
l = sheet_length()
for k in range(l+1):
    city_= city(k)
    zip_ = zip_code(k)
    county_ = county(k)

    zip_box = driver.find_element_by_xpath('//*[@id="ui_zip"]')
    zip_box.send_keys('0')
    zip_box.send_keys(int(zip_))
    time.sleep(1)
    search_btm = driver.find_element_by_xpath('//*[@id="search"]/p[2]/input[2]')
    search_btm.click()
    time.sleep(5)
    output = driver.find_elements_by_xpath('//*[@id="details_table"]/table/tbody/tr')
    output_data = [city_,zip_,county_]

    for i in range(2,19):
        xpath = '//*[@id="details_table"]/table/tbody/tr['+str(i) +']/td[2]'
        text = driver.find_element_by_xpath(xpath).text
        output_data.append(text)
    print(output_data)
    # data saved to csv file.
    save_cred(output_data)


    # clear the zip code box
    zip_box = driver.find_element_by_xpath('//*[@id="ui_zip"]')
    zip_box.clear()    

driver.quit()
